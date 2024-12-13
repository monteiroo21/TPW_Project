import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VehiclesFilterComponent } from './vehicles-filter.component';

describe('VehiclesFilterComponent', () => {
  let component: VehiclesFilterComponent;
  let fixture: ComponentFixture<VehiclesFilterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VehiclesFilterComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VehiclesFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
