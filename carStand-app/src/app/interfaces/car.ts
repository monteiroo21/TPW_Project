import { CarModel } from "./model";

export interface Car {
    id: number;
    model: CarModel;  // CarModel ID
    year: number;
    new: boolean;
    kilometers: number;
    price: number;
    image?: string;
    interestedCustomers: number[];  // Customer ID
    purchaser?: number;  // Customer ID
    color: string;
    doors: number;
    electric: boolean;
}