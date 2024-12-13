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
import { BrandsAndGroupsCardsComponent } from '../../Cards/brands-and-groups-cards/brands-and-groups-cards.component';

@Component({
  selector: 'app-groups-and-brands-details',
  imports: [CommonModule, FormsModule, GoBackComponent, BrandsAndGroupsCardsComponent],
  templateUrl: './groups-and-brands-details.component.html',
  styleUrl: './groups-and-brands-details.component.css'
})
export class GroupsAndBrandsDetailsComponent {
  @Input() group: Group | undefined = undefined;
  @Input() brands: Brand[] | undefined = undefined;
  @Input() brand: Brand | undefined = undefined;
  @Input() cars: Car[] | undefined = undefined;
  @Input() motos: Moto[] | undefined = undefined;

  groupService: GroupService = inject(GroupService);
  brandService: BrandService = inject(BrandService);

  urlImage: string = "http://localhost:8000";
  constructor(private route: ActivatedRoute, private location: Location) {
    const type: string = this.route.snapshot.params['type'];
    const num: string = this.route.snapshot.params['num'];
  
    if (type === "group") {
      this.getGroupDetails(+num);
    } else if (type === "brand") {
      this.getBrandDetails(+num);
    } else {
      console.error("Invalid type parameter:", type);
    }
  }

  getGroupDetails(num: number): void {
    if (!num) {
      console.error("No group ID provided");
      return;
    }
  
    this.groupService.getGroup(num).then((group: Group) => {
      this.group = group;
      this.brands = group.brands; // Define as marcas do grupo
      console.log("Detalhes do grupo:", group);
  
      // Processar cada marca e dividir os modelos em carros e motas
      this.brands?.forEach((brand) => {
        this.brandService.getModelsByBrand(brand.id).then((models) => {
          brand.models = models;
          brand.cars = models.filter((model) => model.vehicle_type === "Car"); // Filtra carros
          brand.motos = models.filter((model) => model.vehicle_type === "Moto"); // Filtra motas
  
          console.log(`Modelos para a marca ${brand.name}:`, models);
          console.log(`Carros para a marca ${brand.name}:`, brand.cars);
          console.log(`Motas para a marca ${brand.name}:`, brand.motos);
        }).catch((error) => {
          console.error(`Erro ao buscar modelos para a marca ${brand.name}:`, error);
        });
      });
    }).catch((error) => {
      console.error("Erro ao buscar detalhes do grupo:", error);
    });
  }
  
  getBrandDetails(num: number): void {
    if (!num) {
      console.error("No brand ID provided");
      return;
    }
  
    this.brandService.getBrand(num).then((brand: Brand) => {
      this.brand = brand;
      console.log("Fetched brand details:", brand);
    }).catch((error) => {
      console.error("Error fetching brand details:", error);
    });
  
    this.brandService.getModelsByBrand(num).then((data: { cars: Car[], motos: Moto[] }) => {
      this.cars = data.cars;
      this.motos = data.motos;
      console.log("Fetched cars:", data.cars);
      console.log("Fetched motos:", data.motos);
    }).catch((error) => {
      console.error("Error fetching cars and motos:", error);
    });
  }

  ngOnInit(): void {
    const type = this.route.snapshot.params['type'];
    const num = this.route.snapshot.params['num'];
  
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
}
