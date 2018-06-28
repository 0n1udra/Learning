import java.util.*;
public class test{

    public static void main(String[] args){

        Scanner usrInp = new Scanner(System.in);
        String inpName; String inpStr;
        System.out.print("Your Name > ");
        inpName = usrInp.next();
        System.out.print("Your String > ");
        inpStr = usrInp.next();
        recall(inpName, inpStr);

    }


    static void recall(String name, String Str){
        System.out.printf("Hello %s you said: %s\n", name, Str);
    }
}
