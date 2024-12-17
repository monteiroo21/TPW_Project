import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { CarService } from '../../services/car.service';
import { MotoService } from '../../services/moto.service';
import { CarModel } from '../../interfaces/model';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';

@Component({
  selector: 'app-create-vehicle',
  imports: [CommonModule, FormsModule, GoBackComponent, RouterLink],
  templateUrl: './create-vehicle.component.html',
  styleUrl: './create-vehicle.component.css',
})
export class CreateVehicleComponent {
  vehicleType: string = 'cars';
  vehicleData: any = {
    model: "",
    year: "",
    kilometers: "",
    price: "",
    color: '',
    doors: "",
    electric: false,
    image: '',
    interestedCustomers: [],
    purchaser: null,
  };
  models: CarModel[] = [];
  message: string = '';
  error: boolean = false;

  carService = inject(CarService);
  motoService = inject(MotoService);

  constructor(private route: ActivatedRoute, private router: Router) {
    this.vehicleType = this.route.snapshot.params['type'];
    this.loadModels();
  }

  async loadModels() {
    try {
      this.models = await this.carService.getModelsByType(
        this.vehicleType === 'cars' ? 'Car' : 'Motorbike'
      );
    } catch (error) {
      console.error('Error loading models:', error);
    }
  }

  async submitForm() {
    const requiredFields = ['model', 'year', 'price', 'color', 'image'];
    if (this.vehicleType === 'cars') {
      requiredFields.push('doors');
    }
    const missingFields = requiredFields.filter(
      (field) => !this.vehicleData[field]
    );

    if (missingFields.length > 0) {
      this.message = `Please fill in all required fields: ${missingFields.join(', ')}`;
      this.error = true;
      console.error('Missing fields:', missingFields);
      return;
    }

    const formData = new FormData();
    Object.keys(this.vehicleData).forEach((key) => {
      formData.append(key, this.vehicleData[key]);
    });

    try {
      let result;
      if (this.vehicleType === 'cars') {
        result = await this.carService.createCar(formData);
      } else {
        result = await this.motoService.createMoto(formData);
      }

      if ('error' in result && result.error) {
        this.message = <string>result.error; 
        this.error = true;
        console.error('Server error:', result.error);
      } else {
        this.message = `${this.vehicleType === 'cars' ? 'Car' : 'Motorbike'} created successfully!`;
        this.error = false;
        this.router.navigate([`/${this.vehicleType === 'cars' ? 'cars' : 'motorbikes'}`]);
      }
    } catch (error) {
      this.message = 'Error creating vehicle.';
      this.error = true;
      console.error('Error:', error);
    }
  }


  handleFileInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input?.files?.[0]) {
      this.vehicleData.image = input.files[0];
    }
  }
}
