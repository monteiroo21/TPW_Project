import { Injectable } from '@angular/core';
import { Brand } from '../interfaces/brand';

@Injectable({
  providedIn: 'root'
})
export class BrandService {
  private baseURL = 'http://localhost:8000/api';

  constructor() { }

  async getBrands(): Promise<Brand[]> {
    const url = `${this.baseURL}/brands`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }

  async getBrand(id: number): Promise<Brand> {
    const url = `${this.baseURL}/brand?id=${id}`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }
}