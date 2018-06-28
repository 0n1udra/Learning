package Other;

public class People {
}


// =====

class people {
    private final Person[] pList1 = new Person[10];
    // creates a person object list to store person objects in
    private int i;
    // counter, this is so not to over fill the list

    public void add(Person a) {
        if (this.i < this.pList1.length) {
            // makes sure you're not over the list size
            this.pList1[this.i] = a;
            System.out.println(a + " : Person added to index: " + this.i);
            this.i++;
            // prints it's been added, and adds 1 to i
        }
    }
    // adds a item to the lsit

    public void printList() {
        for (Person p : this.pList1) {
            System.out.println(p);
        }
    }
    // prints all of the objects in the list. this will print out the toString method from the person super class.

    public void addSeveral(Person[] items) {
        for (Person p : items) {
            if (this.i < this.pList1.length) {
                this.pList1[this.i] = p;
                this.i++;
            }
            else { System.out.println("pList1 FULL");  }
        }
    }
    // this is so you can add multiple items at once, using a person list to add to this list



}
// this class if here to store all the person objects in a list, and you can also batch execute and do stuff


abstract class Person {
    // this is an abstract class because you don't need to make a person object directly use one of the sub classes.
    protected String
            first = "FIRST",          // first name
            middle = "MIDDLE",        // middle name
            last = "LAST",            // last name

    desc = "DESCRIPTION",     // description
            race = "RACE",            // race (Asian)
            specialty = "SPECIALTY",  // specialty (Coder)
            level = "LEVEL",          // level of specialty (Advance)
            etc = "ETC",              // any other detail (Asshole)

    phone = "(000)-000-000",  // phone # ( (000)-000-000

    street = "000",           // street address (123 main st)
            city = "CITY",            // city (Sandwon)
            state = "STATE",          // state (NH)
            country = "COUNTRY";      // country (America)

    protected String[]
            likes;

    protected int
            age,              // age (years)
            weight,           // weight (lbs)
            height,           // height (in)

    zip;              // zip code
    // setting all the variables

    Person(String firstName, String lastName, int Age) {
        this.first = firstName;
        this.last = lastName;
        this.age = Age;
    }
    // this function itself will never be used directly but needs to be here so you can use super() in the sub classes

    public void printAllData() {
        System.out.printf("Name | %s %s %s\n", this.first, this.middle, this.last);
        System.out.printf("Body | %sy : %slbs : %sin\n", this.age, this.weight, this.height);
        System.out.printf("Addr | %s %s %s %s %s \n", this.street, this.city, this.state, this.country, this.zip);
        System.out.printf("Misc | %s : %s : %s\n", this.phone, this.race, this.etc);
        System.out.printf("Desc | %s\n", this.desc);
    }
    // prints all the data on person

    public void printBasicData(){
        System.out.println("NotImplemented");
    }
    // prints only the basics


    @Override
    public String toString() {
        return this.first + " " + this.last;
    }
    // this is what it'll return if you try to get a string from a person object, like using .println(personObj);
}


class Programmer extends Person {

    Programmer(String firstName, String lastName, int Age, String specialty, String level) {
        super(firstName, lastName, Age);
        this.specialty = specialty;
        this.level = level;
    }
    // gets data for a programmer person object

    public void printProData() {
        System.out.printf(" Person  | %s %s : %sy\n", this.first, this.last, this.age);
        System.out.printf("Specialty | %s %s\n", this.level, this.specialty);

    }
    // prints data tailored for a programmer person object
}


class RegularPerson extends Person {

    RegularPerson(String firstName, String lastName, int Age, String[] interests) {
        super(firstName, lastName, Age);
        this.likes = interests;

    }

    public void printRegPersonData() {
        System.out.printf("  Person  | %s %s\n", this.first, this.last);
        System.out.printf("Interests | %s\n", this.likes);
    }
}


class Gamer extends Person{
    private final String[] favGames;

    Gamer(String firstName, String lastName, int Age, String[] favoriteGames) {
        super(firstName, lastName, Age);
        this.favGames = favoriteGames;

    }
    // you can input a list of favorite games to store

    public void printGamerData(){
        System.out.println("GAMES: " + this.favGames);
    }



}
/*
person drakeT = new programmer("Drake", "Thomas", 16, "Coder", "New");

        String[] games = {"LoL", "Overwatch"};
        gamer gaelanC = new gamer("Gaelan", "Carman", 17, games);

        String[] brainTLikes = {"TV", "Stuff"};
        // since you can't input an array directly into a method, because you need to init it. so this creates one to pass in.
        regularPerson brianT = new regularPerson("Brian", "Thomas", 50, brainTLikes);

        drakeT.printAllData();
        gaelanC.printGamerData();
        brianT.printRegPersonData();



        System.out.println("-----------------");
        people peoples = new people();
        // create people object
        person[] pList= {drakeT, brianT, gaelanC};
        // this creates a person list to pass into addServeral method
        peoples.addSeveral(pList);
        // passes in person list
        pList = null;
        // deletes the array, removes it since it's in the people's array. and it can save memory.
        peoples.printList();
        // prints all the object toString return data.
    }
 */