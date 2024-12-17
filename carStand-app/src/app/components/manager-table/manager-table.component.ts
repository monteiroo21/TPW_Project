import { Component } from '@angular/core';
import { PurchaserAndSelectedVehiclesService } from '../../services/purchaser-and-selected-vehicles.service';
import { CommonModule } from '@angular/common';
import { ElementForAccept } from '../../interfaces/elementForAccept';
import { SearchBarTableComponent } from '../search-bar-table/search-bar-table.component';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-manager-table',
  imports: [CommonModule, FormsModule, SearchBarTableComponent],
  templateUrl: './manager-table.component.html',
  styleUrl: './manager-table.component.css'
})
export class ManagerTableComponent {
  vehiclesForApproval: ElementForAccept[] = [];

  constructor(private purchaserService: PurchaserAndSelectedVehiclesService) { }

  ngOnInit(): void {
    this.fetchVehiclesForApproval();
  }


  async fetchVehiclesForApproval(queryVehicle: string = '', queryUser: string = ''): Promise<void> {

    try {
      const data = await this.purchaserService.getVehiclesForApproval(queryVehicle, queryUser);
      this.vehiclesForApproval = data.listForAccept;
    } catch (error) {
      console.error('Error fetching vehicles for approval', error);
    }
  }

  onSearchFilters(filters: { queryVehicle: string; queryUser: string }): void {
    this.fetchVehiclesForApproval(filters.queryVehicle, filters.queryUser);
  }

  async approveCustomer(vehicleId: number, profileId: number, type: string) {
    try {
      await this.purchaserService.approveCustomer(vehicleId, profileId, type);
      this.vehiclesForApproval = this.vehiclesForApproval.filter(
        (item) => item.vehicle.id !== vehicleId
      );
    } catch (error) {
      console.error('Erro ao aprovar o cliente:', error);
    }
  }

  async negateCustomer(vehicleId: number, profileId: number, type: string) {
    try {
      await this.purchaserService.negateCustomer(vehicleId, profileId, type);
      this.vehiclesForApproval = this.vehiclesForApproval.filter(
        (item) => item.vehicle.id !== vehicleId || item.profile.id !== profileId
      );
    } catch (error) {
      console.error('Erro ao negar o cliente:', error);
    }
  }
}
