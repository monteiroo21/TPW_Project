import { Injectable } from '@angular/core';
import { Group } from '../interfaces/group';

@Injectable({
  providedIn: 'root'
})
export class GroupService {
  private baseURL = 'http://localhost:8000/api';

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
}