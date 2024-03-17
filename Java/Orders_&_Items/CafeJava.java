public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        String displayChargeDiffrence = "your refund is $";


        // Menu variables (add yours below)
        double mochaPrice = 3.5;

        // Drink Coffee:
        double drip = 2.3;
        double latte = 3.0;
        double cappuccino = 7.0;
    
        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";
    
        // Order completions (add yours below)
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2= true;
        boolean isReadyOrder3= false;
        boolean isReadyOrder4= true;

        // 



    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1);
        System.out.println( customer1 +" "+ isReadyOrder1);
        
        if (isReadyOrder2) {
            System.out.println(generalGreeting + customer4 + readyMessage);
            System.out.println(displayTotalMessage + cappuccino);
        }
        else {
            System.out.println(generalGreeting + customer4 + pendingMessage);
            }
// Question 6:
            System.out.println(displayTotalMessage + latte*2);
            if (isReadyOrder3){
                System.out.println(readyMessage);
            }
            else {
                System.out.println(pendingMessage);
            }


            //Question 7:


            double chargeDiffrenceRefund = (cappuccino - latte);
            System.out.println(displayChargeDiffrence + chargeDiffrenceRefund);



        





         // Displays "Welcome to Cafe Java, Cindhuri"
    	// ** Your customer interaction print statements will go here ** //
    }
}
