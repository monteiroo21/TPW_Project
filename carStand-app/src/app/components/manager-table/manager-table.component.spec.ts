import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManagerTableComponent } from './manager-table.component';

describe('ManagerTableComponent', () => {
  let component: ManagerTableComponent;
  let fixture: ComponentFixture<ManagerTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ManagerTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ManagerTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
