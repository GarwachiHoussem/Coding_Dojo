public class BankAccount{
    private double checkingBalance;
    private double savingBalance;

    private static int numberOfAccounts;

    private static double totalAmount;

    public BankAccount(double checkingBalance, double savingBalance){
        this.checkingBalance = checkingBalance;
        this.savingBalance = savingBalance;
        numberOfAccounts++;
        totalAmount += checkingBalance;
        totalAmount += savingBalance;
        
    }

    public void depositMoney(double amount, String account){
        if(account.equalsIgnoreCase("checking")){
            this.checkingBalance += amount;
            totalAmount += amount;
        } else if(account.equalsIgnoreCase("saving")){
            this.savingBalance += amount;
            totalAmount += amount;
        }

    }

    public void withdrawMoney(double amount, String account){
            if(account.equalsIgnoreCase("checking") && checkingBalance>=amount){
                this.checkingBalance -= amount;
                totalAmount -= amount;
            } else if(account.equalsIgnoreCase("saving") && checkingBalance>=amount){
                this.savingBalance -= amount;
                totalAmount -= amount;
            }

        }

    public double totalBalance(){
        return this.checkingBalance + this.savingBalance;
    }


    public double getCheckingBalance(){
        return this.checkingBalance;
    }

    public void setCheckingBalance(double newCheckingBalance){
        this.checkingBalance = newCheckingBalance;
    }

    public double getSavingBalance(){
        return this.savingBalance;
    }

    public void setSavingBalance(double newSavingBalance){
        this.savingBalance = newSavingBalance;
    }

    public static int getNumberOfAccounts(){
        return numberOfAccounts;
    }

    public static double getTotalAmount(){
        return totalAmount;
    }
}