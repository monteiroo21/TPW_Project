import { TestBed } from '@angular/core/testing';

import { FilterSortService } from './filter-sort.service';

describe('FilterSortService', () => {
  let service: FilterSortService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FilterSortService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
