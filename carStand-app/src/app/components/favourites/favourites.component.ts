import { Component } from '@angular/core';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { Car } from '../../interfaces/car';
import { Moto } from '../../interfaces/moto';
import { ProfileService } from '../../services/profile.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-favourites',
  imports: [CommonModule, GoBackComponent],
  templateUrl: './favourites.component.html',
  styleUrl: './favourites.component.css'
})
export class FavouritesComponent {
  cars: any[] = [];
  motos: any[] = [];
  urlImage: string = "http://localhost:8000";

  constructor(private profileService: ProfileService) {
  }

  ngOnInit(): void {
    this.profileService.getFavourites().then(
      (data) => {
        this.cars = data.cars;
        this.motos = data.motos;
        console.log('Favourites loaded:', this.cars, this.motos);
      },
      (error) => {
        console.error('Error fetching favourites:', error);
      }
    );
  }

}
