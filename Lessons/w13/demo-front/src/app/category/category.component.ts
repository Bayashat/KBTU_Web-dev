import {Component, OnInit} from '@angular/core';
import {Category} from "../module";
import {CategoryService} from "../category.service";
import {LoginService} from "../login.service";

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit{

  categories: Category[] = [];
  newCategory: string = "";

  constructor(private categoryService: CategoryService) {}

  ngOnInit() {
    this.getCategories();
  }

  getCategories() {
    this.categoryService.getCategories().subscribe(data => {
      this.categories = data;
    })
  }

  addCategory(){
    this.categoryService.createCategories(this.newCategory).subscribe((category) => {
      this.categories.push(category);
      this.newCategory = '';
    });
  }

  deleteCategory(category_id: number) {
    this.categories = this.categories.filter((category) => category.id != category_id);

    this.categoryService.deleteCategory(category_id).subscribe((data) => {
    });
  }
}
