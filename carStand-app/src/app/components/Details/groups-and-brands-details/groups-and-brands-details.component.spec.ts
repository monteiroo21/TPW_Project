import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GroupsAndBrandsDetailsComponent } from './groups-and-brands-details.component';

describe('GroupsAndBrandsDetailsComponent', () => {
  let component: GroupsAndBrandsDetailsComponent;
  let fixture: ComponentFixture<GroupsAndBrandsDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GroupsAndBrandsDetailsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GroupsAndBrandsDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
