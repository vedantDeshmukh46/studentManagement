import { Component, OnInit } from '@angular/core';

import { UserService } from '../../users';

@Component({
  selector: 'app-view-user',
  templateUrl: './view-user.html',
  styleUrls: ['./view-user.css']
})
export class ViewUserComponent {
  users: any | undefined;

  constructor(private userService: UserService) { 
   
  }

  ngOnInit(): void {
    this.userService.getUsers().subscribe(data => {
      this.users = data;
      console.log(data)
    });
  }

  deleteUser(id: number) {
    this.userService.deleteUser(id).subscribe(data => {
      console.log(data);
      this.ngOnInit();
    });
  }

}