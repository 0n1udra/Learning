package Learn;

import com.sun.xml.internal.rngom.digested.DListPattern;

import java.util.*;
import java.util.concurrent.TimeUnit;

public class Advance {
    public static void main(String args[]){

    }

}

//TODO ===== Polymorphism =====

abstract class food{


    public abstract void eat();
    // this makes an abstract method, which means it HAS to be overridden. which is why it has no body
    // and you NEED the class to be abstract to make an abstract method, but you don't need an abstract method in an abstract class
    // you also NEED to have the eat method in all of the child classes of food class

    //    void eat(){ System.out.println("This is yummy"); }
    // a regular method, this can be overridden from it's sub classes

}


class dog_List{
    private final Dog[] theList = new Dog[5];
    // new dog object array that holds 5 items
    private int i;  //  counter

    public void add(Dog d){
        if (this.i < this.theList.length){
            // checks if we haven't exceeded i
            this.theList[this.i] = d;
            // adds add argument d to theList
            System.out.printf("%s : Added to index: %s\n", d, this.i);
            this.i++;
        }

//        dog_List dList = new dog_List();
//        Dog d = new Dog();
//        dList.add(d);
    }
}
// only holds dog objects


class Animal{

    public void noise(){
        System.out.println("This shouldn't be called!");
    }

//    Animal[] theList = new Animal[2];
//    Dog d=new Dog();
//    Fish f=new Fish();
//
//    theList[0]=d;
//    theList[1]=f;
//       for(Animal x:theList){
//        try { Thread.sleep(1000);  }
//        catch (InterruptedException e){ ; }
//        // this delays it
//        x.noise();
    }


class animal_List{
    private final Animal[] theList = new Animal[5];
    // this allows it so you can add any object to this list if the class has extends Animal on it
    private int i;
    public void add(Animal a){
        if(this.i < this.theList.length){
            this.theList[this.i] = a;
            System.out.println(a + " : Animal added to index: " + this.i);
            this.i++;
        }
        // you can add any animal object to this array, all you need is the extends Animal on the class
//        animal_List aList = new animal_List();
//        Dog d = new Dog();
//        Fish f = new Fish();
//        aList.add(f);
//        aList.add(d);
    }
}



