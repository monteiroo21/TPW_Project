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

}