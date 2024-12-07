import { Component, inject } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Car } from '../../../interfaces/car';
import { Moto } from '../../../interfaces/moto';
import { CarService } from '../../../services/car.service';
import { MotoService } from '../../../services/moto.service';

@Component({
  selector: 'app-cars-and-motos-details',
  imports: [],
  templateUrl: './cars-and-motos-details.component.html',
  styleUrl: './cars-and-motos-details.component.css'
})
export class CarsAndMotosDetailsComponent {
  car: Car | undefined = undefined;
  moto: Moto | undefined = undefined;

  carService: CarService = inject(CarService);
  motoService: MotoService = inject(MotoService);

  constructor(private route: ActivatedRoute, private location: Location) {
    this.getCarDetails();
    this.getMotoDetails();
  }

  getCarDetails(): void {
    let num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    num = +num;
    this.carService.getCar(num).then((car: Car) => { this.car = car; });
  }

  getMotoDetails(): void {
    let num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    num = +num;
    this.motoService.getMoto(num).then((moto: Moto) => { this.moto = moto; });
  }

  goBack(): void {
    this.location.back();
  }
}
