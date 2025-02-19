public class Main {
    public static void main(String[] args) {
        Inventory inventory = new Inventory();
        Item item1 = new Item("Item 1");
        Item item2 = new Item("Item 2");
        Item item3 = new Item("Item 3");

        inventory.addItem(item1);
        inventory.addItem(item2);
        inventory.addItem(item3);

        System.out.println("Total items: " + inventory.getItemCount());
        inventory.displayItems();

        inventory.removeItem(item2);
        System.out.println("Total items: " + inventory.getItemCount());
        inventory.displayItems();

        if (inventory.hasItem(item3)) {
            System.out.println("Item 3 exists in inventory.");
        } else {
            System.out.println("Item 3 does not exist in inventory.");
        }

        inventory.removeItem(item2);

        if (inventory.hasItem(item2)) {
            System.out.println("Item 2 exists in inventory.");
        } else {
            System.out.println("Item 2 does not exist in inventory.");
        }

        System.out.println("Total items: " + inventory.getItemCount());
    }
}
