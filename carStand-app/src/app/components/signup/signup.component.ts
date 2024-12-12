import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-signup',
  imports: [GoBackComponent, RouterLink,CommonModule, FormsModule],
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {
  username: string = '';
  email: string = '';
  first_name: string = '';
  last_name: string = '';
  password: string = '';
  confirmPassword: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  async onSignUp() {
    if (this.password !== this.confirmPassword) {
      this.errorMessage = 'Passwords do not match.';
      return;
    }

    const userData = {
      username: this.username,
      email: this.email,
      first_name: this.first_name,
      last_name: this.last_name,
      password: this.password,
    };

    try {
      const response = await this.authService.signUp(userData);
      if (response.message) {
        this.router.navigate(['/']);
      } else {
        this.errorMessage = 'Failed to sign up. Please try again.';
      }
    } catch (error) {
      this.errorMessage = 'An error occurred. Please try again.';
    }
  }
}
