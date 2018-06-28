package Learn;


import java.io.*;
import java.text.*;
import java.util.*;
/*
This is for bigger projects and file.
Naming scheme
var int;  --  one word variable, lowercase
simpleVar String;  --  multi work variable, camelFormat
function();  --  function, same as variable, you'll know it's a function because it'll have ()
class Class1{}  --  classes, uppercase
class SimpleClass  --  classes, all uppercase
Intermediate_Advance_Simple_Class  --  long multi worded, using long words or lots of words, all uppercase and use _

ERROR
"ERROR: location | information"  --  error
"INFO: location | info" --  info
"WARNING: location | info"  --  warning
"NOTE: location | info"  -- note
these are for programs that you need outputs from, errors, info, warnings etc
 */


public class Intermediate {

    public static void main(String args[]) {
        LearnCollections LC = new LearnCollections();

    }
}


// you can't make methods(functions) outside of a class in a .java file. easiest thing to do is make a class and then use a constructor
// then just do FileClass FC = new FileClass();  and it'll work similar to the def __init__(self):  from python

//TODO ===== File I/O =====
class FileClass {
    private String filePath = "";
    private File file;


    public static void testSample() {
        String cDir = "/Users/drake/git/Learning/Java/src/Assets/";

        FileClass F1 = new FileClass();
        // create new FileClass object
        F1.setFile(cDir + "testFile2.txt");
        // sets the target file

        System.out.println("F1 Exists: " + F1.checkFile());
        //returns a boolean

        F1.createFile();
        // creates new file, WILL overwrite if already exists

        F1.readAllFile();
        // reads file, using BufferedRead and FileReader

        F1.appendFile("YOLO!!\n");
        // appends this to file, you might need to create new line here(when calling method) if you didn't have it set within the method

        F1._scannerRead();
        // prints out content of file with Scanner module


        F1.deleteFile();
        // deletes the file, WILL return boolean if successful
    }

    // sets the file
    public void setFile(String file) {
        try {
            this.filePath = file;
            this.file = new File(filePath);
        } catch (Exception e) {
            DTJO.printlnError("setFile.catch", "Can't set File : " + this.filePath);
        }
    }

    // check if it exists
    public Boolean checkFile() {
        return file.exists();
        // returns a true or false if the file exists or not
    }

    // read from file with FileReader
    public void readAllFile() {
        String currentLine;
        try {
            BufferedReader bReader = new BufferedReader(new FileReader(this.file.getAbsoluteFile()));  // this gets the absolute file and sets up reader
            System.out.print("File Content:\n");
            while (null != (currentLine = bReader.readLine()))
                DTJO.printlnOutput(currentLine);

            bReader.close();  // closes reader

        } catch (FileNotFoundException e) {
            DTJO.printlnError("readAllFile.catch", "File Not Found");
        } catch (Exception e) {
            DTJO.printlnError("readFile.catch", "Can't read file w/ bufferedReader");
        }
    }

    // append to file
    public void appendFile(String text) {
        try {
            BufferedWriter bWriter = new BufferedWriter(new FileWriter(this.file.getAbsoluteFile(), true));
            // similar to the overwriteFile method, but this fileWriter has the true parameter, so it appends not overwrite
            bWriter.write(text);
            // overwrites text to file, basically deletes all then writes to file, you can use \n, \t to make new lines and tabs etc
            bWriter.close();
            // close writer
        } catch (Exception e) {
            DTJO.printlnError("appendFile.catch", "Can't append to file");
        }
    }

    // create file

    public void createFile() {
        try {
            if (this.checkFile()) {
                DTJO.printlnBold("File Exists. Overwrite File?");
                // ask if want to overwrite existing file
                if (DTJO.askYesNo()) {
                    new Formatter(file);
                }
            } else {
                new Formatter(file);
            } // this checks if the file exists or not, if it does it'll print that this will overwrite it
        } catch (Exception e) {
            DTJO.printlnError("createFile.catch", "Can't create file");
        } finally {
            setFile(this.filePath);  // sets file, after creating
        }


    }

    // delete file
    public void deleteFile() {
        try {
            DTJO.printlnBold("Delete File : " + filePath);
            // asks if you want to delete file, saves to deleteAns
            if (DTJO.askYesNo())
                if (!this.file.delete())
                    DTJO.printlnError("deleteFiletry.if.if", "File Not Deleted");
            // checks if user says yes with DTJO.askYesNO() and then if file wasn't deleted prints error. file.delete() returns a boolean if file was deleted
        } catch (Exception e) {
            DTJO.printlnError("deleteFile.catch", "Couldn't delete File");
            // something went wrong
        }

    }

