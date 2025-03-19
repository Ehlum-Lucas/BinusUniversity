import java.util.LinkedList;
import java.util.Queue;

public class OrderQueue {
    private Queue<String> regularOrders;
    private Queue<String> priorityOrders;

    public OrderQueue() {
        this.regularOrders = new LinkedList<>();
        this.priorityOrders = new LinkedList<>();
    }

    public void addRegularOrder(String order) {
        regularOrders.add(order);
    }

    public void addPriorityOrder(String order) {
        priorityOrders.add(order);
    }

    public String processOrder() {
        if (!priorityOrders.isEmpty()) {
            return priorityOrders.poll();
        } else if (!regularOrders.isEmpty()) {
            return regularOrders.poll();
        } else {
            return null;
        }
    }

    public boolean removeOrder(String order) {
        if (priorityOrders.contains(order)) {
            return priorityOrders.remove(order);
        } else if (regularOrders.contains(order)) {
            return regularOrders.remove(order);
        } else {
            return false;
        }
    }

    public void displayOrders() {
        System.out.println("Priority Orders:");
        for (String order : priorityOrders) {
            System.out.println(order);
        }
        System.out.println("Regular Orders:");
        for (String order : regularOrders) {
            System.out.println(order);
        }
    }

    public boolean containsOrder(String order) {
        return containsOrderRecursive(priorityOrders, order) || containsOrderRecursive(regularOrders, order);
    }

    private boolean containsOrderRecursive(Queue<String> queue, String order) {
        if (queue.isEmpty()) {
            return false;
        }
        String current = queue.poll();
        boolean found = current.equals(order) || containsOrderRecursive(queue, order);
        queue.add(current);
        return found;
    }

    public static void main(String[] args) {
        OrderQueue orderQueue = new OrderQueue();
        orderQueue.addRegularOrder("Order 1");
        orderQueue.addRegularOrder("Order 2");
        orderQueue.addPriorityOrder("Order 3");
        orderQueue.addPriorityOrder("Order 4");
        orderQueue.displayOrders();
        System.out.println("Processing order: " + orderQueue.processOrder());
        orderQueue.displayOrders();
        System.out.println("Removing order 2: " + orderQueue.removeOrder("Order 2"));
        orderQueue.displayOrders();
        System.out.println("Contains order 3: " + orderQueue.containsOrder("Order 3"));
        System.out.println("Contains order 4: " + orderQueue.containsOrder("Order 4"));
        System.out.println("Removing order 3: " + orderQueue.removeOrder("Order 3"));
    }
}
