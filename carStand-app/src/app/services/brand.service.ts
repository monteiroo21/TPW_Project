import { Injectable } from '@angular/core';
import { Brand } from '../interfaces/brand';
import { Moto } from '../interfaces/moto';
import { Car } from '../interfaces/car';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BrandService {
  private baseURL: string = environment.apiBaseUrlApi;

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

  async getBrandVehicles(id: number): Promise<{brand: Brand; cars: Car[]; motos: Moto[]}> {
    const url = `${this.baseURL}/brands/${id}/vehicles`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }
}