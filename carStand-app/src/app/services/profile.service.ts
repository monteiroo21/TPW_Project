import { Injectable } from "@angular/core";
import { Profile } from "../interfaces/profile";

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  private baseURL = 'http://localhost:8000/api';

  constructor() { }

  async getProfile(): Promise<Profile> {
    const url = `${this.baseURL}/profile/`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }

  async editProfile(profile: Profile): Promise<Profile> {
    const url = `${this.baseURL}/profile/`;
    console.log('Editing profile:', profile);
    const data = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(profile)
    });
    return await data.json() ?? undefined;
  }

}