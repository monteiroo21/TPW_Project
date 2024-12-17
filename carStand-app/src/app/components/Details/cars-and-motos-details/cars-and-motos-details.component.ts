import { Component, inject, Input } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { Car } from '../../../interfaces/car';
import { Moto } from '../../../interfaces/moto';
import { CarService } from '../../../services/car.service';
import { AuthService } from '../../../services/auth.service';
import { MotoService } from '../../../services/moto.service';
import { GoBackComponent } from '../../Buttons/go-back/go-back.component';
import { AuthData } from '../../../interfaces/authData';
import { FavoriteService } from '../../../services/favorite.service';
import { PurchaserAndSelectedVehiclesService } from '../../../services/purchaser-and-selected-vehicles.service';
import { CardsAndMotosCardsComponent } from '../../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-cars-and-motos-details',
  imports: [CommonModule, FormsModule, GoBackComponent, CardsAndMotosCardsComponent, RouterLink],
  templateUrl: './cars-and-motos-details.component.html',
  styleUrl: './cars-and-motos-details.component.css'
})
export class CarsAndMotosDetailsComponent {

  @Input() car: Car | undefined = undefined;
  @Input() moto: Moto | undefined = undefined;
  cars: Car[] = [];
  motos: Moto[] = [];

  carService: CarService = inject(CarService);
  motoService: MotoService = inject(MotoService);
  authService: AuthService = inject(AuthService);
  favoriteService: FavoriteService = inject(FavoriteService);
  purchaserService: PurchaserAndSelectedVehiclesService = inject(PurchaserAndSelectedVehiclesService);

  authState: AuthData | null = null;
  isSelected: boolean = false;
  isBuyed: boolean | null = null;
  baseURL = environment.apiBaseUrl;
  constructor(private route: ActivatedRoute, private location: Location, private router: Router) {
    this.authService.authState$.subscribe((state) => {
      this.authState = state;
    });
    this.authService.authState$.subscribe((state) => {
      this.authState = state;
    });
    let type: string = this.route.snapshot.params['type'];
    if (type == 'car') {
      this.getCarDetails();
      this.carService.getCarsNum(4).then((cars: Car[]) => { this.cars = cars; });
      this.carService.getCarsNum(4).then((cars: Car[]) => { this.cars = cars; });
    }
    else {
      this.getMotoDetails();
      this.motoService.getMotosNum(4).then((motos: Moto[]) => { this.motos = motos; });
      this.motoService.getMotosNum(4).then((motos: Moto[]) => { this.motos = motos; });
    }
  }

  getCarDetails(): void {
    let num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    num = +num;
    this.carService.getCar(num).then((car: Car) => { this.car = car; });
    this.checkVehicleStatus('car');

  }

  getMotoDetails(): void {
    let num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    num = +num;
    this.motoService.getMoto(num).then((moto: Moto) => { this.moto = moto; });
    this.checkVehicleStatus('moto');

  }

  isFavorite(): boolean {
    if (this.car || this.moto) {
      const id = this.car ? this.car.id : this.moto?.id;
      const typeList = this.car ? 'favoriteCarList' : 'favoriteMotoList';

      return id ? this.favoriteService.isFavorite(typeList, id) : false;
    }
    return false;
  }

  toggleFavorite(): void {
    if (this.car || this.moto) {
      const id = this.car ? this.car.id : this.moto?.id;
      const type = this.car ? 'favoriteCarList' : 'favoriteMotoList';

      if (id) {
        const isFavorite = this.favoriteService.toggleFavorite(type, id);

        if (isFavorite) {
          console.log(`${type === 'favoriteCarList' ? 'Car' : 'Moto'} ${id} added to favorites.`);
        } else {
          console.log(`${type === 'favoriteCarList' ? 'Car' : 'Moto'} ${id} removed from favorites.`);
        }
      }
    }
  }
  async checkVehicleStatus(type: string): Promise<void> {
    const num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    const id = +num;
    console.log(id);

    if (id) {
      const status = await this.purchaserService.getVehicleStatus(id, type);
      this.isSelected = status.isSelected;
      this.isBuyed = status.isBuyed;

    }
  }

  async toggleInterest(): Promise<void> {
    const id = this.car ? this.car.id : this.moto?.id;
    const type = this.car ? 'car' : 'moto';

    if (id) {
      await this.purchaserService.toggleInterest(id, type);
      this.checkVehicleStatus(type)
    }
  }

  async deleteVehicle(): Promise<void> {
    const num: any = this.route.snapshot.params['num'];
    if (num == null) return;
  
    const id = +num;
    const type = this.car ? 'car' : 'moto';
    
    if (type === 'car') {
      try {
        await this.carService.deleteCar(id);
        this.router.navigate(['/cars']);
      } catch (error) {
        console.error('Error deleting car:', error);
      }
    } else {
      try {
        await this.motoService.deleteMoto(id);
        this.router.navigate(['/motorbikes']);
      } catch (error) {
        console.error('Error deleting motorbike:', error);
      }
    }
  }
  

}
