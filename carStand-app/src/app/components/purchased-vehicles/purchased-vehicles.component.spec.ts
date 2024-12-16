import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PurchasedVehiclesComponent } from './purchased-vehicles.component';

describe('PurchasedVehiclesComponent', () => {
  let component: PurchasedVehiclesComponent;
  let fixture: ComponentFixture<PurchasedVehiclesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PurchasedVehiclesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PurchasedVehiclesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
