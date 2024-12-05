import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BrandsAndGroupsCardsComponent } from './brands-and-groups-cards.component';

describe('BrandsAndGroupsCardsComponent', () => {
  let component: BrandsAndGroupsCardsComponent;
  let fixture: ComponentFixture<BrandsAndGroupsCardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BrandsAndGroupsCardsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BrandsAndGroupsCardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
