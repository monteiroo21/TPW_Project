import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CarService } from '../../services/car.service';
import { MotoService } from '../../services/moto.service';
import { CarModel } from '../../interfaces/model';
import { Car } from '../../interfaces/car';
import { Moto } from '../../interfaces/moto';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-edit-vehicle',
  imports: [CommonModule, FormsModule],
  templateUrl: './edit-vehicle.component.html',
  styleUrl: './edit-vehicle.component.css'
})
export class EditVehicleComponent {
  vehicleType: string = 'cars';
  vehicleData: Car | Moto | any = {};
  models: CarModel[] = [];
  message: string = '';
  error: boolean = false;

  carService = inject(CarService);
  motoService = inject(MotoService);

  constructor(private route: ActivatedRoute, private router: Router) {
    this.vehicleType = this.route.snapshot.params['type'];
    this.loadVehicle();
    this.loadModels();
  }

  async loadVehicle() {
    const id = +this.route.snapshot.params['id'];
    try {
      if (this.vehicleType === 'cars') {
        this.vehicleData = await this.carService.getCar(id);
      } else {
        this.vehicleData = await this.motoService.getMoto(id);
      }
    } catch (error) {
      console.error('Error loading vehicle:', error);
    }
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
    try {
      if (this.vehicleType === 'cars') {
        await this.carService.updateCar(this.vehicleData as Car);
        this.message = 'Car updated successfully!';
      } else {
        await this.motoService.updateMoto(this.vehicleData as Moto);
        this.message = 'Moto updated successfully!';
      }
      this.error = false;
      this.router.navigate([`/${this.vehicleType}`]);
    } catch (error) {
      this.message = 'Error updating vehicle.';
      this.error = true;
      console.error(error);
    }
  }

  handleFileInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input?.files?.[0]) {
      this.vehicleData.image = input.files[0].name; // Save file name only
    }
  }
}