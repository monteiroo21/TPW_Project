import { Component } from '@angular/core';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-login',
  imports: [GoBackComponent, CommonModule, FormsModule, RouterLink],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) { }

  async onLogin() {
    try {
      const response = await this.authService.login(this.username, this.password);
      if (response.message) {
        this.router.navigate(['/']);
      } else {
        this.showErrorMessage('Invalid username or password.');
      }
    } catch (error) {
      this.showErrorMessage('An error occurred. Please try again.');
    }
  }
  async onLogout() {
    try {
      const response = await this.authService.logout();
      if (response.message) {
        this.router.navigate(['/']);
      } else {
        this.showErrorMessage('Invalid username or password.');
      }
    } catch (error) {
      this.showErrorMessage('An error occurred. Please try again.');
    }
  }

  private showErrorMessage(message: string) {
    this.errorMessage = message;
    setTimeout(() => {
      this.errorMessage = '';
    }, 5000);
  }
}