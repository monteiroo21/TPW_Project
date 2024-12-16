import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { CarsComponent } from './components/cars/cars.component';
import { MotorBikesComponent } from './components/motor-bikes/motor-bikes.component';
import { BrandsComponent } from './components/brands/brands.component';
import { GroupsComponent } from './components/groups/groups.component';
import { CarsAndMotosDetailsComponent } from './components/Details/cars-and-motos-details/cars-and-motos-details.component';
import { GroupsAndBrandsDetailsComponent } from './components/Details/groups-and-brands-details/groups-and-brands-details.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { CreateVehicleComponent } from './components/create-vehicle/create-vehicle.component';
import { EditVehicleComponent } from './components/edit-vehicle/edit-vehicle.component';
import { CreateVehicleModelComponent } from './components/create-vehicle-model/create-vehicle-model.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent },
    { path: 'cars', component: CarsComponent },
    { path: 'motorbikes', component: MotorBikesComponent },
    { path: 'brands', component: BrandsComponent },
    { path: 'groups', component: GroupsComponent },
    { path: 'carsdetails/:type/:num', component: CarsAndMotosDetailsComponent },
    { path: 'motosdetails/:type/:num', component: CarsAndMotosDetailsComponent },
    { path: 'branddetails/:type/:num', component: GroupsAndBrandsDetailsComponent },
    { path: 'groupdetails/:type/:num', component: GroupsAndBrandsDetailsComponent },
    { path: 'vehiclecreate/:type', component: CreateVehicleComponent },
    { path: 'vehicleedit/:type/:id', component: EditVehicleComponent },
    { path: 'vehiclemodelcreate/:type', component: CreateVehicleModelComponent },
    { path: 'login', component: LoginComponent },
    { path: 'signup', component: SignupComponent },
];
