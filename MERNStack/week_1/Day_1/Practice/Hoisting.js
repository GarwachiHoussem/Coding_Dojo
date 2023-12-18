// // GIVEN

// var example = "I'm the example!";
// console.log(example);
// AFTER HOISTING BY THE INTERPRETER
// // var example;
// // console.log(example); // logs undefined
// // example = "I'm the example!";
// let example = "I'm the example!";   
// console.log(example);


//1-
// var hello = 'world';        
// console.log(hello);                                   
                         
// // undefined
//2-
// var needle = 'haystack';
// test();
// function test(){
//     var needle = 'magnet';
//     console.log(needle);
// // }
// // magnet\
//3
// var brendan = 'super cool';
// function print(){
//     brendan = 'only okay';
//     console.log(brendan);
// }
// console.log(brendan);
// // super cool 
//4
// var food = 'chicken';
// console.log(food);
// eat();
// function eat(){
//     food = 'half-chicken';
//     console.log(food);
//     var food = 'gone';
// }

// chicken

//5




// var mean = function() {
//     var food; 
//     food = "chicken"; 
//     console.log(food); 
//     food = "fish"; 
//     console.log(food); 
// }

// var food; 

// console.log(food); 

// mean(); 

//6

//
var genre; 
console.log(genre); 
genre = "disco"; 

rewind(); 

function rewind() {
    var genre; // Declaration is hoisted to the top of the function scope
    genre = "rock"; // Assign "rock" to the local genre variable inside the function
    console.log(genre); // Output: "rock"
    genre = "r&b"; // Reassign "r&b" to the local genre variable inside the function
    console.log(genre); // Output: "r&b"
}

console.log(genre); // Output: "disco" (value assigned outside the function)


//8
function makeDojo(name, students) {
    const dojo = {
        name: name,
        students: students
    };

    if (dojo.students > 50) {
        dojo.hiring = true;
    } else if (dojo.students <= 0) {
        dojo.status = "closed for now";
    }

    return dojo;
}

console.log(makeDojo("Chicago", 65));
console.log(makeDojo("Berkeley", 0));



