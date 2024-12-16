import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchBarTableComponent } from './search-bar-table.component';

describe('SearchBarTableComponent', () => {
  let component: SearchBarTableComponent;
  let fixture: ComponentFixture<SearchBarTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SearchBarTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SearchBarTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
