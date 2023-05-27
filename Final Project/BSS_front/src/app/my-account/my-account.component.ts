import { Component, OnInit } from '@angular/core';
import { RouterLink, Router } from '@angular/router';

@Component({
  selector: 'app-my-account',
  templateUrl: './my-account.component.html',
  styleUrls: ['./my-account.component.css']
})
export class MyAccountComponent implements OnInit {

  constructor(public router: Router) { }

  ngOnInit(): void {
  }

  currentAcc = {
    id: 1,
    name: "Shang",
    surname: "Qi",
    img: "",
    age: 20,
    orderStory: ["Lanzhou Noodles", "Risotto"],
    addInfo: "Single and good-looking. Favorite food category Fast food.",
  }

}
