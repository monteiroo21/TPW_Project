import { Component, inject } from '@angular/core';
import { CarModelService } from '../../services/car-model.service';
import { ActivatedRoute, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { Brand } from '../../interfaces/brand';
import { BrandService } from '../../services/brand.service';
import { CarModel } from '../../interfaces/model';

@Component({
  selector: 'app-create-vehicle-model',
  imports: [CommonModule, FormsModule, GoBackComponent],
  templateUrl: './create-vehicle-model.component.html',
  styleUrl: './create-vehicle-model.component.css'
})
export class CreateVehicleModelComponent {
  vehicleType: string = 'cars';
  modelData: any = {
    brand: '',
    name: '',
    base_price: '',
    specifications: '',
    releaseYear: '',
  };
  brands: Brand[] = [];
  message: string = '';
  error: boolean = false;

  carModelService = inject(CarModelService);
  brandService = inject(BrandService);

  constructor(private route: ActivatedRoute, private router: Router) {
    this.vehicleType = this.route.snapshot.params['type'];
    this.loadModels();
  }

  async submitForm() {
    const vehicle_type = this.vehicleType === 'cars' ? 'Car' : 'Motorbike';

    const formData = new FormData();
    formData.append('brand', this.modelData.brand);
    formData.append('name', this.modelData.name);
    formData.append('base_price', this.modelData.base_price);
    formData.append('specifications', this.modelData.specifications);
    formData.append('releaseYear', this.modelData.releaseYear);
    formData.append('vehicle_type', vehicle_type);

    try {
      const result: CarModel = await this.carModelService.createCarModel(formData);
      console.log(result);
      if (this.vehicleType === 'cars') {
        this.router.navigate(['/vehiclecreate/cars']);
      } else {
        this.router.navigate(['/vehiclecreate/motorbikes']);
      }
    } catch (error) {
      this.message = 'Error creating model.'
      if(this.modelData.releaseYear<1990||this.modelData.releaseYear>2024)
      this.message = 'Year must be more than 1990 and not future.';
      this.error = true;
      console.error(error);
    }
  }
  async loadModels() {
    try {
      this.brands = await this.brandService.getBrands();
    } catch (error) {
      console.error('Error loading models:', error);
    }
  }
}













