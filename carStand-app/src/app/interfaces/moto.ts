import { CarModel } from "./model";

export interface Moto {
    id: number;
    model: CarModel;  // MotoModel ID
    year: number;
    new: boolean;
    kilometers: number;
    price: number;
    image?: string;
    interestedCustomers: number[];  // Customer ID
    purchaser?: number;  // Customer ID
    color: string;
}