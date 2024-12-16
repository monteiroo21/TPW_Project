import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DesiredVehiclesComponent } from './desired-vehicles.component';

describe('DesiredVehiclesComponent', () => {
  let component: DesiredVehiclesComponent;
  let fixture: ComponentFixture<DesiredVehiclesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DesiredVehiclesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DesiredVehiclesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
