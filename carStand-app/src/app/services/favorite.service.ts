import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FavoriteService {
  private baseURL: string = environment.apiBaseUrlApi;

  constructor() { }

  initializeList(storageKey: string, list: number[] = []): void {
    if (!sessionStorage.getItem(storageKey)) {
      sessionStorage.setItem(storageKey, JSON.stringify(list));
    }
  }

  getFavorites(storageKey: string): number[] {
    const favorites = sessionStorage.getItem(storageKey);
    return favorites ? JSON.parse(favorites) : [];
  }



  isFavorite(storageKey: string, itemId: number): boolean {
    const favorites = this.getFavorites(storageKey);
    return favorites.includes(itemId);
  }

  toggleFavorite(storageKey: string, itemId: number): boolean {
    const favorites = this.getFavorites(storageKey);
    const isFavorite = favorites.includes(itemId);

    if (isFavorite) {
      const updatedFavorites = favorites.filter(id => id !== itemId);
      sessionStorage.setItem(storageKey, JSON.stringify(updatedFavorites));
    } else {
      favorites.push(itemId);
      sessionStorage.setItem(storageKey, JSON.stringify(favorites));
    }

    return !isFavorite;
  }

  clearFavorite(storageKey: string): void {
    if (sessionStorage.getItem(storageKey)) {
      sessionStorage.removeItem(storageKey);
    }
  }


  async sendFavoritesToBackend(type: string, storageKey: string): Promise<void> {
    const url = `${this.baseURL}/favorites/${type}/`;
    const favorites = this.getFavorites(storageKey)
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: new Headers({
          'Content-Type': 'application/json',
        }),
        body: JSON.stringify({ favorites }),
      });

      if (!response.ok) {
        throw new Error(`Failed to send ${type} favorites to backend: ${response.statusText}`);
      }

      console.log(`Successfully sent ${type} favorites to backend`);
    } catch (error) {
      console.error(error);
    }
  }

async getFavoritesBackend(type: string, storageKey: string): Promise<any> {
  const favorites = this.getFavorites(storageKey);
  const queryString = favorites.map(id => `favorites=${id}`).join('&');
  const url = `${this.baseURL}/favorites/${type}/get/?${queryString}`;
  
  try {
    const response = await fetch(url, {
      method: 'GET',
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
    });
    if (!response.ok) {
      throw new Error(`Failed to fetch ${type} favorites: ${response.statusText}`);
    }
    const data = await response.json();
    return data.favorites;
  } catch (error) {
    console.error(`Error fetching ${type} favorites:`, error);
    return [];
  }
}

}
