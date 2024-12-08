import { Component, inject } from '@angular/core';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { Car } from '../../interfaces/car';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CarService } from '../../services/car.service';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
  selector: 'app-cars',
  imports: [CommonModule, CardsAndMotosCardsComponent, FormsModule, SearchBarComponent],
  templateUrl: './cars.component.html',
  styleUrl: './cars.component.css'
})
export class CarsComponent {
  cars: Car[] = [];
  carService: CarService = inject(CarService);

  constructor() {
    this.carService.getCars().then(cars => this.cars = cars);
  }
}
