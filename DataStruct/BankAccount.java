public class BankAccount {
    int accountNumber;
    String accountHolder;
    double balance;

    public BankAccount(int accountNumber, String accountHolder, double balance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public void withdraw(double amount) {
        balance -= amount;
    }

    public void display() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Account Holder: " + accountHolder);
        System.out.println("Balance: " + balance);
    }

    public static void main(String[] args) {
        BankAccount account = new BankAccount(123456, "John Doe", 1000);
        account.deposit(500);
        account.withdraw(200);
        account.display();
    }
}
