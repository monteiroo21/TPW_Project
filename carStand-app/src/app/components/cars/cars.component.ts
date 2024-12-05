import { Component } from '@angular/core';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { Car } from '../../interfaces/car';

@Component({
  selector: 'app-cars',
  imports: [CardsAndMotosCardsComponent], // Falta o import do Car aqui!!!
  templateUrl: './cars.component.html',
  styleUrl: './cars.component.css'
})
export class CarsComponent {
  // cars: Car[]; // Array of cars
}
