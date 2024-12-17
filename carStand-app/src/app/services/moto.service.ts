import { Injectable } from "@angular/core";
import { Moto } from "../interfaces/moto";
import { environment } from "../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class MotoService {
  private baseURL: string = environment.apiBaseUrlApi;

  constructor() { }

  async getMotos(): Promise<Moto[]> {
    const url = `${this.baseURL}/motos`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }

  async getMoto(id: number): Promise<Moto> {
    const url = `${this.baseURL}/moto?id=${id}`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }

  async getMotosNum(num: Number): Promise<Moto[]> {
    const url = `${this.baseURL}/motos?num=${num}`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }

  async createMoto(moto: any): Promise<Moto> {
    const url = `${this.baseURL}/motos/create`;
    const response = await fetch(url, {
      method: 'POST',
      body: moto,
    });
    console.log(response.status);
    
    return await response.json();
  }

  async deleteMoto(id: number): Promise<void> {
    const url = `${this.baseURL}/motos/delete/${id}`;
    const response = await fetch(url, {
      method: 'DELETE',
    });
  
    if (!response.ok) {
      throw new Error('Failed to delete motorbike');
    }
  }

  async updateMoto(moto: FormData): Promise<Moto> {
    const url = `${this.baseURL}/motos/update`;
    const response = await fetch(url, {
      method: 'PUT',
      body: moto,
    });
  
    console.log(response.status);
    return await response.json();
  }
  
}