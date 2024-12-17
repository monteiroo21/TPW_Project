import { Component, inject, Input, OnInit } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Group } from '../../../interfaces/group';
import { Brand } from '../../../interfaces/brand';
import { Car } from '../../../interfaces/car';
import { Moto } from '../../../interfaces/moto';
import { GroupService } from '../../../services/group.service';
import { BrandService } from '../../../services/brand.service';
import { GoBackComponent } from '../../Buttons/go-back/go-back.component';
import { BrandsAndGroupsCardsComponent } from "../../Cards/brands-and-groups-cards/brands-and-groups-cards.component";
import { CardsAndMotosBrandsCardComponent } from '../../Cards/cards-and-motos-brands-card/cards-and-motos-brands-card.component';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-groups-and-brands-details',
  imports: [CommonModule, FormsModule, GoBackComponent, BrandsAndGroupsCardsComponent, CardsAndMotosBrandsCardComponent],
  templateUrl: './groups-and-brands-details.component.html',
  styleUrl: './groups-and-brands-details.component.css'
})
export class GroupsAndBrandsDetailsComponent implements OnInit {
  @Input() group: Group | undefined = undefined;
  @Input() brands: Brand[] | undefined = undefined;
  @Input() brand: Brand | undefined = undefined;
  @Input() cars: Car[] = [];
  @Input() motos: Moto[] = [];
  
  baseURL = environment.apiBaseUrl;

  groupService: GroupService = inject(GroupService);
  brandService: BrandService = inject(BrandService);

  constructor(private route: ActivatedRoute, private location: Location) { }

  ngOnInit(): void {
    const type = this.route.snapshot.params['type'];
    const num = this.route.snapshot.params['num'];
    const id = this.route.snapshot.params['id'];

    if (id) {
      this.brandService.getBrandVehicles(id).then((data) => {
        console.log("Brand vehicles fetched:", data);
        this.brand = data.brand;
        this.cars = data.cars;
        this.motos = data.motos;
      });
    }

    if (!type || !num) {
      console.error("Missing route parameters: type or num");
      return;
    }

    if (type === "group") {
      this.getGroupDetails(+num);
    } else if (type === "brand") {
      this.getBrandDetails(+num);
    } else {
      console.error("Invalid type parameter:", type);
    }
  }

  getGroupDetails(groupId: number): void {
    if (!groupId) {
      console.error("No group ID provided");
      return;
    }

    this.groupService.getGroup(groupId)
      .then((group: Group) => {
        this.group = group;
        this.brands = group.brands;
        console.log("Group details fetched:", group);
      })
      .catch((error) => {
        console.error("Error fetching group details:", error);
      });
  }

  getBrandDetails(brandId: number): void {
    if (!brandId) {
      console.error("No brand ID provided");
      return;
    }

    this.brandService.getBrand(brandId)
      .then((brand: Brand) => {
        this.brand = brand;
        console.log("Brand details fetched:", brand);
      })
      .catch((error) => {
        console.error("Error fetching brand details:", error);
      });

    this.brandService.getBrandVehicles(brandId)
      .then((data) => {
        console.log("Brand vehicles fetched:", data);
        this.cars = data.cars;
        this.motos = data.motos;
      })
      .catch((error) => {
        console.error("Error fetching brand vehicles:", error);
      });


  }
}
