public class BankTest {
    public static void main(String[] args)
    {
        //Create a new Bank Account with an initial balance of 100.
        //Instantiate the bank account object and call deposit method to add money into it, then withdraw some amount from it.
    	 BankAccount account = new BankAccount(0,25100);
//        BankAccount account1 = new BankAccount(1000,25100);
        System.out.println("TotalBalance"+ account.totalBalance());    
        System.out.println("++++++++++++++++");
        account.depositMoney(25,"checking");
        System.out.println("Deposit money"+ account.getCheckingBalance());
        System.out.println("++++++++++++++++");
        System.out.println("TotalBalance"+ account.totalBalance());

        account.withdrawMoney(75,"saving");
        System.out.println("Withdraw money"+ account.getSavingBalance());
        System.out.println("TotalBalance"+ account.totalBalance());

        System.out.println("++++++++++++++++");

        System.out.println("Number of Account "+ BankAccount.getNumberOfAccounts());     
            System.out.println(BankAccount.getTotalAmount());    
   
        System.out.println("Total Balance" + account.totalBalance());    
    }
}