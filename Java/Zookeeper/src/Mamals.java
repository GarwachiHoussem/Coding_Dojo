
public class  Mamals {
	
	// Member variables
	
	int energy;
	
	
	
	// Constructor (zero-args)

	public Mamals() {
		
	}

	// Constructor (all-args)
	
	public Mamals(int energy) {
		
		this.energy = 100;
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
