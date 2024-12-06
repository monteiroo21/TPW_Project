import { Component } from '@angular/core';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { Car } from '../../interfaces/car';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cars',
  imports: [CommonModule, CardsAndMotosCardsComponent, FormsModule], // Falta o import do Car aqui!!!
  templateUrl: './cars.component.html',
  styleUrl: './cars.component.css'
})
export class CarsComponent {
  // cars: Car[]; // Array of cars
}
