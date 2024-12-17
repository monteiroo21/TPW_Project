import { Injectable } from '@angular/core';
import { Car } from '../interfaces/car';
import { CarModel } from '../interfaces/model';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CarService {
  private baseURL: string = environment.apiBaseUrlApi;

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

  async getCarsNum(num: Number): Promise<Car[]> {
    const url = `${this.baseURL}/cars?num=${num}`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }

  async createCar(car: FormData): Promise<Car> {
    const url = `${this.baseURL}/cars/create`;
    const response = await fetch(url, {
      method: 'POST',
      body: car,
    });

    return await response.json();
  }

  async getModelsByType(vehicleType: string): Promise<CarModel[]> {
    const url = `${this.baseURL}/models/${vehicleType}/`;
    try {
      const response = await fetch(url);

      return await response.json();
    } catch (error) {
      console.error(error);
      return [];
    }
  }

  async deleteCar(id: number): Promise<void> {
    const url = `${this.baseURL}/cars/delete/${id}`;
    const response = await fetch(url, {
      method: 'DELETE',
    });
  
    if (!response.ok) {
      throw new Error('Failed to delete car');
    }
  }
  
  async updateCar(car: FormData): Promise<Car> {
    const url = `${this.baseURL}/cars/update`;
    console.log(car.values());
    const response = await fetch(url, {
      method: 'PUT',
      body: car,
    });
  
    return await response.json();
  }

}
