import { Component, inject } from '@angular/core';
import { BrandsAndGroupsCardsComponent } from '../Cards/brands-and-groups-cards/brands-and-groups-cards.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Brand } from '../../interfaces/brand';
import { BrandService } from '../../services/brand.service';

@Component({
  selector: 'app-brands',
  standalone: true,
  imports: [CommonModule, BrandsAndGroupsCardsComponent, FormsModule],
  templateUrl: './brands.component.html',
  styleUrls: ['./brands.component.css']
})
export class BrandsComponent {
  brands: Brand[] = [];
  brandService: BrandService = inject(BrandService);

  constructor() {
    this.brandService.getBrands().then(brands => {
      this.brands = brands;
      console.log(this.brands);
    });
  }
}
