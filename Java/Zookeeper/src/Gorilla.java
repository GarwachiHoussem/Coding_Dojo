
public class Gorilla extends Mamals {


	 // Constructor

	public Gorilla() {
		super();
	}
	// Methods
	public int throwSomething() {
	    this.energy -= 5;
	    System.out.println("Gorilla throws something. Energy remaining: " + this.energy);
	    return this.energy;
	}

	public int eatBananas() {
		this.energy +=10;
		System.out.println("gorilla's satisfaction " + this.energy);
		return this.energy ;
		
	}
	public int climb() {
		this.energy -= 10;
		System.out.println("gorilla has climbed a tree " + this.energy);
		return this.energy;
	}

}



