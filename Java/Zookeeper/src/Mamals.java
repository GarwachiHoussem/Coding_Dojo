
public class  Mamals {
	
	// Member variables
	
	int energy=100;
	
	
	
	// Constructor (zero-args)

	public Mamals() {
		
	}

	// Constructor (all-args)
	
	public Mamals(int energy) {
		super();
		
		this.energy = energy;
	}
	
	// Method to display energy level
	
	public int displayEnergy() {
		System.out.println("Energy level" + this.energy);
		return this.energy;
	}
	
	

	// Getters & Setters
	public int getEnergy() {
		return energy;
	}

	public void setEnergy(int energy) {
		this.energy = energy;
	}
	
	

}
