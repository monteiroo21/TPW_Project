import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { Car } from '../../../interfaces/car';

@Component({
  selector: 'app-cards-and-motos-cards',
  imports: [CommonModule],
  templateUrl: './cards-and-motos-cards.component.html',
  styleUrl: './cards-and-motos-cards.component.css'
})
export class CardsAndMotosCardsComponent {
  @Input() car: any;
  urlImage: string = "http://localhost:8000";

  @Input() moto: any;
  urlImageMoto: string = "http://localhost:8000";
}
