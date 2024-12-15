import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Component, Input } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { BrandsAndGroupsCardsComponent } from '../Cards/brands-and-groups-cards/brands-and-groups-cards.component';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';
import { VehiclesFilterComponent } from '../vehicles-filter/vehicles-filter.component';
import { FilterCar, FilterMoto } from '../../interfaces/filter.interface';
import { FilterSortService } from '../../services/filter-sort.service';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [CommonModule, FormsModule, BrandsAndGroupsCardsComponent, CardsAndMotosCardsComponent, VehiclesFilterComponent,RouterLink],
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  @Input() type!: string;
  searchQuery: string = '';
  results: any[] = [];
  filters: FilterCar | FilterMoto | undefined = undefined;
  sortOption: string = '';

  constructor(private filterSortService: FilterSortService) { }

  async onSearch() {
    if (this.searchQuery || this.filters || this.sortOption ) {
      if (this.filters) {
        this.results = await this.filterSortService.getVehicles(this.type, {
          query: this.searchQuery,
          filters: this.filters,
          sortOption: this.sortOption,
        });
      }else{
        this.results = await this.filterSortService.getVehicles(this.type, {
          query: this.searchQuery,
          sortOption: this.sortOption,
        });
      }
    }else{
      this.results = await this.filterSortService.getVehiclesByType(this.type);
    }

   
  }

  async onFiltersApplied(filters: FilterCar | FilterMoto) {
    this.filters = { ...filters };
    await this.onSearch();
  }

  async onSortChanged() {
    await this.onSearch();
  }

  async ngOnInit() {
    this.results = await this.filterSortService.getVehiclesByType(this.type);
  }
}
