package Learn;
/**
 * Created by drake on 7/29/17.
 */
public class secondFile {
    public void printHi() { System.out.println("Hi! From secondFile class");
    }
}



// these classes are called concrete classes, since they are specific and not general. the food class is an abstract class
class hamburger extends food{
    public void eat(){
        System.out.println("Hamburgers are OK!");

    }
    // this overrides the parent food class eat methods, to override it has to have the same parameters, if this one is different that overloading not overriding
}
class dumpling extends food{

    public void eat(){
        System.out.println("Dumplings are yummy!");

    }
    // overrides food's eat method, doesn't touch hamburger's

}

class fatty{
    public void digest(food x){

        x.eat();
        System.out.println("Just ate food.");
//
//        food foods[] = new food[2];
//        foods[0] = new dumpling();
//        foods[1] = new hamburger();
//
//
//        for(int x=0; x<foods.length; x++){
//            foods[x].eat();
//
//        }
//
//        fatty fat = new fatty();
//        for (food x: foods){
//            fat.digest(x);
//        }
//
//        // same as > for (int x=0; x<foods.length; x++){ fat.digest(foods[x]); }

    }

}

class Dog extends Animal{
    public void noise(){
        System.out.println("Annoying dog bark!");
    }
}

class Fish extends Animal{
    public void noise(){
        System.out.println("Fish noise....?");
    }
}



