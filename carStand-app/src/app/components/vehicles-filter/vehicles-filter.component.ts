import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FilterCar, FilterMoto } from '../../interfaces/filter.interface';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-vehicles-filter',
  imports: [FormsModule, CommonModule],
  templateUrl: './vehicles-filter.component.html',
  styleUrl: './vehicles-filter.component.css'
})
export class VehiclesFilterComponent {
  @Input() type: 'cars' | 'motos' = 'cars';
  @Output() applyFilters = new EventEmitter<FilterCar | FilterMoto>();
  isModalOpen: boolean = false;

  carFilters: FilterCar = {
    isEletric: false,
    doors: '',
    condition: '',
    color: '',
    minPrice: 0,
    maxPrice: 0
  };

  motoFilters: FilterMoto = {
    condition: '',
    color: '',
    minPrice: 0,
    maxPrice: 0
  };

  onApplyFilters() {
    if (this.type === 'motos') {
      this.applyFilters.emit(this.motoFilters);
      console.log(this.motoFilters);
      this.closeModal();
    } else {
      this.applyFilters.emit(this.carFilters);
      console.log(this.carFilters);
      this.closeModal();
    }
  }

  get filters() {
    return this.type === 'cars' ? this.carFilters : this.motoFilters;
  }

  openModal() {
    this.isModalOpen = true;
  }

  closeModal() {
    this.isModalOpen = false;
  }

  clearFilters(): void {
    if (this.type === 'cars') {
      this.carFilters = {
        isEletric: false,
        doors: '',
        condition: '',
        color: '',
        minPrice: 0,
        maxPrice: 0
      };
    } else {
      this.motoFilters = {
        condition: '',
        color: '',
        minPrice: 0,
        maxPrice: 0
      };
    }
  }

}
