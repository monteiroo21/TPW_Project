export interface Group {
    id: number;
    name: string;
    email: string;
    country: string;
    website: string;
    logo?: string;  // path to the logo
    headquartes?: string;   // path to the headquartes
}