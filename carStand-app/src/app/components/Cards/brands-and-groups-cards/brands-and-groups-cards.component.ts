import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-brands-and-groups-cards',
  imports: [CommonModule],
  templateUrl: './brands-and-groups-cards.component.html',
  styleUrl: './brands-and-groups-cards.component.css'
})
export class BrandsAndGroupsCardsComponent {
  @Input() group: any;
  urlImage: string = "http://localhost:8000";

  @Input() brand: any;
  urlImageBrand: string = "http://localhost:8000";
}
