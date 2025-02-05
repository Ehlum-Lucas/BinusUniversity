public class SavingsAccount extends BankAccount {
    double interestRate;

    public SavingsAccount(int accountNumber, String accountHolder, double balance, double interestRate) {
        super(accountNumber, accountHolder, balance);
        this.interestRate = interestRate;
    }

    public void addInterest() {
        balance += balance * interestRate;
    }

    public static void main(String[] args) {
        SavingsAccount account = new SavingsAccount(123456, "John Doe", 1000, 0.05);
        account.deposit(500);
        account.addInterest();
        account.display();
    }
}