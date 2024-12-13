import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FilterSortService {
  private baseURL = 'http://localhost:8000/api';

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

  async searchVehicles(type: string, query: string, sortOption: string = ''): Promise<any[]> {
    const url = new URL(`${this.baseURL}/search/${type}/`);
    if (query) {
      url.searchParams.append('q', query);
    }
    if (sortOption) {
      url.searchParams.append('sort', sortOption);
    }

    try {
      const response = await fetch(url.toString());
      return await response.json() ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos com termo:', error);
      return [];
    }
  }

  async filterVehicles(type: string, filters: any, sortOption: string = ''): Promise<any[]> {
    const url = new URL(`${this.baseURL}/${type}/filters`);
    let n = 0;

    Object.keys(filters).forEach(key => {
      if (key === 'name' && filters[key] !== '') {
        url.searchParams.append('q', filters[key]);
        n += 1;
      }

      if (filters[key]) {
        url.searchParams.append(key, filters[key]);
        n += 1;
      }
    });

    if (sortOption) {
      url.searchParams.append('sort', sortOption);
      n += 1;
    }

    try {
      if (n >= 0) {
        const response = await fetch(url.toString());
        return await response.json() ?? [];
      }
      const newURL = `${this.baseURL}/${type}`;
      const responseMain = await fetch(newURL.toString());
      return await responseMain.json() ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos com filtros:', error);
      return [];
    }
  }
}
