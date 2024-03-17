import java.util.ArrayList;

class Item {
    String name;
    double price;

    // Constructor
    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    }
}

class Order {
    String name;
    ArrayList<Item> itemList;
    double total;
    boolean ready;

    // Constructor
    public Order(String name, ArrayList<Item> itemList) {
        this.name = name;
        this.itemList = itemList;
        this.total = 0.0;
        this.ready = false;
    }

    // Method to add item to order
    public void addItem(Item item) {
        itemList.add(item);
        total += item.price;
    }

    // Method to calculate total price
    public double calculateTotal() {
        return total;
    }

    // Getter for order name
    public String getName() {
        return name;
    }

    // Getter for order status
    public boolean isReady() {
        return ready;
    }

    // Method to set order status to ready
    public void setReady(boolean ready) {
        this.ready = ready;
    }
}

public class TestOrders {
    public static void main(String[] args) {
        // Create item variables
        Item item1 = new Item("mocha", 4.5);
        Item item2 = new Item("latte", 3.0);
        Item item3 = new Item("drip coffee", 2.0);
        Item item4 = new Item("cappuccino", 5.0);

        // Create order variables
        Order order1 = new Order("Cindhuri", new ArrayList<>());
        Order order2 = new Order("Jimmy", new ArrayList<>());
        Order order3 = new Order("Noah", new ArrayList<>());
        Order order4 = new Order("Sam", new ArrayList<>());

        // Print order1 variable
        System.out.println(order1);

        // Predicting order1.total will result in 0.0 as no items are added yet
        System.out.println("Order1 total: " + order1.calculateTotal());

        // Add item1 to order2's item list and increment the order's total
        order2.addItem(item1);

        // Noah ordered a cappuccino. Add the cappuccino to their order list and to their tab.
        order3.addItem(item4);

        // Sam added a latte. Update the order accordingly.
        order4.addItem(item2);

        // Cindhuri’s order is now ready. Update her status.
        order1.setReady(true);

        // Sam ordered more drinks - 2 lattes. Update their order as well.
        order4.addItem(item2);
        order4.addItem(item2);

        // Jimmy’s order is now ready. Update his status.
        order2.setReady(true);

        // Print order1 variable after modifications
        System.out.println(order1);
    }
}
