// const arr1 = [1, 2, 3];
// const separator1 = ", ";
// const expected1 = "1, 2, 3";

// const arr2 = [1, 2, 3];
// const separator2 = "-";
// const expected2 = "1-2-3";

// const arr3 = [1, 2, 3];
// const separator3 = " - ";
// const expected3 = "1 - 2 - 3";

// const arr4 = [1];
// const separator4 = ", ";
// const expected4 = "1";

// const arr5 = [];
// const separator5 = ", ";
// const expected5 = "";

// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// take 5-7 mins to write the pseudocode here:

// create the function and decide what params it needs and what it will return
function join(arr, separator) {
    var expected=[]
    for(var i=0; i<arr.length;i++){
        if (i != arr.length-1){
            expected+=(arr[i]+separator)
        }else{
            expected+=arr[i]
        }
    }
    return expected
}

console.log(join([1,2,3], '+'))