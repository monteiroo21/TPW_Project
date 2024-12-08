import { Component, inject } from '@angular/core';
import { CommonModule, Location } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Group } from '../../../interfaces/group';
import { Brand } from '../../../interfaces/brand';
import { GroupService } from '../../../services/group.service';
import { BrandService } from '../../../services/brand.service';
import { GoBackComponent } from '../../Buttons/go-back/go-back.component';

@Component({
  selector: 'app-groups-and-brands-details',
  imports: [CommonModule, FormsModule, GoBackComponent],
  templateUrl: './groups-and-brands-details.component.html',
  styleUrl: './groups-and-brands-details.component.css'
})
export class GroupsAndBrandsDetailsComponent {
  group: Group | undefined = undefined;
  brand: Brand | undefined = undefined;

  groupService: GroupService = inject(GroupService);
  brandService: BrandService = inject(BrandService);

  urlImage: string = "http://localhost:8000";
  constructor(private route: ActivatedRoute, private location: Location) {
    let type: string = this.route.snapshot.params['type'];
    if (type == "group") {
      this.getGroupDetails();
    }
    else {
      this.getBrandDetails();
    }
  }

  getGroupDetails(): void {
    let num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    num = +num;
    this.groupService.getGroup(num).then((group: Group) => { this.group = group; });
  }

  getBrandDetails(): void {
    let num: any = this.route.snapshot.params['num'];
    if (num == null)
      return undefined;
    num = +num;
    this.brandService.getBrand(num).then((brand: Brand) => { this.brand = brand; });
  }
}
