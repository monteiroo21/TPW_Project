import { Component } from '@angular/core';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { ProfileService } from '../../services/profile.service';
import { CommonModule } from '@angular/common';
import { CardsAndMotosBrandsCardComponent } from '../Cards/cards-and-motos-brands-card/cards-and-motos-brands-card.component';

@Component({
  selector: 'app-purchased-vehicles',
  imports: [CommonModule, GoBackComponent, CardsAndMotosBrandsCardComponent],
  templateUrl: './purchased-vehicles.component.html',
  styleUrl: './purchased-vehicles.component.css'
})
export class PurchasedVehiclesComponent {
  cars: any[] = [];
  motos: any[] = [];

  constructor(private profileService: ProfileService) {
  }

  ngOnInit(): void {
    this.profileService.getPurchasedVehicles().then(
      (data) => {
        this.cars = data.cars;
        this.motos = data.motos;
        console.log('Purchased vehicles loaded:', this.cars, this.motos);
      },
      (error) => {
        console.error('Error fetching purchased vehicles:', error);
      }
    );
  }
}
