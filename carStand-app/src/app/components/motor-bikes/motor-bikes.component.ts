import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Moto } from '../../interfaces/moto';
import { MotoService } from '../../services/moto.service';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
  selector: 'app-motor-bikes',
  imports: [CommonModule, FormsModule, SearchBarComponent],
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
