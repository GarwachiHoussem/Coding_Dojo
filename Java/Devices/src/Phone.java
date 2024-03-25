class Phone extends Device {
	// Method to make call
	public void makeCall () {
		if (this.battery >= 5) {
			System.out.println("Making a call📞");
			this.battery >=5;
			 displayBattery();
			 if (this.battery < 10) {
				 System.out.println("Battery Critical🪫");
				 else {
					 System.out.println("Battery to low to play Game 🪫 ");}
			 }
		}
	
		
	}
	
	// Method to play game
	
	public void playGame() {
		if (this.battery>= 25) {
			System.out.println("playing a game.");
			this.battery -= 20;
			displayBattery();
			if (this.battery < 10) {
				System.out.println("Battery critical");
			} else {
				System.out.println("Battery too low to play a game.");
			}
			
		}
		
	}
	// Method to charge phone
	public void charge() {
        System.out.println("Charging.");
        this.battery += 50;
        if (this.battery > 100) {
            this.battery = 100;
        }
        displayBattery();
	
	
	

}
