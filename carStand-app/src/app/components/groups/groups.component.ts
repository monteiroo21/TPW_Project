import { Component, inject } from '@angular/core';
import { BrandsAndGroupsCardsComponent } from '../Cards/brands-and-groups-cards/brands-and-groups-cards.component';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Group } from '../../interfaces/group';
import { GroupService } from '../../services/group.service';

@Component({
  selector: 'app-groups',
  standalone: true,
  imports: [CommonModule, BrandsAndGroupsCardsComponent, FormsModule],
  templateUrl: './groups.component.html',
  styleUrls: ['./groups.component.css']
})
export class GroupsComponent {
  groups: Group[] = [];
  groupService: GroupService = inject(GroupService);

  constructor() {
    this.groupService.getGroups().then(groups => this.groups = groups);
  }
}
