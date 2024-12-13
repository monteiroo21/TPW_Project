import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-cards-and-motos-cards',
  imports: [CommonModule, FormsModule],
  templateUrl: './cards-and-motos-cards.component.html',
  styleUrl: './cards-and-motos-cards.component.css'
})
export class CardsAndMotosCardsComponent {
  @Input() car: any;
  urlImage: string = "http://localhost:8000";

  @Input() moto: any;
  urlImageMoto: string = "http://localhost:8000";
  
  navigateToDetails(type: string, id: number): void {
    if (type == "car")
      window.location.href = `/carsdetails/${type}/${id}`;
    else
      window.location.href = `/motosdetails/${type}/${id}`;
  }
}