    // read from file with scanner
    public void _scannerRead() {
        Scanner scannerFile;
        try {
            scannerFile = new Scanner(file);
            System.out.print("Content of file:\n");
            while (scannerFile.hasNext())
                DTJO.printlnOutput(scannerFile.next());
            // prints out content of file line by line, you have ot use println or it'll print everything on one line

            scannerFile.close(); // you should put this under finally in a try/catch statement
            // closes scannerFile
        } catch (Exception e) {
            DTJO.printlnError("scannerRead.catch", "Scanner issue");
        }

    }

}

//TODO ===== Arrays, Lists, Collections, etc =====
class LearningCollections {
    public void LearningCollection() {
        DTJO.printSep2("Collections");

        String[] colorz = {"Red", "Blue", "Yellow", "Purple", "Black"};
        // when you initialize the String array, that's it you can't really add more to it, it's fixed
        System.out.println("colorz : " + Arrays.toString(colorz));
        // you have to use Arrays.toString() to print content of list to console, or it'll show its memory location

        List<String> colors = new ArrayList<>();
        // List<type> name = new ArrayList<type>(length); the length is not needed, unless you know what the exact length should/will be, you might run into errors if you try to exceed this
        // with this kind of array you can add as many items you want later on
        // need to add items to ArrayList

        for (String str : colorz) colors.add(str);

        System.out.println("colors : " + colors);
        // with Collections, you don't have to use the .toString() method

        List<String> colors2 = new ArrayList<>(Arrays.asList(colorz));
        // quicker way. you could also do .asList("item1", "Item2", "Three") also
        // you could also use colors2.addAll(Arrays.toList(colorz));  to add the data
        System.out.println("colors2 : " + colors2);


        // --- ---

        DTJO.printSep3("Two List to One");

        List<Integer> num1 = new ArrayList<>(Arrays.asList(1, 3, 4, 7, 9));
        List<Integer> num2 = new ArrayList<>(Arrays.asList(2, 4, 5, 7, 1));
        List<Integer> num3 = new ArrayList<>();

        for (int n : num1)
            if (num1.contains(n) && num2.contains(n))
                num3.add(n);

        for (int n : num1)
            if (num1.contains(n) && num2.contains(n))
                num3.add(n);


        Collections.sort(num1);
        Collections.sort(num2);
        Collections.sort(num3);
        // this just sorts the lists, lowest ot highest

        System.out.println("-----");
        System.out.println("num1 : " + num1);
        System.out.println("num2 : " + num2);
        System.out.println("num3 : " + num3);


        class editList {
            editList(Collection<Integer> list1, Collection<Integer> list2) {
                for (Integer i : list1) {
                    if (list2.contains(i)) list1.remove(i);
                }
                // if item from list2 is in list1 remove from list1
            }
        }

        // --- Linked Lists ---

    }
}

// Collections, ArrayList, linkedLIst, etc

