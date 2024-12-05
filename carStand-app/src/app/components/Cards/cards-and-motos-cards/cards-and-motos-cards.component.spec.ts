import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardsAndMotosCardsComponent } from './cards-and-motos-cards.component';

describe('CardsAndMotosCardsComponent', () => {
  let component: CardsAndMotosCardsComponent;
  let fixture: ComponentFixture<CardsAndMotosCardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardsAndMotosCardsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CardsAndMotosCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
