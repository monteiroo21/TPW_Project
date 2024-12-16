import { Component, inject } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CarService } from '../../services/car.service';
import { MotoService } from '../../services/moto.service';
import { CarModel } from '../../interfaces/model';
import { Car } from '../../interfaces/car';
import { Moto } from '../../interfaces/moto';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';

@Component({
  selector: 'app-edit-vehicle',
  standalone: true,
  imports: [CommonModule, FormsModule, GoBackComponent],
  templateUrl: './edit-vehicle.component.html',
  styleUrls: ['./edit-vehicle.component.css']
})
export class EditVehicleComponent {
  vehicleType: string = 'cars';
  vehicleData: Car | Moto | any = {};
  models: CarModel[] = [];
  message: string = '';
  modelID: number|string='';
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
      const formData = new FormData();

      Object.keys(this.vehicleData).forEach((key) => {
        if (key === 'image' && this.vehicleData[key] instanceof File) {
          formData.append(key, this.vehicleData[key]);
        } else if (key === 'model') {
          console.log(key, this.modelID);
          
          formData.append(key,this.modelID!='' ? this.modelID.toString() : this.vehicleData[key].id);
        } else {
          formData.append(key, this.vehicleData[key] !== undefined ? this.vehicleData[key] : '');
        }
      });

      console.log('FormData keys:', Array.from(formData.keys()));

      if (this.vehicleType === 'cars') {
        await this.carService.updateCar(formData); // Envia formData sem headers manual
        this.message = 'Car updated successfully!';
        this.router.navigate([`/carsdetails/car/${this.vehicleData.id}`]);

      } else {
        await this.motoService.updateMoto(formData); // Envia formData sem headers manual
        this.message = 'Moto updated successfully!';
        this.router.navigate([`/motosdetails/moto/${this.vehicleData.id}`]);
      }
      this.error = false;
    } catch (error) {
      this.message = 'Error updating vehicle.';
      this.error = true;
      console.error(error);
    }
  }

  handleFileInput(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input?.files?.[0]) {
      this.vehicleData.image = input.files[0]; // Agora armazena o próprio arquivo
    }
  }
}
