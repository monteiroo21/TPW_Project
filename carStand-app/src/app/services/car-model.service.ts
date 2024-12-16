import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CarModelService {
  private baseURL = 'http://localhost:8000/api';

  constructor() { }

  async createCarModel(modelData: FormData): Promise<any> {
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
