import { Component, inject } from '@angular/core';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Moto } from '../../interfaces/moto';
import { MotoService } from '../../services/moto.service';

@Component({
  selector: 'app-motor-bikes',
  imports: [CommonModule, CardsAndMotosCardsComponent, FormsModule],
  templateUrl: './motor-bikes.component.html',
  styleUrl: './motor-bikes.component.css'
})
export class MotorBikesComponent {
  motos: Moto[] = [];
  motoService: MotoService = inject(MotoService);

  constructor() {
    this.motoService.getMotos().then(motos => this.motos = motos);
  }
}
