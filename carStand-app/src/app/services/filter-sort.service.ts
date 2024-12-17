import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FilterSortService {
  private baseURL: string = environment.apiBaseUrlApi;

  constructor() { }

  async getVehiclesByType(type: string, sortOption: string = ''): Promise<any[]> {
    const url = new URL(`${this.baseURL}/${type}`);
    if (sortOption) {
      url.searchParams.append('sort', sortOption);
    }

    try {
      const response = await fetch(url.toString());
      return await response.json() ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos:', error);
      return [];
    }
  }

  async getVehicles(type: string, options: { query?: string; filters?: any; sortOption?: string } = {}): Promise<any[]> {
    const url = new URL(`${this.baseURL}/search/${type}/`);
    const { query, filters, sortOption } = options;

    if (query) {
      url.searchParams.append('q', query);
    }

    if (filters) {
      Object.keys(filters).forEach(key => {
        if (filters[key]) {
          url.searchParams.append(key, filters[key]);
        }
      });
    }

    if (sortOption) {
      url.searchParams.append('sort', sortOption);
    }

    try {
      const response = await fetch(url.toString());
      
      return await response.json() ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos:', error);
      return [];
    }
  }
}
