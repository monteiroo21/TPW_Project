import { Component } from '@angular/core';
import { PurchaserAndSelectedVehiclesService } from '../../services/purchaser-and-selected-vehicles.service';
import { CommonModule } from '@angular/common';
import { ElementForAccept } from '../../interfaces/elementForAccept';

@Component({
  selector: 'app-manager-table',
  imports: [CommonModule],
  templateUrl: './manager-table.component.html',
  styleUrl: './manager-table.component.css'
})
export class ManagerTableComponent {
  vehiclesForApproval: ElementForAccept[] = [];

  constructor(private purchaserService: PurchaserAndSelectedVehiclesService) {}

  async ngOnInit() {
    try {
      const response = await this.purchaserService.getVehiclesForApproval();
      this.vehiclesForApproval = response?.listForAccept ?? [];
    } catch (error) {
      console.error('Erro ao buscar veículos para aprovação:', error);
    }
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
