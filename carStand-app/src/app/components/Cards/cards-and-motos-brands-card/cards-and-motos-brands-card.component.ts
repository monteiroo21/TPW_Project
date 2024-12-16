import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-cards-and-motos-brands-card',
  templateUrl: './cards-and-motos-brands-card.component.html',
  styleUrls: ['./cards-and-motos-brands-card.component.css'],
})
export class CardsAndMotosBrandsCardComponent {
  @Input() item: any;
  @Input() type: string = '';
  urlImage: string = 'http://localhost:8000';

  navigateToDetails(): void {
    const url = this.type === 'car'
      ? `/carsdetails/${this.type}/${this.item.id}`
      : `/motosdetails/${this.type}/${this.item.id}`;
    window.location.href = url;
  }
}
