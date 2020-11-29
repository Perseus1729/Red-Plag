import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { User } from './user';
import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService  implements CanActivate{

  constructor(private router: Router,private service:UserService) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if(this.service.isValid){
      return true;
    }
    this.router.navigate(['/login']);
    return false;
  }
}
