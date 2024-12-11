import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private baseUrl: string = 'http://localhost:8000/api/';

  constructor() {}

  async signUp(userData: { username: string, email: string, first_name: string, last_name: string, password: string }): Promise<any> {
    const url = `${this.baseUrl}signup`;
    const response = await fetch(url, {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
      body: JSON.stringify(userData),
    });

    return await response.json();
  }

  async login(username: string, password: string): Promise<any> {
    const url = `${this.baseUrl}login`;
    const response = await fetch(url, {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
      body: JSON.stringify({ username, password }),
    });

    return await response.json();
  }

  async logout(): Promise<any> {
    const url = `${this.baseUrl}logout`;
    const response = await fetch(url, {
      method: "POST",
      headers: new Headers({
        "Content-Type": "application/json",
      }),
    });

    return await response.json();
  }

  //Implentar depois o edit_profile
}
