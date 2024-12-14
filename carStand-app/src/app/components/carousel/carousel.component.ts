import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CarService } from '../../services/car.service';
import { Car } from '../../interfaces/car';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-carousel',
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './carousel.component.html',
  styleUrl: './carousel.component.css'
})
export class CarouselComponent {
  cars: Car[] = [];

  carService: CarService = inject(CarService);
  CarsImages = [
    { image: '../../../assets/bmwm3panorama.jpg', id: 4 },
    { image: '../../../assets/ferraripanorama.png', id: 18 },
    { image: '../../../assets/mercedespropanorama.jpg', id: 7 },
    { image: '../../../assets/lexuspanorama.png', id: 14 },
    { image: '../../../assets/astonpanorama.png', id: 17 },
  ];

  carsList = [
    4, 18, 7, 14, 17
  ]

  currentIndex = 0;

  prevSlide() {
    this.currentIndex =
      (this.currentIndex - 1 + this.CarsImages.length) % this.CarsImages.length;
  }

  nextSlide() {
    this.currentIndex = (this.currentIndex + 1) % this.CarsImages.length;
  }
}
