import { Component, OnInit } from '@angular/core';
import { FormGroup,FormControl,Validators } from '@angular/forms';
import { UserService } from '../user.service';
@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.css']
})
export class ChangePasswordComponent implements OnInit {

  changepasswordform:FormGroup;
  constructor(private service:UserService) { }

  ngOnInit(): void {
    this.changepasswordform=new FormGroup({
      username : new FormControl('',[Validators.required]),
      password: new FormControl('',[Validators.required])
    });
  }

  loginuser(){
    this.service.loginuser(this.changepasswordform.value)
  }

}
