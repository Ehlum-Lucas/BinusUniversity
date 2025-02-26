public class Contact {
    String name, email, phoneNumber;
    Contact next;

    Contact(String name, String email, String phoneNumber) {
        this.name = name;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.next = null;
    }
}
