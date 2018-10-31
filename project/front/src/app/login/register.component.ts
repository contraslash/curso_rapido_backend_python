import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import {AlertService} from '../alert/alert.service';
import {AuthenticationService} from './login.service';


@Component({templateUrl: 'register.component.html'})
export class RegisterComponent implements OnInit {
    registerForm: FormGroup;
    loading = false;
    submitted = false;

    constructor(
        private formBuilder: FormBuilder,
        private router: Router,
        private alertService: AlertService,
        private authenticationService: AuthenticationService
    ) { }

    ngOnInit() {
        this.registerForm = this.formBuilder.group({
            firstName: ['', Validators.required],
            lastName: ['', Validators.required],
            username: ['', Validators.required],
            email: ['', Validators.required],
            password: ['', [Validators.required, Validators.minLength(6)]]
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit() {
        this.submitted = true;

        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }

        this.loading = true;
        this.authenticationService.signup(
          this.f.firstName.value,
          this.f.lastName.value,
          this.f.username.value,
          this.f.email.value,
          this.f.password.value
        )
            .pipe(first())
            .subscribe(
                data => {
                  console.log(data);
                  console.log(this.router);
                  console.log(this.returnUrl);
                    this.router.navigate([this.returnUrl]);
                },
                error => {
                  console.log(error);
                    this.alertService.error(error);
                    this.loading = false;
                });
    }
}
