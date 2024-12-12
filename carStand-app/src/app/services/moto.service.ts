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

  // Depois implementar o resto dos métodos
}