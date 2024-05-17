// Push Front
function pushFront(arr, val) {
    for (let i = arr.length; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = val;
    return arr;
}

// Examples
console.log(pushFront([5, 7, 2, 3], 8)); // => [8,5,7,2,3]
console.log(pushFront([99], 7)); // => [7,99]

// Pop Front
function popFront(arr) {
    if (arr.length === 0) return undefined;
    let first = arr[0];
    for (let i = 1; i < arr.length; i++) {
        arr[i - 1] = arr[i];
    }
    arr.length--; // Reduce array length by 1
    console.log(arr); // Print the array after removal
    return first;
}

// Examples
console.log(popFront([0, 5, 10, 15])); // => 0 returned, with [5,10,15] printed
console.log(popFront([4, 5, 7, 9])); // => 4 returned, with [5,7,9] printed

// Insert At
function insertAt(arr, index, val) {
    for (let i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    arr[index] = val;
    return arr;
}

// Examples
console.log(insertAt([100, 200, 5], 2, 311)); // => [100,200,311,5]
console.log(insertAt([9, 33, 7], 1, 42)); // => [9,42,33,7]

// BONUS: Remove At
function removeAt(arr, index) {
    if (index < 0 || index >= arr.length) return undefined;
    let removed = arr[index];
    for (let i = index + 1; i < arr.length; i++) {
        arr[i - 1] = arr[i];
    }
    arr.length--; // Reduce array length by 1
    console.log(arr); // Print the array after removal
    return removed;
}

// Examples
console.log(removeAt([1000, 3, 204, 77], 1)); // => 3 returned, with [1000,204,77] printed
console.log(removeAt([8, 20, 55, 44, 98], 3)); // => 44 returned, with [8,20,55,98] printed

// BONUS: Swap Pairs
function swapPairs(arr) {
    for (let i = 0; i < arr.length - 1; i += 2) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
    }
    return arr;
}

// Examples
console.log(swapPairs([1, 2, 3, 4])); // => [2,1,4,3]
console.log(swapPairs(["Brendan", true, 42])); // => [true,"Brendan",42]

// BONUS: Remove Duplicates
function removeDupes(arr) {
    if (arr.length === 0) return arr;
    let newIndex = 1;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[i - 1]) {
            arr[newIndex] = arr[i];
            newIndex++;
        }
    }
    arr.length = newIndex; // Reduce array length to remove duplicates
    return arr;
}

// Examples
console.log(removeDupes([-2, -2, 3.14, 5, 5, 10])); // => [-2,3.14,5,10]
console.log(removeDupes([9, 19, 19, 19, 19, 19, 29])); // => [9,19,29]
