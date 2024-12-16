import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardsAndMotosBrandsCardComponent } from './cards-and-motos-brands-card.component';

describe('CardsAndMotosBrandsCardComponent', () => {
  let component: CardsAndMotosBrandsCardComponent;
  let fixture: ComponentFixture<CardsAndMotosBrandsCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardsAndMotosBrandsCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CardsAndMotosBrandsCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
