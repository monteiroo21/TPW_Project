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
  @Input() cars: Car[] = [];
}
