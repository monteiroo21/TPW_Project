import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { ManagerTableComponent } from "../manager-table/manager-table.component";
import { AuthService } from '../../services/auth.service';
import { FormsModule } from '@angular/forms';
import { AuthData } from '../../interfaces/authData';
import { CarouselComponent } from "../carousel/carousel.component";
import { CarService } from '../../services/car.service';
import { MotoService } from '../../services/moto.service';
import { Car } from '../../interfaces/car';
import { Moto } from '../../interfaces/moto';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-home',
  imports: [CommonModule, ManagerTableComponent, FormsModule, CarouselComponent, CardsAndMotosCardsComponent, RouterLink],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  authService: AuthService = inject(AuthService);
  authState: AuthData | null = null;
  carService: CarService = inject(CarService);
  motoService: MotoService = inject(MotoService);

  cars: Car[] = [];
  motos: Moto[] = [];

  constructor() {
    this.authService.authState$.subscribe((state) => {
      this.authState = state;
    });

    this.carService.getCarsNum(4).then((cars: Car[]) => {
      this.cars = cars;
    });

    this.motoService.getMotosNum(4).then((motos: Moto[]) => {
      this.motos = motos;
    });
  }
}
