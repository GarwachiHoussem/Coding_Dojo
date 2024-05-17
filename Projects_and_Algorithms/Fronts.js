class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    addFront(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    removeFront() {
        if (this.head === null) {
            return null;
        }
        const removedNode = this.head;
        this.head = this.head.next;
        return this.head;
    }

    front() {
        if (this.head === null) {
            return null;
        }
        return this.head.data;
    }
}

// Examples:
const SLL1 = new SLL();
console.log(SLL1.addFront(18)); // => Node { data: 18, next: null }
console.log(SLL1.addFront(5));  // => Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.addFront(73)); // => Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } }

console.log(SLL1.removeFront()); // => Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.removeFront()); // => Node { data: 18, next: null }
console.log(SLL1.removeFront()); // => null (since the list is now empty)

console.log(SLL1.addFront(18));  // Re-adding node to test front method
console.log(SLL1.front());       // => 18
console.log(SLL1.removeFront()); // => null (remove the last element)
console.log(SLL1.front());       // => null (since the list is now empty)
