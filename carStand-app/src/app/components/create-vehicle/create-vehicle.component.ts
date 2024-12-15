import { Component, inject } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
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
    interestedCustomers:[],
    purchaser:null,
  };
  models: CarModel[] = [];
  message: string = '';
  error: boolean = false;

  carService = inject(CarService);
  motoService = inject(MotoService);

  constructor(private route: ActivatedRoute) {
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
    const formData = new FormData();
    Object.keys(this.vehicleData).forEach((key) => {
      formData.append(key, this.vehicleData[key]);
    });
    console.log(this.vehicleData);
    try {
      if (this.vehicleType === 'cars') {
        await this.carService.createCar(formData);
        this.message = 'Car created successfully!';
      } else {
        await this.motoService.createMoto(formData);
        this.message = 'Moto created successfully!';
      }
      this.error = false;
    } catch (error) {
      this.message = 'Error creating vehicle.';
      this.error = true;
      console.error(error);
    }
  }

  handleFileInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input?.files?.[0]) {
      this.vehicleData.image = input.files[0];
    }
  }
}