// ----- Basics of Arrays -----
class BasicsArray {
    // ----- Array Basics -----
    public void basicsArray() {
        // ----- Declaring & Basic editing -----
        System.out.println("----- Basic Array stuff -----");


        String[] strArr1 = {"Emoji", "july"};           // string
        float[] floatArr1 = {1.5f, 50.5f};              // flat
        double[] doubleArr1 = {1.66, 8.9};              // double
        int[] intArr1 = {2017, 28, 7};                  // integer
        char[] charArr1 = {'k', 'i', 'r', 'b', 'y'};       // characters
        byte[] byteArr1;                                // byte
        boolean[] boolArr1 = {true, false, true, true}; // boolean
        Object[] objArr1 = {"Emoji", 28, 2017.7, 'l', 'o', 'l', true, false};  // everything

        int[] intArr2 = new int[10];  //int intArr1[]  also works
        // creates a new integer array with length of ten. you can not add or expand beyond this

        intArr2[0] = 1;
        intArr2[1] = 4;
        // setting variables

        int[] intArr3 = {1, 2, 3, 4};
        // creates a new array with length of four and with items in it

        // --- Multi-Dimensional ---
        System.out.println("Multi-Dimensional");
        int[][] deepIntArr1 = {{1, 2, 3}, {4, 5, 6}};
        // create array in array, works with all other types

        System.out.println(deepIntArr1[0][1]);
        // prints out 2


        // ----- For Loop Array -----
        System.out.println("--- For Loop Array ----");

        // go to theNewBoston for multi dimensional array looping

        int nums[] = {1, 2, 3};
        for (int i = 0; i < nums.length; i++) {
            int cItem1 = nums[i];
            // current Item, sets cItem1 to the item from nums list according to the loop number.
            // you should probably set the current item to the same as the list type, but if you don't know what you're getting or it's a object list, set it to, Object cItem = list[i];
            System.out.println(cItem1);
        }

        // - Quicker foreach way -
        System.out.println("- foreach loop -");
        for (int cItem2 : nums) {
            System.out.print(cItem2);
        }
        // same as above but shorter, cItem is kinda like a private var, only the loop can see it

        System.out.println();

        // - Quick way to print array data -
        System.out.println("nums array: " + Arrays.toString(nums));
        int[][] deepNums1 = {{1, 2, 3}, {7, 8, 9}};
        System.out.println("deepNums1 array: " + Arrays.deepToString(deepNums1));


        // --- Simple Table in Console ---
        System.out.println("--- Simple Table ---");
        System.out.println("Index\tValues");
        Object[] objData1 = {28, "July", "Emoji", 2017.7};
        for (int i = 0; i < objData1.length; i++) {
            System.out.println(i + "\t\t" + objData1[i]);
        }
        // i didn't use foreach, because I needed the loop number, so this was the easiest instead of making an outside variable then useing i++


        // --- Sum Int Array ---
        System.out.println("--- Sum of Int Array ---");
        int[] nums2 = {1, 2, 3, 4, 5};
        int nums2Sum = 0;
        for (int cItem3 : nums2) {
            nums2Sum += cItem3;
        }
        System.out.println("num2Sum: " + nums2Sum);
    }

    // ----- Array Methods -----
    public void ArrayMethods() {
        System.out.println("----- Array Methods -----");

        int[] intArray1 = new int[10];
        // a new integer array with length 10, means it can only hold 10 objects, from index 0 - 9

        String[] strArray1 = {"Emoji", "July", "Movie", "28", "FGSP"};
        // an array with just strings,

        System.out.println("intArray1 Length: " + intArray1.length);
        // printing array length

        intArray1[0] = 28;
        intArray1[1] = intArray1[0] + 2017;
        // sets value to position 0, then adds that value with 2017 and stores in position 1. you can't add outside of the range of what set to when created.
        System.out.println(intArray1[1]);

        Object[] objArray1 = {"Emoji", 28, "Movie", 2017.7, ":)"};
        // this can hold a mixed of data types
        System.out.println(Arrays.toString(objArray1));
    }
}

// ----- Collections -----
class LearnCollections{
    LearnCollections(){
        String[] strArr1 = {"Stuff", "More Stuff", "And EVEN MORE", "1", "4", "2", "6", "3", "1"};
        List<String> list1 = Arrays.asList(strArr1);

        Collections.sort(list1);  // sorts list
        // .sort(list, Collections.reverseOrder)  --  reverses order
        System.out.println(list1);  // prints content of list1
        System.out.println(strArr1);  // prints memory location of strArr1 not the content

        // creates a new String array; copy of strArr1 and new List
        String[] strArr1Copy = new String[strArr1.length];
        List<String> list1Copy = Arrays.asList(strArr1Copy);

        Collections.copy(list1, list1Copy);
        // copies list1 to list1Copy

        Collections.fill(list1, "LOL");
        // basically replaces all items to "LOL"

        Collections.reverse(list1);  // reverses list1

        private static void output(List<String> l){
            for (String i : l) System.out.println(i);
        }

    }
}
// ----- Linked Lists -----
class LearningLinkedLists {
     LearningLinkedLists() {

         String[] words1 = {"one", "two", "brown", "Uh", "lolz", "huh"};
         String[] words2 = {"Three", "five", "lul", "blah", "boooop", "beeep"};

         List<String> list1 = new LinkedList<>(Arrays.asList(words1));
         List<String> list2 = new LinkedList<>(Arrays.asList(words2));
         // adds words1,2 items to list1,2

         list1.addAll(list2);
         // combines list1 and 2

         list2 = null;
        // nulls list2, it's noting now


         DTJO.printlnBold("Normal: ");

         printMe(list1);
         // prints list1
         DTJO.printlnBold("RemoveStuff: ");

         removeStuff(list1, 2, 5);

         printMe(list1);
         // removes stuff from list1, from index to index
         DTJO.printlnBold("reverseMe: ");

         reverseMe(list1);
         // prints out data in reverse


         // Convert array to LinkedList and back
         String[] stringArr1 = {"Stuff", "Burger", "Fries", "Other stuff"};
         // basic String array
         LinkedList<String> lLString = new LinkedList<String>(Arrays.asList(stringArr1));
         // convert String array to Linked List
         lLString.add("More Stuff");
         lLString.addFirst("First!");  // adds item to beginning

         stringArr1 = lLString.toArray(new String[lLString.size()]);
         // converts back to array. replaces stringArr1 with new String list by getting the items fro lLString and size

         for(String x:stringArr1) System.out.println(x);
         // prints out stringArr1
         // in some if statements and for loops, you don't need {}
         

     }


