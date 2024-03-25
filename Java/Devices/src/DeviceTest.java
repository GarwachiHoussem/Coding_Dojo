
public class DeviceTest {
	// Method to test Phone actions
    public static void testActions() {
        Phone phone = new Phone();
        System.out.println("Testing Phone actions:");
        phone.makeCall();
        phone.makeCall();
        phone.makeCall();
        phone.playGame();
        phone.playGame();
        phone.charge();
    }

}

//Main class
public class Main {
 public static void main(String[] args) {
     // Testing Phone actions
     DeviceTest.testActions();
 }
}