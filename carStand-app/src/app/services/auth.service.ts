import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { AuthData } from '../interfaces/authData';
import { FavoriteService } from './favorite.service';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseURL: string = environment.apiBaseUrlApi;

  private authStateSubject = new BehaviorSubject<AuthData>({
    authenticated: false,
    isManager: false,
    username: '',
    favoriteCarList:[],
    favoriteMotoList:[],
  });

  authState$ = this.authStateSubject.asObservable();
  constructor(private favoriteService: FavoriteService) {
    this.checkAuthStatus();
  }

  async signUp(userData: { username: string, email: string, first_name: string, last_name: string, password: string }): Promise<any> {
    const url = `${this.baseURL}/signup`;
    const response = await fetch(url, {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
      body: JSON.stringify(userData),
    });

    const result = await response.json();
    await this.checkAuthStatus();
    this.setFavorites()
    return result;
  }

  async login(username: string, password: string): Promise<any> {
    const url = `${this.baseURL}/login`;
    const response = await fetch(url, {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
      body: JSON.stringify({ username, password }),
    });
    const result = await response.json();
    await this.checkAuthStatus();
    this.setFavorites()
    return result;
  }

  async logout(): Promise<any> {
    await this.sendFavorites();
    const url = `${this.baseURL}/logout`;
    const response = await fetch(url, {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
    });

    const result = await response.json();
    await this.checkAuthStatus();
    return result;
  }

  async checkAuthStatus(): Promise<void> {
    try {
      const url = `${this.baseURL}/isAuth`;
      const response = await fetch(url);
      const data: AuthData = await response.json();
      this.authStateSubject.next(data);
    } catch (error) {
      console.error('Erro ao verificar autenticação:', error);
      this.authStateSubject.next({
        authenticated: false,
        isManager: false,
        username: '',
        favoriteCarList:[],
        favoriteMotoList:[],
      });
    }
  }

  setFavorites(): void{
  const authState = this.authStateSubject.value;
    this.favoriteService.initializeList("favoriteCarList",authState.favoriteCarList)
    this.favoriteService.initializeList("favoriteMotoList",authState.favoriteMotoList)
  }
  

  async sendFavorites(): Promise<void>{
    await this.favoriteService.sendFavoritesToBackend('cars', "favoriteCarList");
    await this.favoriteService.sendFavoritesToBackend('motos', "favoriteMotoList");
    this.favoriteService.clearFavorite("favoriteCarList")
    this.favoriteService.clearFavorite("favoriteMotoList")
  }
}
