import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Component, Input } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { BrandsAndGroupsCardsComponent } from '../Cards/brands-and-groups-cards/brands-and-groups-cards.component';
import { CardsAndMotosCardsComponent } from '../Cards/cards-and-motos-cards/cards-and-motos-cards.component';

@Component({
  selector: 'app-search-bar',
  standalone: true,
  imports: [CommonModule, FormsModule, BrandsAndGroupsCardsComponent, CardsAndMotosCardsComponent, HttpClientModule],
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  @Input() type!: string;
  searchQuery: string = '';
  results: any[] = [];

  constructor(private http: HttpClient) {}

  onSearch() {
    if (this.searchQuery.trim()) {
      this.http
        .get<any[]>(
          `http://localhost:8000/api/search/${this.type}/?q=${this.searchQuery}`
        )
        .subscribe(
          (results) => {
            this.results = results;
          },
          (error) => {
            this.results = [];
          }
        );
    } else {
      this.http
      .get<any[]>(`http://localhost:8000/api/${this.type}`)
      .subscribe(
        (results) => {
          this.results = results;
        },
        (error) => {
          this.results = [];
        }
      );
    }
  }

  ngOnInit() {
    this.http
      .get<any[]>(`http://localhost:8000/api/${this.type}`)
      .subscribe(
        (results) => {
          this.results = results;
        },
        (error) => {
          this.results = [];
        }
      );
  }
}
