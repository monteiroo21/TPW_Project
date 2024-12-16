import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProfileService } from '../../services/profile.service';
import { Profile } from '../../interfaces/profile';
import { GoBackComponent } from '../Buttons/go-back/go-back.component';

@Component({
  selector: 'app-profile',
  imports: [CommonModule, FormsModule, GoBackComponent],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent {
  profile!: Profile;

  isModalVisible: boolean = false;

  constructor(private profileService: ProfileService) {}

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
