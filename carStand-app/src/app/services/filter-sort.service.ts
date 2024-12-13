import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FilterSortService {
  private baseURL = 'http://localhost:8000/api';

  constructor() { }

  async getVehiclesByType(type: string): Promise<any[]> {
    const url = `${this.baseURL}/${type}`;
    try {
      const response = await fetch(url);
      return await response.json() ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos:', error);
      return [];
    }
  }

  // Método para realizar busca por termo
  async searchVehicles(type: string, query: string): Promise<any[]> {
    const url = `${this.baseURL}/search/${type}/?q=${query}`;
    try {
      const response = await fetch(url);
      return await response.json() ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos com termo:', error);
      return [];
    }
  }

  // Método para buscar veículos com filtros
  async filterVehicles(type: string, filters: any): Promise<any[]> {
    const url = new URL(`${this.baseURL}/${type}/filters`);
    let n = 0;
    Object.keys(filters).forEach(key => {
      if (key == "name" && filters[key] != "") {
        url.searchParams.append("q", filters[key]);
        n += 1;
      }

      if (filters[key]) {
        url.searchParams.append(key, filters[key]);
        n += 1;
      }
    });

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
