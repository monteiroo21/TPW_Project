import { Group } from "./group";
import { Car } from "./car";
import { Moto } from "./moto";

export interface Brand {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    cellPhone: string;
    group: Group;
    description: string;
    logo?: string;  // path to the logo
    cars?: Car[];
    motos?: Moto[];
}