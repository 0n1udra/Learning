package Learn;
public class OOP {



    // ----- Multiple Constructors -----
    // you would have multiple constructors for different possible inputs
    public static class constructorClass{
        private int var1, var2, var3;

        public constructorClass(){
            this(0, 0, 0);
            System.out.println("Constructor 0");
        }
        public constructorClass(int x){
            this(x, 0, 0);
            System.out.println("Constructor 1");
        }
        public constructorClass(int x, int y){
            this(x, y, 0);
            System.out.println("Constructor 2");
        }
        public constructorClass(int x, int y, int z){
            this.run(x, y, z);
            System.out.println("Constructor 3");
        }

        public void run(int x, int y, int z){
            System.out.println(String.format("x: %d | y: %d | z: %d", x, y, z));
        }

        // the way this is setup, if you only input 1 arg it'll be x, you have to make set methods to set individual ones
        // in python you have kwargs which you can say which variable to set arg to :p
        //    constructorClass c1 = new constructorClass(1);        >>  x: 1 | y: 0 | z: 0
        //    constructorClass c2 = new constructorClass(1, 2);     >>  x: 1 | y: 2 | z: 0
        //    constructorClass c3 = new constructorClass(1, 2, 3);  >>  x: 1 | y: 2 | z: 3


    }


    // ----- Setting data, closes to Keyword Arguments -----
    // nicest way to set data by using methods instead of inputting all when making class object. closest(not close at all) to python keyword argument
    public static class setData{
        private int var1, var2, var3;
        // the data has to be set out here if you want to access the data everywhere else from the class. If they were declared in a method on that method will be-able to access it
        public void setVar1(int var1) { this.var1 = var1; }

        public void setVar2(int var2) { this.var2 = var2; }

        public void setVar3(int var3) { this.var3 = var3; }
        // set the different variables

        // you can have method to return each one also
        //public void getVar1(){ return var1; } ...

        public void printData(){
            System.out.print(String.format("%d : %d : %d", this.var1, this.var2, this.var3));
        }
        //    keywordArgs kwArg = new keywordArgs(){{
        //        setVar1(1);
        //        setVar3(3);
        //        printData();
        //    }};
        //        kwArg.setVar2(2);
        //        kwArg.printData();
        // this is how you would use it, not as easy as it is in python function(param=arg, param1=arg1...etc)

    }



    //TODO ===== Inheritance, Interface, Implements =====

    // ----- Extend -----
    // lets you basically have a parent class with certain attributes and they will be the same in the child classes
    // this works across files also. it's calls super class and sub class(s)
    public static class testParent{
        private final String parentVar = "This is a string from testParent!";
        // only testParent can access this, not even the child classes

        protected String protVar = "This string is protected";

        public String pubStr = "This string is public";
        // TODO: Find out the differences
        // This will be accessable anywhere, not just the parent and sub class

        String str1 = "str1, from testParent";


        public void printStr1(){
            System.out.println(this.str1);

        }
    }

    public static class testChild extends OOP.testParent{
        String str2 = "str2, from testChild Class";
        private int testChildInt;

        public void printStrs(){
            System.out.println(str1 + " | " + str2);
        }
    }

    public static class testSubChild extends testChild{
        String str3 = "str3, from testSubChild!!!";


        public void printStrs(){
            System.out.printf("%s | %s | %s\n", str1, str2, str3);
        }

        OOP.testParent testParentChild = new OOP.testSubChild();

//        testChild testChild = new testChild();
//        testChild.printStr1();
//        testChild.printStrs();
    }

    // ----- Interface -----
    interface Interface1{
        void method1();

        String str1();

    }

    public class C1 implements OOP.Interface1{
        @Override
        public String str1() {
            return "This is str1";
        }

        @Override
        public void method1() {
            System.out.println("From C1.method1, " + this.str1());
        }
    }
}



