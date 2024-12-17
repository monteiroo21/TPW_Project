import { Injectable } from '@angular/core';
import { CarModel } from '../interfaces/model';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CarModelService {
  private baseURL: string = environment.apiBaseUrlApi;

  constructor() { }

  async createCarModel(modelData: FormData): Promise<CarModel> {
    const url = `${this.baseURL}/carmodel/create`;
    const response = await fetch(url, {
      method: 'POST',
      body: modelData,
    });

    if (!response.ok) {
      throw new Error('Failed to create CarModel');
    }

    return await response.json();
  }
}
