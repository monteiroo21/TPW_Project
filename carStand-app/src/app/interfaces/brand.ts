export interface Brand {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    cellphone: string;
    group: number;
    description: string;
    logo?: string;  // path to the logo
}