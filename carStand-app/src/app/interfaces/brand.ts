import { Group } from "./group";
import { Car } from "./car";
import { Moto } from "./moto";
import { CarModel } from "./model";

export interface Brand {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    cellPhone: string;
    group: Group;
    description: string;
    logo?: string;
    models?: Car[] | Moto[] | CarModel[];
    cars?: Car[];
    motos?: Moto[];
}