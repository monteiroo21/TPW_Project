import { Injectable } from '@angular/core';
import { Car } from '../interfaces/car';

@Injectable({
  providedIn: 'root'
})
export class CarService {
  private baseURL = 'http://localhost:8000/api';

  constructor() { }

  async getCars(): Promise<Car[]> {
    const url = `${this.baseURL}/cars`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }

  async getCar(id: number): Promise<Car> {
    const url = `${this.baseURL}/car?id=${id}`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }

  // Depois implementar o resto dos métodos
}
