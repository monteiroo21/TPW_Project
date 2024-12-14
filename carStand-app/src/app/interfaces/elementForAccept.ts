import { Car } from "./car";
import { Moto } from "./moto";
import { Profile } from "./profile";

export interface ElementForAccept {
    vehicle: Car | Moto ;
    profile: Profile;
    type: string;
  }