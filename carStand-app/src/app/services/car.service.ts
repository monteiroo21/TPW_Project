import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class CarService {
    private baseURL = 'http://localhost:8000/api/cars/';

    constructor(private http: HttpClient) { }

    getCars(): Observable<any> {
        return this.http.get(this.baseURL);
    }

    getCar(id: number): Observable<any> {
        return this.http.get(`${this.baseURL}${id}/`);
    }

    createCar(car: any): Observable<any> {
        return this.http.post(`${this.baseURL}create/`, car);
    }

    updateCar(id: number, car: any): Observable<any> {
        return this.http.put(`${this.baseURL}update/${id}/`, car);
    }

    deleteCar(id: number): Observable<any> {
        return this.http.delete(`${this.baseURL}delete/${id}/`);
    }
}
