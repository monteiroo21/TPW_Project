import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { AuthData } from '../../interfaces/authData';
import { Router, RouterLink } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports: [RouterLink, CommonModule],
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  authState: AuthData | null = null;
  isLogoutModalOpen: boolean = false;
  dropdownOpen = false;

  constructor(private authService: AuthService, private router: Router) {
    this.authService.authState$.subscribe((state) => {
      this.authState = state;
    });
  }


  toggleDropdown(): void {
    this.dropdownOpen = !this.dropdownOpen;
  }

  openLogoutModal(): void {
    this.isLogoutModalOpen = true;
    this.dropdownOpen = false; 
  }

  closeLogoutModal(): void {
    this.isLogoutModalOpen = false;
  }

  logout(): void {
    this.authService.logout().then(() => {
      this.dropdownOpen = false;
      this.isLogoutModalOpen = false;
      this.router.navigate(["/home"]);
    });
  }
}
