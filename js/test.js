// var answer = 6 - 2 * 2;
// console.log(answer);

// var answer = (6 - 2) * 2;
// console.log(answer);


// for(var i=10; i<15; i++) {
//     console.log(i);
//     i += 2;
// }
// for(var i=3; i>-3; i--) {
//     console.log(i);
//     i -= 1;
// }

// var i = 13;
// if(i % 2 == 0) {
//     console.log("even");
// } else {
//     console.log(i);
// }

// for(var i=7; i>2; i--) {
//     if(i % 2 == 0) {
//         console.log(i);
//     } else {
//         console.log("odd");
//     }
// }


// var arr = [-3, 4, 3, 6, 3.3, 1, 3];
// var count = 0;
// for(var i=0; i<arr.length; i++) {
//     if(arr[i] == 3) {
//         count++;
//     }
// }
// console.log(count);


/* Question 8
 * Complete the function in the code below to console log all odd numbers from 3 to 99.
 */ 

// function printOdds3to99() {
//     for( var i=3; i<=99;i++){
//         if (i % 2 == 1) {
//             console.log(i)
//     }
//     }
//     }
    
//     printOdds3to99();

// Question9

// function findSmallest(arr) {
//     x = arr[0]
//     var test = false
//     while(test == false) {
//         for(i=1 ;i<arr.length;i++) {
//             if(arr[i] < x) {
//                 x = arr[i];
//                 test = false
//             }else {
//                 test = true
//             }
//         }
//     }
//     return x
// }

// console.log(findSmallest([3, 6, 4, 9, 2]));

// function countGreaterThanY(arr, y) {
//     var count = 0;
//     for(i=0;i<arr.length;i++) {
//         if (arr[i] > y) {
//             count++
//         } 
//     }
//     return count;
// }
// console.log(countGreaterThanY([22, 12, 13.6, 19, 42, 8], 15));

for(var i=1; i<25; i++) {
    console.log(i);
    i += 4;