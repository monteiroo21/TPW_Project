import { Component, inject } from '@angular/core';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { CommonModule } from '@angular/common';
import { FavoriteService } from '../../services/favorite.service';
import { CardsAndMotosBrandsCardComponent } from '../Cards/cards-and-motos-brands-card/cards-and-motos-brands-card.component';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-favourites',
  imports: [CommonModule, GoBackComponent, CardsAndMotosBrandsCardComponent],
  templateUrl: './favourites.component.html',
  styleUrl: './favourites.component.css'
})
export class FavouritesComponent {
  cars: any[] = [];
  motos: any[] = [];
  
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