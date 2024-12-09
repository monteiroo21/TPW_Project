import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Group } from '../../interfaces/group';
import { GroupService } from '../../services/group.service';
import { SearchBarComponent } from '../search-bar/search-bar.component';

@Component({
  selector: 'app-groups',
  standalone: true,
  imports: [CommonModule, FormsModule, SearchBarComponent],
  templateUrl: './groups.component.html',
  styleUrls: ['./groups.component.css']
})
export class GroupsComponent {
  groups: Group[] = [];
  groupService: GroupService = inject(GroupService);

  constructor() {
    this.groupService.getGroups().then(groups => {
      this.groups = groups;
      console.log(this.groups);
    });
  }
}

