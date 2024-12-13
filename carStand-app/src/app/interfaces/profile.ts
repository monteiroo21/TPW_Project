import { User } from "./user";

export interface Profile {
    id: number;
    user: User;
    first_name: string;
    last_name: string;
    email: string;
  }