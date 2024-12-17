import { Injectable } from '@angular/core';
import { ElementForAccept } from '../interfaces/elementForAccept';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PurchaserAndSelectedVehiclesService {
  private baseURL: string = environment.apiBaseUrlApi;

  constructor() { }

  async toggleInterest(vehicleId: number, type: string): Promise<any> {
    const url = `${this.baseURL}/vehicles/${vehicleId}/${type}/interest/`;
    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: new Headers({
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        }),
      });

      return await response.json();
    } catch (error) {
      console.error(error);
    }
  }
  async approveCustomer(vehicleId: number, profile_id: number, type: string): Promise<any> {
    const url = `${this.baseURL}/vehicles/${vehicleId}/${profile_id}/${type}/approve/`;
    try {
      const response = await fetch(url, { method: 'POST' });

      return await response.json();
    } catch (error) {
      console.error(error);
    }
  }

  async negateCustomer(vehicleId: number, profile_id: number, type: string): Promise<any> {
    const url = `${this.baseURL}/vehicles/${vehicleId}/${profile_id}/${type}/negate/`;
    try {
      const response = await fetch(url, { method: 'POST' });

      return await response.json();
    } catch (error) {
      console.error(error);
    }
  }
  async getVehicleStatus(vehicleId: number, type: string): Promise<{ isSelected: boolean; isBuyed: boolean | null }> {
    const url = `${this.baseURL}/vehicles/${vehicleId}/${type}/status/`;

    try {
      const response = await fetch(url);

      return await response.json();
    } catch (error) {
      console.error(error);
      return { isSelected: false, isBuyed: null };
    }
  }
  async getVehiclesForApproval(queryVehicle: string = '', queryUser: string = ''): Promise<{ listForAccept: ElementForAccept[] }> {
    const url = new URL(`${this.baseURL}/vehicles/approval/`);

    if (queryVehicle) url.searchParams.append('qVehicle', queryVehicle);
    if (queryUser) url.searchParams.append('qUser', queryUser);

    try {
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`Failed to fetch vehicles for approval: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error(error);
      return { listForAccept: [] };
    }
  }

}