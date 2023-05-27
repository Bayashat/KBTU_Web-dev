import { Component } from '@angular/core';
import { products_laptop, products_cameras, products_pcs, products_phones } from './products';
import { Product } from './products';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // declare the category 
  category: Product[] = [];

  // provide product by selected category
  categorySelect(id: number){
    if(id == 1){
      this.category = products_laptop;
    } 
    else if(id == 2){
      this.category = products_phones;
    } 
    else if(id == 3){
      this.category = products_cameras;
    } else if(id == 4){
      this.category = products_pcs;
    } else {
      this.category = [];
    }

  }
}
