import { Injectable } from '@angular/core';
import { Group } from '../interfaces/group';
import { Brand } from '../interfaces/brand';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class GroupService {
  private baseURL: string = environment.apiBaseUrlApi;

  constructor() { }

  async getGroups(): Promise<Group[]> {
    const url = `${this.baseURL}/groups`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }

  async getGroup(id: number): Promise<Group> {
    const url = `${this.baseURL}/group?id=${id}`;
    const data = await fetch(url);
    return await data.json() ?? undefined;
  }

  async getBrandsByGroup(id: number): Promise<Brand[]> {
    const url = `${this.baseURL}/groups/${id}/brands`;
    const data = await fetch(url);
    return await data.json() ?? [];
  }
}