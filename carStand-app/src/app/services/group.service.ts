import { Injectable } from '@angular/core';
import { Group } from '../interfaces/group';

@Injectable({
    providedIn: 'root'
})
export class BrandServuce {
    private baseURL = 'http://localhost:8000/api';

    constructor() { }

    async getBrands(): Promise<Group[]> {
        const url = `${this.baseURL}/groups`;
        const data = await fetch(url);
        return await data.json() ?? [];
    }

    async getBrand(id: number): Promise<Group> {
        const url = `${this.baseURL}/groups/${id}`;
        const data = await fetch(url);
        return await data.json() ?? undefined;
    }
}