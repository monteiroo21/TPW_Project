import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ManagerTableComponent } from "../manager-table/manager-table.component";

@Component({
  selector: 'app-home',
  imports: [CommonModule, ManagerTableComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
