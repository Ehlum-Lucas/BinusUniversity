public class DoublyLinkedList {
    class Node {
        String data;
        Node next;
        Node prev;

        Node(String data) {
            this.data = data;
            this.next = null;
            this.prev = null;
        }
    }

    private Node head;
    private Node tail;

    DoublyLinkedList() {
        head = null;
        tail = null;
    }

    public void addNode(String data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
    }

    public void deleteNode(String data) {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }
        if (head.data.equals(data)) {
            head = head.next;
            head.prev = null;
            System.out.println("Node deleted.");
            return;
        }
        Node current = head;
        while (current.next != null) {
            if (current.next.data.equals(data)) {
                current.next = current.next.next;
                if (current.next != null) {
                    current.next.prev = current;
                } else {
                    tail = current;
                }
                System.out.println("Node deleted.");
                return;
            }
            current = current.next;
        }
        System.out.println("Node not found.");
    }

    public Node searchNode(String data) {
        if (head == null) {
            System.out.println("List is empty.");
            return null;
        }
        Node current = head;
        while (current != null) {
            if (current.data.equals(data)) {
                System.out.println("Node found.");
                return current;
            }
            current = current.next;
        }
        System.out.println("Node not found.");
        return null;
    }

    public void printListNode() {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    public void printListNodeReverse() {
        if (tail == null) {
            System.out.println("List is empty.");
            return;
        }
        Node current = tail;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.prev;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DoublyLinkedList list = new DoublyLinkedList();
        list.addNode("A");
        list.addNode("B");
        list.addNode("C");
        list.addNode("D");
        list.printListNode();
        list.deleteNode("B");
        list.printListNode();
        list.printListNodeReverse();
        list.searchNode("C");
        list.searchNode("E");
    }
}
