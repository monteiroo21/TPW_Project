export interface FilterCar {
    isEletric: boolean;
    doors: string;
    condition: string;
    color: string;
    minPrice: number;
    maxPrice: number;
}

export interface FilterMoto {
    condition: string;
    color: string;
    minPrice: number;
    maxPrice: number;
}