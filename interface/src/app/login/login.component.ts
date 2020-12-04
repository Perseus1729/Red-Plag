import { Component, OnInit } from '@angular/core';
import { FormGroup,FormControl,Validators } from '@angular/forms';

import { UserService } from '../user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginform:FormGroup;
  constructor(private userservice:UserService) { }

  ngOnInit(): void {
    this.loginform=new FormGroup({
      username : new FormControl('',[Validators.required]),
      password: new FormControl('',[Validators.required])
    });
  }  
  loginUser(){
    this.userservice.loginuser(JSON.stringify(this.loginform.value)).subscribe(
      response=>{
          alert("success");
          sessionStorage.setItem('token', response['token']);
          sessionStorage.setItem('username', this.loginform.get('username').value);
          location.replace("http://localhost:4200/home");
      },
      error=>{
        sessionStorage.setItem('token', '');
          sessionStorage.setItem('username', '');
          alert("incorrect credentials");
      }
    );
  }

}
