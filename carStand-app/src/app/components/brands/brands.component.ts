import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Brand } from '../../interfaces/brand';
import { BrandService } from '../../services/brand.service';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
  selector: 'app-brands',
  standalone: true,
  imports: [CommonModule, FormsModule, SearchBarComponent],
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
