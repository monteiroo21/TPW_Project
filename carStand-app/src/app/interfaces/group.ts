import { Brand } from "./brand";

export interface Group {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    logo?: string;
    headquarters?: string;
    brands?: Brand[];
}