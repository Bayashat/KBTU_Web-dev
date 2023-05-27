//  1.
let i = 3;

while (i) {
  alert( i-- );
}   // last one is 1

//  2.
let j = 0;
while (++j < 5) alert( j );  // from 1 to 4

let x = 0;
while (x++ < 5) alert( x );  // from 1 to 5

//  3.
for (let i = 0; i < 5; i++) alert( i );  // 0~4
for (let i = 0; i < 5; ++i) alert( i );  // 0~4

//  4.
for (let i = 2; i <= 10; i++) {
    if (i % 2 == 0) {
      alert( i );
    }
  }

//  5.
let y = 0;
while (y < 3) {
    alert( `number ${y}!` );
    y++;
}

//  6.
let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);

//  7.
let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) {

  for (let j = 2; j < i; j++) {
    if (i % j == 0) continue nextPrime;
  }

  alert( i ); 
}