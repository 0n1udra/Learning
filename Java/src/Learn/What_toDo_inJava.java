package Learn;

import javax.swing.*;

public class What_toDo_inJava {
}


//TODO ===== Prallel Arrays vs Classes =====
//http://www.dreamincode.net/forums/topic/147196-moving-away-from-parallel-arrays/
class Item{

    /*notice how each attribute is contained within the class.
      by doing this, we don't have to worry about mismatching
      the attributes as seen in parallel arrays
     */
    private int quantity;
    private double price;
    private String name;

    /*
      when the class is created, the constructor is invoked.
      this specific constructor allows for the specification of
      each attribute upon the creation of the object
     */
    public Item(String name, int quantity, double price){
        //initialize the attributes
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    /*
      This constructor simply creates a default item
      with a generic name, none in stock and no price set.
      It calls the other Item() constructor through the use of
      the keyword this
    */
    public Item(){
        this("New Item",0,0);
    }

  /*
	Basic getter and setter methods for each attribute
  */

    public void setName(String name){this.name = name;}
    public String getName(){return name;}

    public void setPrice(double price){this.price = price;}
    public double getPrice(){return price;}

    public void setQuantity(int quantity){this.quantity = quantity;}
    public int getQuantity(){return quantity;}

  /*
   this setter method is a little more advanced. it is designed to allow for an easy
   update of the item by passing a param representing the attribute to update and the
   new value.
   @params:
	  -int category: 1- Name, 2- Quantity, 3- Price
	  -String value: represents the new value; will be parsed to appropriate type
  */

    public void update(int category, String value){
        switch(category){
            case 1:
                name = value;
                return;
            case 2:
                //value is converted to an int
                quantity = Integer.parseInt(value);
                return;
            case 3:
                //value is converted to a double
                price = Double.parseDouble(value);
                return;
        }
    }
    /*
      This toString() method makes it very easy to get formatted information about the
      Item rather than having to go through each of the getter methods individually.
      Returns name, quantity and price separated by tabs
    */
    public String toString(){
        return name + "\t" + quantity + "\t" + price;
    }

}


class Inventory{
    public static void main(String[] args){
        //notice how we only use one array instead of 3
        //and that the array type is the same as class name
        //for Item
        Item[] inventory = new Item[10];

        boolean toContinue = true;
        String input = "";
        int menuItem = 0;
        int counter = 0;

        while(toContinue){
            input = JOptionPane.showInputDialog("1) Add an item\n2) Modify an existing item\n3) Display inventory\n4) Exit");
            menuItem = Integer.parseInt(input);
            switch(menuItem){
                case 1: //add an item
					/*
					 as we see here, we still need to get the input for each attribute
					 but we eliminate a few lines where we had to update each parallel array.
					 instead, we just create a new Item, and increment the counter in the same
					 statement. counter++ will execute after the item has been created in the
					 current index of counter. so if counter = 0, a new Item will be created
					 at inventory[0], then counter increments to 1.
					 */
                    String name = JOptionPane.showInputDialog("Enter the name of the item");
                    int quantity = Integer.parseInt(JOptionPane.showInputDialog("Enter the quantity of the item"));
                    double price = Double.parseDouble(JOptionPane.showInputDialog("Enter the price"));
                    inventory[counter++] = new Item(name, quantity, price);
                    break;

                case 2: //modify an existing item
                    int index = Integer.parseInt(JOptionPane.showInputDialog("Which item from 0-9 do you wish to modify?"));

                    //notice how we just call the toString() method instead of having a line to set up the String display
                    int category = Integer.parseInt(JOptionPane.showInputDialog(inventory[index].toString() + "\nModify:\n1) Name\n2) Quantity\n3) Price"));
                    String value = JOptionPane.showInputDialog("Enter the new value");

                    //notice how we use the update() method from the given Item and let it update its attributes internally
                    //rather than messing around with determining what parallel array to update and how to parse the values
                    inventory[index].update(category, value);
                    break;

                case 3: //display items
                    //notice how many fewer lines this takes up than iterating through each parallel array
                    //and appending the information to the display String
                    //Here, the toString() method comes in handy, plus having one array makes the task easier
                    //So we have about 4 lines of code for this part total
                    String display = "Name\tQuantity\tPrice\n";
                    for(Item i: inventory){
                        if(i != null)
                            display += i.toString() + "\n";
                    }
                    JOptionPane.showMessageDialog(null, display);
                    break;

                case 4: //exit
                    System.exit(0);
            }//end switch

        }//end while
    }
}


class Inventory_1{
    public static void main(String[] args){
		  /*
			 As we can see, we are starting out with 3 parallel arrays representing quantity, price, and name.
			 Each element in an array lines up with the elements at the corresponding indices in the other two arrays.
			 So quantity[0] represents the same item as price[0] and name[0]
		  */
        int[] quantity = new int[10]; //quantity defaults to 0 for all items
        double[] price = new double[10]; //price defaults to 0 for all items

        //names default to null, so we can't use an item's name until it is assigned one
        String[] name = new String[10];

        boolean toContinue = true;
        String input = "";
        int menuItem = 0;

        //holds place so when elements are supposed to be added, the appropriate indices are updated
        int counter = 0;

        while(toContinue){
            input = JOptionPane.showInputDialog("1) Add an item\n2) Modify an existing item\n3) Display inventory\n4) Exit");

            menuItem = Integer.parseInt(input);
            switch(menuItem){
                case 1: //add an item
                    name[counter] = JOptionPane.showInputDialog("Enter the name of this item");
                    quantity[counter] = Integer.parseInt(JOptionPane.showInputDialog("Enter the quantity available for this item"));
                    price[counter] = Double.parseDouble("Enter the price of this item");
                    counter++; //go to the next position
                    break; //jump out of the switch

                case 2: //modify existing item
                    //pick the item
                    int index = Integer.parseInt(JOptionPane.showInputDialog("Which item from 0-9 do you wish to modify?"));

                    //set up the display for the item
                    String item = "Name: " + name[index] + "\nQuantity: " + quantity[index] + "\nPrice: " + price[index];

                    //prompt for category to update
                    int category = Integer.parseInt(JOptionPane.showInputDialog(item + "\nModify:\n1) Name\n2) Quantity\n3) Price"));

                    //and effect the update
                    if(category == 1) name[index] = JOptionPane.showInputDialog("Enter a new name");
                    else if(category == 2) quantity[index] = Integer.parseInt(JOptionPane.showInputDialog("Enter a new quantity"));
                    else if(category == 3) price[index] = Double.parseDouble(JOptionPane.showInputDialog("Enter a new price"));
                    break;
                case 3: //display items
                    String display = "";
                    for(int i = 0; i < name.length; i++){
                        //if there isn't a name for an item, we won't display it
                        if(name[i] == null) break;
                        display += name[i] + "\t" + quantity[i] + "\t" + price[i] + "\n";
                    }
                    //if there are no items in inventory, display such
                    if(display.trim().length() != 0) JOptionPane.showMessageDialog(null, "There are no items in inventory");

                        //otherwise, display what is in inventory
                    else JOptionPane.showMessageDialog(null,"Name\tQuantity\tPrice\n" + display);
                    break;
                case 4: //exit
                    System.exit(0);
            }
        }

    }
}




