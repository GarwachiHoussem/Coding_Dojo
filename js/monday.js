/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
  Do not ignore spaces, punctuation and capitalization
 */
// level
// racecar
// tacocat

const str1 = "a x a";
const expected1 = true;


const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

// take 5-7 mins to write the pseudocode here:

// create the function and decide what params it needs and what it will return

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
// function isPalindrome(str) {

//   let start = 0;
//   let end = str.length-1;

//   while (start < end) {
//     if (str[start] !== str[end]) {
//         return false;
//     }
//     start++;
//     end--;
    
// }

// return true;

// }

// console.log(isPalindrome(str1));
// console.log(isPalindrome(str2));
// console.log(isPalindrome(str3));
// console.log(isPalindrome(str4));


function isPalindrome(str=""){
for (var i=0; i<Math.floor(str.length/2); i++){

  if (str[i]!= str[str.length-1-i] ){
  }
}

    return false
  }


isPalindrome(srt1)


/\ 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
  hasOwnProperty()
*/
var user = {username:"John", age:35}

// console.log(user.hasOwnProperty('age'));
// console.log(user.hasOwnProperty('email'));

const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};
const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

function makeFrequencyTable(arr) {
}

