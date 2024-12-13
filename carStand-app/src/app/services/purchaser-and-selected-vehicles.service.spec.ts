import { TestBed } from '@angular/core/testing';

import { PurchaserAndSelectedVehiclesService } from './purchaser-and-selected-vehicles.service';

describe('PurchaserAndSelectedVehiclesService', () => {
  let service: PurchaserAndSelectedVehiclesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PurchaserAndSelectedVehiclesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
