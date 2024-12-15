import { Injectable } from "@angular/core";
import { Moto } from "../interfaces/moto";

@Injectable({
  providedIn: 'root'
})
export class MotoService {
  private baseURL = 'http://localhost:8000/api';

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

  async createMoto(moto: any): Promise<any> {
    const url = `${this.baseURL}/motos/create`;
    const response = await fetch(url, {
      method: 'POST',
      headers: new Headers({
        'Content-Type': 'application/json',
      }),
      body: JSON.stringify(moto),
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

  async updateMoto(moto: Moto): Promise<void> {
    const url = `${this.baseURL}/motos/update`;
    const response = await fetch(url, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(moto),
    });
  
    if (!response.ok) {
      throw new Error('Failed to update motorbike');
    }
  }
  
  // Depois implementar o resto dos métodos
}