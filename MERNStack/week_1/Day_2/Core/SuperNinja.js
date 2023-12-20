
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
