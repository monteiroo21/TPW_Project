import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-cards-and-motos-cards',
  imports: [CommonModule, FormsModule],
  templateUrl: './cards-and-motos-cards.component.html',
  styleUrl: './cards-and-motos-cards.component.css'
})
export class CardsAndMotosCardsComponent {
  baseURL = environment.apiBaseUrl;
  @Input() car: any;
  @Input() moto: any;
  
  navigateToDetails(type: string, id: number): void {
    if (type == "car")
      window.location.href = `/carsdetails/${type}/${id}`;
    else
      window.location.href = `/motosdetails/${type}/${id}`;
  }
}
