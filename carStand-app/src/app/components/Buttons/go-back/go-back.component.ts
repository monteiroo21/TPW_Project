import { Component, Input } from '@angular/core';
import { Location } from '@angular/common';

@Component({
  selector: 'app-go-back',
  imports: [],
  templateUrl: './go-back.component.html',
  styleUrl: './go-back.component.css'
})
export class GoBackComponent {
  constructor(private location: Location) { }

  goBack(): void {
    this.location.back();
  }
}
