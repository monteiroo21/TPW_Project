import { Component, inject, Input } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Car } from '../../../interfaces/car';
import { Moto } from '../../../interfaces/moto';
import { CarService } from '../../../services/car.service';
import { MotoService } from '../../../services/moto.service';
import { GoBackComponent } from '../../Buttons/go-back/go-back.component';

@Component({
  selector: 'app-cars-and-motos-details',
  imports: [CommonModule, FormsModule, GoBackComponent],
  templateUrl: './cars-and-motos-details.component.html',
  styleUrl: './cars-and-motos-details.component.css'
})
export class CarsAndMotosDetailsComponent {
  @Input() car: Car | undefined = undefined;
  @Input() moto: Moto | undefined = undefined;

  carService: CarService = inject(CarService);
  motoService: MotoService = inject(MotoService);

  urlImage: string = "http://localhost:8000";
  constructor(private route: ActivatedRoute, private location: Location) {
    let type: string = this.route.snapshot.params['type'];
    if (type == "car") {
      this.getCarDetails();
    }
    else {
      this.getMotoDetails();
    }
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
}
