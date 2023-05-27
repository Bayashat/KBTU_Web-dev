import {Component, OnInit} from '@angular/core';
import {LoginService} from "./login.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'demo-front';
  logged: boolean = false;
  username: string = '';
  password: string = '';

  constructor(private loginService: LoginService) {}
  ngOnInit() {
    const token = localStorage.getItem('token');
    if(token){
      this.logged = true
    }
  }
  login() {
    this.loginService.login(this.username, this.password).subscribe((data) => {
      localStorage.setItem('token', data.token); // 将得到的token存入 localStorage 中, 以便后续使用
      this.logged = true;
      this.username = '';
      this.password = '';
    })
  }

  logout() {
    this.logged = false;
    localStorage.removeItem('token');
  }

}