    private void printMe(List<String> list) {
        System.out.println(list);
        // prints out list
    }

    private void removeStuff(List<String> list, int from, int to) {
        list.subList(from, to).clear();
        // gets subList of list and removes it
    }

    private void reverseMe(List<String> l) {
        Collections.reverse(l);
        System.out.println(l);
        // reverses data from list and prints it
    }

}

//TODO ===== String =====
class String_Stuff {
    public String Strings(String Str) {
        DTJO.printSep1("Strings");
        // ----- String Formatting -----
        DTJO.printSep2("String Formatting");

        String str_Format = String.format("Str input: %s", Str);
        System.out.println(String.format("%s | ", str_Format));
        // String.format, this is probably the easiest way to set as variable

        String messageFormat_Format = MessageFormat.format("Str input: {0}", Str);
        System.out.println("MessageFormat.format | " + messageFormat_Format);
        // you can also use this, this you can specify which item in {x}

        System.out.format(".out.format | Str input: %s\n", Str);
        // if you just want to print something you can use this. but you'll need a .println() or \n since it doesn't make a new line

        System.out.printf(".out.printf | Str input: %s\n", Str);
        // basically the same as .out.format()


        // ----- String Methods etc -----
        DTJO.printSep2("String Methods, Looping, etc");
        String str1 = "Hello World. How are you?!!?";
        String str2 = "hi";
        String str3 = "Hi";
        String str4 = "           hey hihihihihihi  byebyebyebye   lolol    kbye            "; // 12spaces, word, 1space, words, 2spaces, words , 3spaces, words, 4spaces, word, 3tabs
        // for most of this I'll use DTJO.println(); since it's quicker

        DTJO.println("str1 len : " + str1.length());
        // prints length of str1

        DTJO.println("str1 index(w) : " + str1.indexOf('e', 4));
        // shows index of letter from str1, the 4 means start from index 4, ignore the first 5 letters(0 is the start)
        // you can use parts of text with "text". not just one letter ''

        DTJO.println("str1 replace Hello > Bye : " + str1.replace("Hello", "Bye"));
        // replaces target letter/word with replacement arg. there isn't much of a difference in replace() and replaceAll()

        DTJO.println("str4 replace first match hi > uh : " + str4.replaceFirst("hi", "uh"));
        // will only replace the first matched

        DTJO.println("str1 all uppercase : " + str1.toUpperCase());
        DTJO.println("str1 all lowercase : " + str1.toLowerCase());
        // converts all to uppercase or lowercase

        DTJO.println("str4 removes spaces : " + str4.trim());
        // basically removes starting and ending spaces, nothing in between the words

        DTJO.printSep3("String Comparing");
        if (str2.equals(str1)) DTJO.println("str1 = str2");
        else DTJO.println("str1 != str2");
        // use a.equals(b) instead of a==b. case sensitive
        // in java comparing strings are different comparing other objects. to compare the actual text have to use .equals()

        if (str2.equalsIgnoreCase(str3)) DTJO.println("str2 = str3");
        else DTJO.println("str2 != str3");
        // this is so the comparing isn't case sensitive

        DTJO.printSep3("startsWith/endsWIth");
        String[] words = {"funk", "chunk", "furry", "beaconator"};

        for (String w : words)
            if (w.startsWith("fu")) DTJO.println(w + " : fu..");  // prints word(s) that starts with fu
            else if (w.endsWith("nk")) DTJO.println(w + " : ..nk");  // prints word(s) stat ends with nk
            else DTJO.println(w + " : ..");  // prints rest of words

        return (Str);
    }
}

