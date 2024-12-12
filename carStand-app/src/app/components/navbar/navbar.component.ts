import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { AuthData } from '../../interfaces/authData';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports: [RouterLink, CommonModule],
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  authState: AuthData | null = null;
  dropdownOpen = false; // Controla a visibilidade do dropdown
  urlImage: string = "http://localhost:8000";

  constructor(private authService: AuthService) {
    this.authService.authState$.subscribe((state) => {
      this.authState = state;
    });
  }


  toggleDropdown(): void {
    this.dropdownOpen = !this.dropdownOpen; // Alterna o estado de visibilidade
  }

  logout(): void {
    this.authService.logout().then(() => {
      this.dropdownOpen = false; // Fecha o dropdown após logout
    });
  }
}
