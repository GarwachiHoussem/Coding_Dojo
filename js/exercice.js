// function hello() {
//     console.log('hello');
//     return 15;
// }
// var result = hello();
// console.log('result is', result);

// var x= 10;
// if( x==10){
// console.log x);
// }

// for(var x=12; x>4; x-=1)
// {
//     console.log(x)
//     break;
// }

var arr = [-3, 4, 3, 6, 3.3, 1, 3];
var count = 0;
for(var i=0; i<arr.length; i++) {
    if(arr[i] == 3) {
        count++;
    }
}
console.log(count);
