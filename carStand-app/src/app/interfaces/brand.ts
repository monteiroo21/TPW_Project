import { Group } from "./group";

export interface Brand {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    cellphone: string;
    group: Group;
    description: string;
    logo?: string;  // path to the logo
}