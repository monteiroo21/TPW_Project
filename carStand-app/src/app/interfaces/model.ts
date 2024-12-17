import { Brand } from "./brand";

export interface CarModel {
    id: number;
    brand: Brand;
    name: string;
    base_price: number;
    specifications: string;
    releaseYear: number;
    vehicle_type: string;
}
