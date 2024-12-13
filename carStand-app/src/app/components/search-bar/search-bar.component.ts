import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Component, Input } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { BrandsAndGroupsCardsComponent } from '../Cards/brands-and-groups-cards/brands-and-groups-cards.component';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { VehiclesFilterComponent } from '../vehicles-filter/vehicles-filter.component';
import { FilterCar, FilterMoto } from '../../interfaces/filter.interface';
import { FilterSortService } from '../../services/filter-sort.service';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [CommonModule, FormsModule, BrandsAndGroupsCardsComponent, CardsAndMotosCardsComponent, HttpClientModule, VehiclesFilterComponent],
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  @Input() type!: string;
  searchQuery: string = '';
  results: any[] = [];
  filters: FilterCar | FilterMoto | undefined = undefined;
  filtersApplied: boolean = false;
  sortOption: string = '';

  constructor(private filterSortService: FilterSortService) { }

  async onSearch() {
    this.filtersApplied = false;
    if (this.searchQuery.trim()) {
      this.results = await this.filterSortService.searchVehicles(this.type, this.searchQuery, this.sortOption);
    } else {
      await this.ngOnInit();
    }
  }

  async onFiltersApplied(filters: FilterCar | FilterMoto) {
    this.filtersApplied = true;
    filters = { ...filters, name: this.searchQuery };
    this.results = await this.filterSortService.filterVehicles(this.type, filters, this.sortOption);
  }

  async onSortChanged() {
    if (this.filtersApplied) {
      await this.onFiltersApplied(this.filters!);
    } else {
      await this.onSearch();
    }
  }

  async ngOnInit() {
    this.results = await this.filterSortService.getVehiclesByType(this.type);
  }
}
