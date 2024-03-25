
public class Gorilla extends Mamals {
	 
	
	// Methods
	public int throwSomething() {
		System.out.println("Gorilla throw something"+ this.energy );
		return this.energy -= 5;
		
		
	}
	public int eatBananas() {
		System.out.println("gorilla's satisfaction"+ this.energy);
		return this.energy += 10;
		
	}
	public int climb() {
		System.out.println("gorilla has climbed a tree"+ this.energy);
		return this.energy -=10;
	}

}
