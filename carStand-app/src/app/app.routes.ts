import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { CarsComponent } from './components/cars/cars.component';
import { MotorBikesComponent } from './components/motor-bikes/motor-bikes.component';
import { BrandsComponent } from './components/brands/brands.component';
import { GroupsComponent } from './components/groups/groups.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent },
    { path: 'cars', component: CarsComponent },
    { path: 'motorbikes', component: MotorBikesComponent },
    { path: 'brands', component: BrandsComponent },
    { path: 'groups', component: GroupsComponent },
];
