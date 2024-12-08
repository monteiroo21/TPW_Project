import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-search-bar',
  imports: [CommonModule],
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  searchQuery: string = '';
  results: { brands: any[]; groups: any[]; cars: any[]; motos: any[] } | null = null;

  constructor(private http: HttpClient) {}

  onSearch() {
    if (this.searchQuery.trim()) {
      this.http
        .get<{ brands: any[]; groups: any[]; cars: any[]; motos: any[] }>(
          `http://localhost:8000/api/search?q=${this.searchQuery}`
        )
        .subscribe((results) => {
          this.results = results;
        });
    } else {
      this.results = null;
    }
  }
}
