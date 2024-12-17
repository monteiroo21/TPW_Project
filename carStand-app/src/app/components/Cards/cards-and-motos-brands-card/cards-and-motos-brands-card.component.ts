import { Component, Input } from '@angular/core';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-cards-and-motos-brands-card',
  templateUrl: './cards-and-motos-brands-card.component.html',
  styleUrls: ['./cards-and-motos-brands-card.component.css'],
})
export class CardsAndMotosBrandsCardComponent {
  @Input() item: any;
  @Input() type: string = '';
  baseURL = environment.apiBaseUrl;
  

  navigateToDetails(): void {
    const url = this.type === 'car'
      ? `/carsdetails/${this.type}/${this.item.id}`
      : `/motosdetails/${this.type}/${this.item.id}`;
    window.location.href = url;
  }
}
