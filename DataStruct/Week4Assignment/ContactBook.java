public class ContactBook {
    private Contact head;
    private Contact tail;

    ContactBook() {
        head = null;
        tail = null;
    }

    void addContact(String name, String email, String phoneNumber) {
        Contact newContact = new Contact(name, email, phoneNumber);
        if (head == null) {
            head = newContact;
            tail = newContact;
        } else {
            tail.next = newContact;
            tail = newContact;
        }
    }

    void deleteContact(String name) {
        if (head == null) {
            System.out.println("Contact book is empty.");
            return;
        }

        if (head.name.equals(name)) {
            head = head.next;
            System.out.println("Contact deleted.");
            return;
        }

        Contact current = head;
        while (current.next != null) {
            if (current.next.name.equals(name)) {
                current.next = current.next.next;
                System.out.println("Contact deleted.");
                return;
            }
            current = current.next;
        }
        System.out.println("Contact not found.");
    }

    void searchContact(String name) {
        if (head == null) {
            System.out.println("Contact book is empty.");
            return;
        }

        Contact current = head;
        while (current != null) {
            if (current.name.equals(name)) {
                System.out.println("Name: " + current.name);
                System.out.println("Email: " + current.email);
                System.out.println("Phone Number: " + current.phoneNumber);
                return;
            }
            current = current.next;
        }
        System.out.println("Contact not found.");
    }

    void searchByEmailContact(String email) {
        if (head == null) {
            System.out.println("Contact book is empty.");
            return;
        }

        Contact current = head;
        while (current != null) {
            if (current.email.equals(email)) {
                System.out.println("Name: " + current.name);
                System.out.println("Email: " + current.email);
                System.out.println("Phone Number: " + current.phoneNumber);
                return;
            }
            current = current.next;
        }
        System.out.println("Contact not found.");
    }

    void printContacts() {
        if (head == null) {
            System.out.println("Contact book is empty.");
            return;
        }

        Contact current = head;
        while (current != null) {
            System.out.println("Name: " + current.name);
            System.out.println("Email: " + current.email);
            System.out.println("Phone Number: " + current.phoneNumber);
            System.out.println();
            current = current.next;
        }
    }
}