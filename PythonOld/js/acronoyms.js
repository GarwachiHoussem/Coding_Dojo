/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const strA = "object oriented programming";
const expectedA = "OOP";

// The 4 pillars of OOP
const strB = "abstraction polymorphism inheritance encapsulation";
const expectedB = "APIE";

const strC = "software development life cycle";
const expectedC = "SDLC";
//- Bonus: ignore extra spaces
// const strD = "  global   information tracker    ";
// const expectedD = "GIT";
    //.split() ->
    // console.log()
    function acronomize(str){
    var result = ""
    words_array = str.split(" ")
    // return result
    for (let i = 0; i <words_array.length; i++){
      result+=  words_array[i][0].toUpperCase();
    }
    console.log(result)
    return result;
    
    
}
acronomize(strA)
