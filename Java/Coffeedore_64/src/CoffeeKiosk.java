import java.util.ArrayList;

public class CoffeeKiosk {
    private ArrayList<Item> menu;

    public CoffeeKiosk() {
        this.menu = new ArrayList<>();
    }

    public void addMenuItem(String name, double price) {
        Item item = new Item(name, price);
        menu.add(item);
    }

    public void newOrder() {
        Order order = new Order();
        order.addItem(menu.get(0)); // Add a sample item to the order
        order.display();
    }
}
