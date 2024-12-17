import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-search-bar-table',
  imports: [CommonModule, FormsModule],
  templateUrl: './search-bar-table.component.html',
  styleUrl: './search-bar-table.component.css'
})
export class SearchBarTableComponent {
  queryVehicle: string = '';
  queryUser: string = '';

  @Output() searchFilters = new EventEmitter<{ queryVehicle: string; queryUser: string }>();

  emitFilters(): void {
    this.searchFilters.emit({
      queryVehicle: this.queryVehicle,
      queryUser: this.queryUser
    });
  }
}
