import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {AuthToken} from "./module";
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  BASE_URL = "http://127.0.0.1:8000"

  constructor(private client: HttpClient) { }

  login(username: string, password: string): Observable<AuthToken> {
    return this.client.post<AuthToken>(
      `${this.BASE_URL}/api/login/`,
      {username, password}  // in new version of js, if key=value, we can simply it
    )
  }
}
