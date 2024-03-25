
public class Bat extends Mamals{
	
	// Constructor

	public Bat() {
		super(300);
	}
	
	// Method 
	public int fly() {
		this.energy -= 50;
		System.out.println("the bat is airborne " + this.energy);
		return this.energy;
	}
	
	public int eatHumans() {
		this.energy += 25;
		System.out.println("the bat's satisfaction " + this.energy);
		return this.energy;
	}
	public int attackTown() {
		this.energy -= 100;
		System.out.println("the bat's attack " + this.energy);
		return this.energy;
	}
	
	

}
