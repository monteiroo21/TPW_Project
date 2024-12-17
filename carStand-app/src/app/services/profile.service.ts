import { Injectable } from "@angular/core";
import { Profile } from "../interfaces/profile";
import { Car } from "../interfaces/car";
import { Moto } from "../interfaces/moto";
import { environment } from "../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  private baseURL: string = environment.apiBaseUrlApi;

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

  async getPurchasedVehicles(): Promise<{ cars: Car[], motos: Moto[] }> {
    const url = `${this.baseURL}/profile/purchased/`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }

  async getDesiredVehicles(): Promise<{ cars: Car[], motos: Moto[] }> {
    const url = `${this.baseURL}/profile/desired/`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }


}