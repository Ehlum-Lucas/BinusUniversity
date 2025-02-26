import java.util.Scanner;

public class ContactBookApp {
    public static char chooseCommand(Scanner scanner) {
        System.out.println("************************");
        System.out.println("(A)dd");
        System.out.println("(D)elete");
        System.out.println("(E)mail Search");
        System.out.println("(P)rint List");
        System.out.println("(S)earch");
        System.out.println("(Q)uit");
        System.out.println("************************");
        System.out.print("Please Enter a command: ");
        return scanner.next().toUpperCase().charAt(0);
    }

    public static void main(String[] args) {
        ContactBook contactBook = new ContactBook();
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        while (running) {
            char choice = chooseCommand(scanner);
            scanner.nextLine();

            switch (choice) {
                case 'A':
                    System.out.print("Enter Name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter Phone: ");
                    String phone = scanner.nextLine();
                    System.out.print("Enter Email: ");
                    String email = scanner.nextLine();
                    contactBook.addContact(name, phone, email);
                    break;
                case 'D':
                    System.out.print("Enter Name to delete: ");
                    String delName = scanner.nextLine();
                    contactBook.deleteContact(delName);
                    break;
                case 'E':
                    System.out.print("Enter Email to search: ");
                    String searchEmail = scanner.nextLine();
                    contactBook.searchByEmailContact(searchEmail);
                    break;
                case 'P':
                    contactBook.printContacts();
                    break;
                case 'S':
                    System.out.print("Enter Name to search: ");
                    String searchName = scanner.nextLine();
                    contactBook.searchContact(searchName);
                    break;
                case 'Q':
                    System.out.println("Exiting program...");
                    running = false;
                    break;
                default:
                    System.out.println("Invalid command. Please try again.");
            }
        }
        scanner.close();
    }
}
