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
      this.modelID = this.vehicleData.model.id;
    } catch (error) {
      console.error('Error loading vehicle:', error);
    }
  }

  async loadModels() {
    const id = +this.route.snapshot.params['id'];
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
      let result : any;
      if (this.vehicleType === 'cars') {
        result = await this.carService.updateCar(formData);
      } else {
        result = await this.motoService.updateMoto(formData);
      }
      console.log(result)
      if ('error' in result && result.error) {
        this.message = <string>result.error; 
        this.error = true;
        console.error('Server error:', result.error);
      } else {
        this.router.navigate([`/${this.vehicleType === 'cars' ? 'carsdetails/car' : 'motosdetails/moto'}/${this.vehicleData.id}`]);

      }

    } catch (error) {
      this.message = 'Error updating vehicle.';
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
