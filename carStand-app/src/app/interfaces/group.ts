export interface Group {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    logo?: string;  // path to the logo
    headquarters?: string;   // path to the headquarters
}