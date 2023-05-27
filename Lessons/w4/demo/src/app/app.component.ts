import { Component } from '@angular/core';
// import { Student } from './models'

// interface Student {
//   name: string;
//   age: number;
// }

@Component({
	selector: 'app-root',
	templateUrl: './app.component.html',
	styleUrls: ['./app.component.css']
})
export class AppComponent {
	title;
	message: string;
	numbers: number[];
	isOK: boolean;
	students: any[];
	items: string[];
	inputData: string;

	constructor() {
		console.log('constructor of AppComponent started')
		this.title = "demo";
		this.message = "Hello"
		this.numbers = [1, 2, 3];
		this.isOK = false;
		this.students = [
			{
				id: '21BD123123',
				name: 'Student 1',
				gpa: 3.7
			},
			{
				id: '22BD456456',
				name: 'Student 2',
				gpa: 3.2
			},
			{
				id: '20BD789789',
				name: 'Student 3',
				gpa: 3.5
			}
		];
		this.items = [];
		this.inputData = '';
	}

	btnClick() {
		this.isOK = !this.isOK;
	}

	addItem() {
		if (this.inputData != '') {
			this.items.push(this.inputData)
			this.inputData = ''
		} else {
			alert('Enter the task name!')
		}
	}

	deleteItem(index: number) {
		this.items.splice(index, 1);
	}
}
