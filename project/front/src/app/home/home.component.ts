import { Component, OnInit } from '@angular/core';
import {first} from 'rxjs/internal/operators';
import {User} from '../login/models/user';
import * as jwt_decode from 'jwt-decode';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  currentUser: User;
    users: User[] = [];

    constructor() {
      const token = localStorage.getItem('currentUser');
      console.log(token);
      const decoded_token = jwt_decode(token);
      console.log(decoded_token);
        this.currentUser = decoded_token;
    }

    ngOnInit() {
        // this.loadAllUsers();
    }

}
