import { CarModel } from "./model";

export interface Moto {
    id: number;
    model: CarModel;
    year: number;
    new: boolean;
    kilometers: number;
    price: number;
    image?: string;
    interestedCustomers: number[];
    purchaser?: number;
    color: string;
}