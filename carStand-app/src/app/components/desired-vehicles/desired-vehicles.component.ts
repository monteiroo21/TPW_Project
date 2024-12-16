import { Component } from '@angular/core';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { Car } from '../../interfaces/car';
import { Moto } from '../../interfaces/moto';
import { ProfileService } from '../../services/profile.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-desired-vehicles',
  imports: [CommonModule, GoBackComponent],
  templateUrl: './desired-vehicles.component.html',
  styleUrl: './desired-vehicles.component.css'
})
export class DesiredVehiclesComponent {
  cars: any[] = [];
  motos: any[] = [];
  urlImage: string = "http://localhost:8000";

  constructor(private profileService: ProfileService) {
  }

  ngOnInit(): void {
    this.profileService.getDesiredVehicles().then(
      (data) => {
        this.cars = data.cars;
        this.motos = data.motos;
        console.log('Desired vehicles loaded:', this.cars, this.motos);
      },
      (error) => {
        console.error('Error fetching desired vehicles:', error);
      }
    );
  }

}