//TODO ===== try/catch =====
class Exception_Stuff {
    public void tryCatch() {

        Scanner usrInp = new Scanner(System.in);
        while (true) try {
            DTJO.printUsrinp("Input first number");
            String num1 = usrInp.next();
            DTJO.printUsrinp("Input second number");
            String num2 = usrInp.next();
            System.out.printf("num1  num2 = %d\n", (Integer.parseInt(num1) / Integer.parseInt(num2)));
            break;
        } catch (InputMismatchException e) {
            DTJO.printlnError("tryCatch.catch", "Wrong input: Has to be a integer");
        } catch (Exception e) {
            DTJO.printlnError("tryCatch.catch", "Error dividing numbers");
        }
    }
}

//TODO ===== Functions =====
class Function_Stuff {
    // ----- Parameters & Arguments -----
    public static void para_Args() {
        // parameter is what you set when making a method, public void func1(int parameter1){}
        // argument is what you pass in when calling method, func1(argument1);
    }

    // if you don't know how much data will be thrown at function. you can use the ...
    public static void inputFunc1(int... nums) {
        // the ... is if you don't know how much input your going to get, you might have to do extra if you working with multi dimensional arrays or more
        System.out.println(Arrays.toString(nums));
    }

    // array input
    public static void inputArr(int[] nums) {
        // input a array of data
        for (int i : nums) System.out.println(i);
    }

    // --- Recursion ---
    public static int recursion(int x) {
        if (1 >= x) {
            System.out.println(x);
            return 1;
            // ends program if x is equal to 1
        } else {
            int n = x * recursion(x - 1);
            // takes the output of this function again with x-1 and * x
            System.out.println(n);
            return n;
        }
    }

}

//TODO ===== Class =====
class Class_Stuff {
    // ----- enum(enumeration) -----
    enum testEnum1 {

        emoji("yellow", "N/A"),
        booo("uhgg", "666"),
        kirby("cute", "25"),
        drake("mehm", "16"),
        per1("persin1", "1"),
        per2("person2", "2"),
        per3("person3", "3");

        private final String desc;
        private final String bDay;

        testEnum1(String description, String birthday) {
            this.desc = description;
            this.bDay = birthday;
        }

        public String getDesc() {
            return this.desc;
        }

        public String getYear() {
            return this.bDay;
        }


        public static void PrintThing() {
            System.out.println("Name:\tDesc:\tAge:");
            for (Class_Stuff.testEnum1 peeps : Class_Stuff.testEnum1.values()) {
                System.out.printf("%s\t%s\t%s\n", peeps, peeps.desc, peeps.bDay);
            }
        }

        /*
        System.out.println("range of constants\n");
        // need java.util/EnumSet
        for(testEnum1 peeps2: EnumSet.range(testEnum1.drake, testEnum1.kirby)){
            System.out.printf("%s\t%s\t%s \n", peeps2, peeps2.desc, peeps2.year);
            // most of the time you want to use x.getData() instead of getting the variable right-out
        }
    */
    }

    // go to OOP file. for more complex class and Object Oriented Programming. E.g. Multiple constructors, interfaces, implements, etc
// ----- Constructor -----
// a constructor method basically allow you to pass in args when creating new class instance
    class TestClass1 {

        private final String inputArg;

        TestClass1(String Something) {
            this.inputArg = Something;
        }

        public String getData() {
            return (this.inputArg);
        }
        // now when you call it like this, testClass1 classObj = new testClass1("TEXT");  , instead of blank testClass1();
        // similar to def __init__(self, Something):  in python


    }


    // ----- this. -----
    class ThisClass {
        // this. can be used for if you want to edit and access class variables from all class methods
        // go up to Constructor for the use of 'this' in those.
        // you don't need to use 'this' for keeping the data different between class instances like in python. so you don't have to call the class variable with 'this.' every time like in python, since in python 'self' means get data for this instance
    }

    // --- class var ---
    class TestClass2 {
        private int classVar1 = 1;

        public void setInt(int x) {
            this.classVar1 = x;
        }

