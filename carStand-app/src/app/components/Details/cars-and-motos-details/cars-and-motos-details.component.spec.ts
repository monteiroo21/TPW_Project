import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarsAndMotosDetailsComponent } from './cars-and-motos-details.component';

describe('CarsAndMotosDetailsComponent', () => {
  let component: CarsAndMotosDetailsComponent;
  let fixture: ComponentFixture<CarsAndMotosDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CarsAndMotosDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarsAndMotosDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
