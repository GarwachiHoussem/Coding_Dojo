class Ninja{
    constructor(name, health= 100, speed= 3, strength= 3,){

        this.name= name
        this.health= health
        this.speed= speed
        this. strength= strength

    }
    sayName(){
        console.log(`My name is $(this.name)`);
    }

    showStats(){
        console.log(`Name: ${this.name}, Strength: ${this.strength}, Speed: ${this.speed}, Health: ${this.health} `);
    }
    drinkSake(){
        this.health=+10;
        console.log(`${this.name} drank sake and gained 10 health`);
    }
}
const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.showStats();


class Sensei extends Ninja{
    constructor(name, health = 200, speed = 10, strength = 10, wisdom = 10){
        super(name,health,speed, strength);
        this.wisdom=wisdom;
        }
    speakWisdom() {
        super.drinkSake();
        console.log("A wise message from the sensei: The journey of a thousand miles begins with one step.");
        }
    }
    const sensei1 = new Sensei("Master Splinter");
    sensei1.sayName(); 
    sensei1.showStats(); 
    sensei1.speakWisdom();
