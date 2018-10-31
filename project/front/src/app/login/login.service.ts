import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';
import {environment} from '../../environments/environment';
import {first} from "rxjs/internal/operators";


@Injectable()
export class AuthenticationService {
    constructor(private http: HttpClient) { }

    login(username: string, password: string)
    {
        return this.http.post<any>(
          `${environment.authUrl}/log-in/`,
          {
            username: username,
            password: password
          }
          )
            .pipe(
              map(
                user =>
                {
                  console.log(user);
                  // login successful if there's a jwt token in the response
                  if (user && user.response)
                  {
                      // store user details and jwt token in local storage to keep user logged in between page refreshes
                      localStorage.setItem('currentUser', user.response);
                  }
                  return user;
                }
              )
            );
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
    }

    signup(first_name: string, last_name: string, username: string, email: string, password: string) {
        return this.http.post<any>(
          `${environment.authUrl}/sign-up/`,
          {
            first_name: first_name,
            last_name: last_name,
            username: username,
            email: email,
            password: password
          }
        )
          .pipe(
              map(
                user =>
                {
                    console.log(user);
                    // login successful if there's a jwt token in the response
                    if (user && user.response)
                    {
                        // store user details and jwt token in local storage to keep user logged in between page refreshes
                        localStorage.setItem('currentUser', user.response);
                    }
                    return user;
                }
              )
          );
    }
}