        public void setInt2(int classVar1) {
            this.classVar1 = classVar1;
        }
        // this is one of the reason you might use 'this', it's also used in constructor and other things
        // it's much more important in python with self(which is not really the same but whatevs) since it's about scope in the class functions and class instance and other stuff.

    }

    // --- toString & this ---
    class TestClass3 {
        String str = "Hello";

        public TestClass3(String Str) {
            this.str = Str;
            System.out.printf("String is: %s\n", this);
        }
        // prints string, when you use 'this' it looks for

        public String toString() {
            return this.str;
        }


        public void func1() {
            System.out.println(this);
        }
    }

    // ----- Composition, using toString method -----
    class TestCallMe {
        private String cMstr1 = "From callMe class";

        public TestCallMe(String text) {
            this.cMstr1 = text;
            System.out.printf("str1 set to: %s | From callMe class\n", this);
        }

        public String toString() {
            return this.cMstr1;
        }
    }

    class TestHostClass {
        private final String hCstr1;
        private final TestCallMe cM;
        // this sets cM to the toString object from callMe class

        public TestHostClass(String data1, TestCallMe cMData) {
            this.hCstr1 = data1;
            this.cM = cMData;
            System.out.printf("hCstr1 set to: %s | cM set to: %s | From hostClass\n", data1, cMData);
        }
        // sets the variables from input, if you input a class object it'll try to get teh data from toString method

        public String toString() {
            return this.cM + " " + this.hCstr1;
        }
        // returns data when use 'this' in class, or if you use .println(classObject);

        public void printData() {
            System.out.printf("cM: %s | hCstr1: %s", this.cM, this.hCstr1);
        }
/*
        callMe cM = new callMe("HELLO");
        hostClass hC = new hostClass("WORLD", cM);
        // uses "WORLD" as arg 1 and cM as arg2, cM will be the data that callMe toString method returns
        System.out.println(hC);
        // prints the toString method from hostClass
*/
    }
}

//TODO ===== private/static/void/etc =====
class Data_States {
    // static
    static void staticFunc() {
        System.out.println("This is a Static Function");
    }
    // static means you don't need to make a instance of the object, or the parent class

    // non void
    static int returnIntFunc(int Int) {
        System.out.println(Int);
        return (Int);
        // this function will return data, printing is not returning data
        // if you don't have void you NEED a return statement. and you also need to specify what the function is returning
        // static String strFunc() , static double doubleFunc() , static boolean boolFunc() , etc

    }

    // non static
    void nonStaticFunc() {
        System.out.println("This is NONE Static Function");
    }

    // void
    public void voidFunc1() {
    // this means this function will not RETURN anything, System outputs does not count
    }


    // public

    // private
}

// --- abstract class ---

abstract class testAbstract {
    // only works on classes, abstract makes it so you can't create an object of that class
    // you can still have child classes and object of those, and can still use polymorphism, just can't create a object directly of the class
    final String str1 = "str1, Hello there ";

    public void printHI() {
        System.out.println("HI, from testAbstract");
    }
}

class testAbstractChild extends testAbstract {
    public void printHI2() {
        System.out.println(this.str1);
    }
        /*
        testAbstract tA = new testAbstractChild();
        tA.printHI();
        testAbstractChild tAC = new testAbstractChild();
        tAC.printHI2();

        //testAbstract tA = new testAbstract();
        // this won't work
        */
}


// using static on class variables
class testStaticClass {
    private static int members;
    private final String first;
    private final String last;
    // this makes it so the variable 'members' is the same across all instance/objects

    public testStaticClass(String firstName, String lastName) {
        this.first = firstName;
        this.last = lastName;
        testStaticClass.members++;
        System.out.printf("Welcom %s %s!!!\n", this.first, this.last);
    }

    public static int getMembers() {
        return testStaticClass.members;
    }

    public void printMembers() {
        System.out.printf("Number of members: %s\n", testStaticClass.members);
    }

    public String getFirst() {
        return this.first;
    }

    public String getLast() {
        return this.last;
    }
    //    testStaticClass tS = new testStaticClass("Drake", "Thomas");
//    testStaticClass tS2 = new testStaticClass("Kirby", "Pink");
//    testStaticClass tS3 = new testStaticClass("Emoji", "Yellow");
//    // add three people to the club, they're there own objects, they don't see each other except for the static 'members' variable
//    tS.printMembers();
//    // even though you made more object after tS, the static variable still gets updated for all. this should be 3

}






