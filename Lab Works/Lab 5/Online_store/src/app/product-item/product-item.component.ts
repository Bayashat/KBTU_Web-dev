import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Product } from '../products';

@Component({
	selector: 'app-product-item',
	templateUrl: './product-item.component.html',
	styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
	@Input() product: Product;  // get the product items from parent component 
	@Output() remove = new EventEmitter();  

	cnt:number = 0;
	is_liked: boolean = false;

	constructor() {
		this.product = {
			id: 0,
			name: '',
			price: 0,
			description: '',
			rating: 0,
			url: '',
			image: ''
		};
	}

	share_wtsp(item_url: string) {
		window.alert(window.open(`https://web.whatsapp.com://send?text=${item_url}`));
	}

	share_telegram(item_url: string) {
		window.alert(window.open(`https://telegram.me/share/url?url=<${item_url}>&text=<TEXT>`));
	}


	liked(){
		this.is_liked = !this.is_liked
		this.is_liked ? this.cnt++ : this.cnt--;
	}

	// send the remove info to parent comp
	removeProduct(){
		this.remove.emit(this.product)
	}
}
