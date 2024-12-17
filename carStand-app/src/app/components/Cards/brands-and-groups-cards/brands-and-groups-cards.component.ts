import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { environment } from '../../../environments/environment';
@Component({
  selector: 'app-brands-and-groups-cards',
  imports: [CommonModule],
  templateUrl: './brands-and-groups-cards.component.html',
  styleUrl: './brands-and-groups-cards.component.css'
})
export class BrandsAndGroupsCardsComponent {
  baseURL = environment.apiBaseUrl;
  @Input() group: any;
  @Input() brand: any;
}
