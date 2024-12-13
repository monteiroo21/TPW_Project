export interface FilterCar {
    name: string;
    sort: string;
    isEletric: boolean;
    doors: string;
    condition: string;
    color: string;
    minPrice: number;
    maxPrice: number;
}

export interface FilterMoto {
    name: string;
    sort: string;
    condition: string;
    color: string;
    minPrice: number;
    maxPrice: number;
}