import { Component } from '@angular/core';
import { GoBackComponent } from "../Buttons/go-back/go-back.component";
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-signup',
  imports: [GoBackComponent, RouterLink],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {

}
