import { Component, inject } from '@angular/core';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { Car } from '../../interfaces/car';
import { Moto } from '../../interfaces/moto';
import { ProfileService } from '../../services/profile.service';
import { CommonModule } from '@angular/common';
import { FavoriteService } from '../../services/favorite.service';

@Component({
  selector: 'app-favourites',
  imports: [CommonModule, GoBackComponent],
  templateUrl: './favourites.component.html',
  styleUrl: './favourites.component.css'
})
export class FavouritesComponent  {
  cars: any[] = [];
  motos: any[] = [];
  urlImage: string = "http://localhost:8000";
  errorMessage: string = "";
  favoriteService: FavoriteService = inject(FavoriteService);
  constructor() {
  }

  async ngOnInit(): Promise<void> {
    try {
      this.cars = await this.favoriteService.getFavoritesBackend('cars', 'favoriteCarList');
      console.log('Favorite cars loaded:', this.cars);
      this.motos = await this.favoriteService.getFavoritesBackend('motos', 'favoriteMotoList');
      console.log('Favorite motos loaded:', this.motos);
    } catch (error) {
      this.errorMessage = 'Failed to load favorites. Please try again.';
      console.error(this.errorMessage, error);
    }
  }
}