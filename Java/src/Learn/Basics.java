package Learn;
/**
 * Created by drake on 7/29/17.
 */

import java.util.InputMismatchException;
import java.util.Scanner;
public class Basics {
    public static void main(String args[]){

        //TODO ===== Data Types =====
        System.out.println("===== Data Types =====");
        System.out.println("Hello World");

        // Basic variables
        //String emoji = 'July 28';
        byte Byte1 = 1;             // 8bit -- -128 - 127 , 0 , useful to save memory when it's important
        short Short1 = 2;           // 16bit -- -32,768 - 32,767 , 0 ,
        int Interger1 = 28;         // 32bit -- -2^32 - 2^32-1 , 0 ,
        long Long1 = 666L;          // 64bit -- -2^63 - 2^64-1 , 0L , used for very big numbers
        float Float1 = 666.6f;      // 32bit -- 3.4e+038 , 0.0f ,
        double Double1 = 28.0d;     // 64bit -- 1.7e+308 , 0.0d , use this one the most
        char Char1 = 'h';           // 16bit -- '\u0000' -  '\uffff' (or 65,535 inclusive) , '\u0000' ,
        boolean Boolean1 = true;    // 1bit information, but size unknown , false , true/false
        String String1 = "Emoji Movie, July 28!";
                                            // xbit -- x - x , null , String can contain almost anything, ascii
        // / Print variable
        System.out.println(Interger1);

        // Declaring Variables
        int int1 = 1, int2 = 2;
        // this declares multiple int variables

        String str1, str2;
        //private String str3; String str4;
        // make private variables
        String str5; int int3;
        str1 = str2 = "Lol";
        // this creates two String vars and then sets str1 equal to str2 which is ewal to "Lol"



        // --- More Complicated Data Types ---
        // Arrays

        int[] intArray1;
        // Integer array, can only hold integers

        // Go to Basic Concepts for more, and array methods


        //TODO ===== User Input =====
        // go to Java_Utils file for more on Scanner module

        System.out.println("===== User Input =====");

        Scanner usrInp = new Scanner(System.in);
        // you need to import the Scanner module to get user input from console. then this code makes a new object to catch the data and puts into a var if so choose

        System.out.print("Input something > ");
        String usrInput1 = usrInp.nextLine();
        // calls Scanner object to get data and then prints said data on new line
        // this gets user input and stores in usrInput1 String variable to be called later
        System.out.println(usrInput1);

        System.out.print("Input Integer please > ");
        double usrInputInt1 = usrInp.nextInt();
        // depending on what input you're asking for and going to get you can use the corresponding type with nextLine, nextInt, nextDouble, etc




        // ----- if/else & Switch -----


        System.out.println("----- if/else & Switch -----");

        // --- simple if/else statement ---
        boolean ifVar = true;
        if (true == ifVar){
            System.out.println("ifVar is True");
        } else {
            System.out.println("ifVar is False");
        }



        if (ifVar) {System.out.println("ifVar is True, still"); }
        // this shows you can do things on one line, but probably shouldn't since it doesn't look very good
        // and if you want to check if a boolean var is true you don't need var == true, just put the var name in () of the statement
        // and since this if statement doesn't have an else it'll just do nothing if not true


        boolean ifVar2 = false;

        if (ifVar && ifVar2) {
            System.out.println("Both are True");
        }
        // this checks if both are true, if ifVar and ifVar2 are True then ...
        if (ifVar || ifVar2) {
            System.out.println("At least One is True");
        }
        // one or both are true works, if ifVar or ifVar2 is True then ...

        if (!ifVar2) {
            System.out.println("ifVar2 is False");
        }
        // the ! means opposite, so if ifVar2 not True then ...


        // --- Nested if/else ---
        int ifVar3 = 15;
        if (1 < ifVar3){
            System.out.println("Bigger then 1");
            if (10 < ifVar3){
                System.out.println("Bigger then 10");
            }
        }



        // --- if/else if/else ---
        int ifVar4 = 1;
        if (1 == ifVar4){
            System.out.println("One");
        }
        else if (2 == ifVar4) {
            System.out.println("Two");
        }
        else if (3 == ifVar4) {
            System.out.println("Three");
            System.out.println("...");
        }
        else {
            System.out.println("Unknown");
        }
        // if one of the if statements is true and runs then it doesn't check the others


        // --- Switch Statement ---
        System.out.println("----- Switch Statement -----");
        int switchVar1 = 1;

        switch (switchVar1){
            case 1: System.out.println("One");
            break;
            // checks if var is 1 then runs this code
            case 2:
                System.out.println("Two");
            break;
            // the break just means to stop looking at the other cases if already found matching
            case 3:
                System.out.println("Three");
                System.out.println("...");
            break;
            //  the above example just shows more compact way if you don't have a lot of code
            default: System.out.println("Unknown");
            break;
            //  this will run if it doesn't mach any of the cases
        }



        // --- Conditionals & Conditional Statements ---
        System.out.println("----- Conditional Statements -----");


        int a = 4, b = 5;
        boolean result;
        result = a < b;             // true
        result = a > b;             // false
        result = 4 >= a;            // a smaller or equal to 4 - true
        result = 6 <= b;            // b bigger or equal to 6 - false
        result = a == b;            // a equal to b - false
        result = a != b;            // a is not equal to b - true
        result = a > b || a < b;    // Logical or - true
        result = (3 < a) && (a < 6);    // Logical and - true
        result = !result;           // Logical not - false
        a += b;                     // adds, same as a = a + b
        a *= b;
        a -= b;
        a /= b;
        a %= b;
        a++;                        // adds one after a
        ++a;                        // adds before
        b--;                        // Ex. .println(a++)  output >> 4
        --b;                        // .println(++a)  output >> 5

        String a1 = "Wow";
        String b1 = "Wow";
        String sameA1 = a1;


        boolean r1 = a1 == b1;      // This is false, since a and b are not the same object
        boolean r2 = a1.equals(b1); // This is true, since a and b are logically equals
        boolean r3 = a1 == sameA1;  // This is true, since a and sameA are really the same object

        boolean conditionalVar = true;
        System.out.println(conditionalVar ? "Var is True" : "Var is False");
        // prints one thing if variable is true and something else if false

        boolean conditionalVar2 = !conditionalVar;
        // makes this variable false if first variable is true and true of false
        System.out.println(conditionalVar2);
        // you could use, boolean conditionalVar2 = !conditionalVar
        // but this is just to show conditional statements


        //TODO ===== try/catch =====
        System.out.println("===== try/catch =====");
        Scanner usrInp2 = new Scanner(System.in);

        while (true) {
            try {
                System.out.print("try/catch | Input Integer Please > ");
                int usrInput2 = usrInp2.nextInt();
                System.out.println(usrInput2);
                break;
                // tries to run this code
            } catch (InputMismatchException e) {
                System.out.println("ERROR");
                usrInp2.next();
            }
            // if try code fails then this catches and runs code
        }



        //TODO ===== Looping =====
        System.out.println("===== Looping =====");

        // --- Simple While Loop ---
        System.out.println("--- Simple While Loop ---");

        int whileInt1 = 0;
        while (10 > whileInt1){
            System.out.print(whileInt1);
            whileInt1++;
        }
        System.out.println();
        // add spacing


        // --- Do While Loop ---
        System.out.println("--- Do While Loop ---");
        // this is similar to a while loop but it loops once before checking the statement to run or not

        int doWhileVar1 = 10;
        do {
            System.out.println(doWhileVar1);
            doWhileVar1++;
        } while (10 > doWhileVar1);



        // --- For Loop ---
        System.out.println("--- For Loop ---");

        for (int i = 0; 10 > i; i++) {
            System.out.println(i);
        }
        // (makes int var; loop while i < 10; add 1 each loop) { print i }

        // go to Basic concepts for more foreach loop. for (obj i: list) { }

        // --- foreach loop ---
        System.out.println("--- forach loop ---");
        Object[] objArr1 = {"Movie", "FGSP", 28, "Emoji", 2017.7};
        for (Object i:objArr1){
            System.out.println(i);
        }

        // --- break & continue ---
        System.out.println("--- break & continue ---");

        for (int i = 0; 10 <= i; i++){
            // loops until break, watch out using while loop like this, you might get an infinite loop
            System.out.println("Beginning Loop");
            // adds one to variable, if not then infinite loop.

            if (5 <= i) {
                System.out.println("STOPPING");
                break;
            }
            // checks statement, if true it stop the loop (breaks out of it)

            System.out.println("Middle");

            if (2 == i) {
                System.out.println("Skipping Loop :(");
                continue;
            }
            // checks statement, if true it'll instantly go to the next loop, won't run any code after the continue
            // if you're doing this with a while loop, watch where you put the i++; , since if it's after the continue it won't be able to change the number and it'll always equal 2
            System.out.println("End of Loop!");
        }



        //TODO ===== Importing =====
        System.out.println("===== Importing =====");

        secondFile secondFileObject = new secondFile();
        // this creates a new secondFile object in this main file, so you call and get data from the other file. basically treat as a class
        secondFileObject.printHi();





        //TODO ===== Math =====
        System.out.println("===== Math =====");


        System.out.println("Add 1+1: " + 1+1);
        System.out.println(("Sub 1-2: ") + (1-2));
        System.out.println(("Times 2*2: ") + 2*2);
        System.out.println(("Divide 10/2: ") + 10/2);
        System.out.println("Power 10^2: " + Math.pow(10, 2));
        System.out.println("Mod 10%3: " + Math.floorMod(10, 3));
        System.out.println("Floor 10//3: " + Math.floorDiv(10, 3));
        System.out.println("Floor 10//3: " + Math.floorDiv(10, 3));
        System.out.println("Abs -10: " + Math.abs(-10));
        System.out.println("Min 1,2: " + Math.min(1, 2));
        System.out.println("Max 1,2: " + Math.max(1, 2));
        System.out.println("sqrt 25: " + Math.sqrt(25));
        System.out.println("Ceil 1.5: " + Math.ceil(1.5));
        System.out.println("Round 1.5: " + Math.round(1.5));
        System.out.println("Random: " + Math.random());
        System.out.println("Pi: " + Math.PI);
        System.out.println("e: " + Math.E);
        System.out.println("e^pi*i: " + Math.pow(Math.E, (Math.PI * Math.sqrt(-1))));


        //TODO ===== Functions =====


        System.out.println("===== Functions =====");
        Basics.func1();
        Basics.func2("July", "28");


        // for more on functions and classes go to Basic Concepts or Advacne
    }

    public static void func1() {
        System.out.println("This is func1");
    }
    // simple function, no output(return (print is not output)) and can be called without making a instance, and it's public

    public static void func2(String fname, String lname){
        System.out.println("Hello " + fname + " " + lname);
    }
    // this takes two args and prints out.
    // you have to specify data type when making parameter, int varName, String varName, etc








}
