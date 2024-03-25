// Device class
class Device {
    // Attribute battery
    protected int battery;

    // Constructor
    public Device() {
        this.battery = 100;
    }

    // Method to display battery life
    public void displayBattery() {
        System.out.println("Battery remaining: " + this.battery);
    }
}
