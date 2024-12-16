import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProfileService } from '../../services/profile.service';
import { Profile } from '../../interfaces/profile';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';
import { AuthService } from '../../services/auth.service';
import { AuthData } from '../../interfaces/authData';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-profile',
  imports: [CommonModule, FormsModule, GoBackComponent, RouterLink],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {
  authService: AuthService = inject(AuthService);
  authState: AuthData | null = null;
  profile!: Profile;

  isModalVisible: boolean = false;

  constructor(private profileService: ProfileService) {
    this.authService.authState$.subscribe((state) => {
      this.authState = state;
    });
  }

  ngOnInit(): void {
    this.profileService.getProfile().then(
      (data) => {
        this.profile = data;
        console.log('Profile loaded:', this.profile);
      },
      (error) => {
        console.error('Error fetching current user profile:', error);
      }
    );
  }


  toggleModal(show: boolean): void {
    this.isModalVisible = show;
  }

  onSubmit() : void {
    this.profileService.editProfile(this.profile).then(
      (updatedProfile) => {
        console.log('Profile updated successfully:', updatedProfile);
        this.toggleModal(false);
      },
      (error) => {
        console.error('Error updating profile:', error);
      }
    );
  }
}
