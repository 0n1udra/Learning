package DT;
import java.util.*;
        
public class Java_Output{
    public static final String RESET = "\u001B[0m";
    public static final String BLACK = "\u001B[30m";
    public static final String RED = "\u001B[31m";
    public static final String GREEN = "\u001B[32m";
    public static final String YELLOW = "\u001B[33m";
    public static final String BLUE = "\u001B[34m";
    public static final String PURPLE = "\u001B[35m";
    public static final String CYAN = "\u001B[36m";
    public static final String WHITE = "\u001B[37m";

    public static final String BOLD = "\033[0;1m";
    public static final String UNDERLINED = "\033[0m";

    public static final String BLACK_BG = "\u001B[40m";
    public static final String RED_BG = "\u001B[41m";
    public static final String GREEN_BG = "\u001B[42m";
    public static final String YELLOW_BG = "\u001B[43m";
    public static final String BLUE_BG = "\u001B[44m";
    public static final String PURPLE_BG = "\u001B[45m";
    public static final String CYAN_BG = "\u001B[46m";
    public static final String WHITE_BG = "\u001B[47m";


    /*
    Red = Error
    Yellow = Info
    Purple = Warning
    Blue = Note
    Cyan = Output (e.g. file output to console)
    Green = User interaction (input)
    
     */
    // print new line

    public static void println(Object obj){
        Java_Output.println(String.valueOf(obj),"", ""); }

    public static void printSep1(Object obj){ System.out.printf("=====%s=====" + Java_Output.RED_BG + Java_Output.RED + ".\n" + Java_Output.RESET, String.valueOf(obj)); }
    // prints, =====text=====, with yellow banner

    public static void printSep2(Object obj){ System.out.printf("-----%s-----" + Java_Output.YELLOW_BG + Java_Output.YELLOW + ".\n" + Java_Output.RESET, String.valueOf(obj));}
    // prints, -----text-----, with yellow banner

    public static void printSep3(Object obj){ System.out.printf("---%s---" + Java_Output.BLUE_BG + Java_Output.BLUE + ".\n" + Java_Output.RESET, String.valueOf(obj)); }
    // prints, ---text---, with blue banner

    public static void println(Object data, String fg, String bg){ System.out.println(String.valueOf(data) + Java_Output.RESET); }
    // prints on new line

    public static void printlnInfo(Object location, Object info){ System.out.printf(Java_Output.YELLOW + "INFO: %s | %s\n", String.valueOf(location),  String.valueOf(info) + Java_Output.RESET); }
    // prints in Yellow. "INFO: location | info"

    public static void printlnWarning(Object location, Object info){ System.out.printf(Java_Output.PURPLE + "WARNING: %s | %s\n", String.valueOf(location), String.valueOf(info) + Java_Output.RESET); }
    // Purple Warninf
    public static void printlnError(Object location, Object info){ System.out.printf(Java_Output.RED + "ERROR: %s | %s\n", String.valueOf(location), String.valueOf(info) + Java_Output.RESET); }
    // Red Error

    public static void printlnNote(Object location, Object info){ System.out.printf(Java_Output.BLUE + "NOTE: %s | %s\n", String.valueOf(location), String.valueOf(info) + Java_Output.RESET); }
    // Blue Notes

    public static void printlnOutput(Object obj){System.out.println(Java_Output.CYAN + String.valueOf(obj) + Java_Output.RESET);}
    // Cyan, output from input

    public static void printlnUsrinp(Object obj) { System.out.println(String.valueOf(obj) + Java_Output.GREEN + " > " + Java_Output.RESET); }
    // Green. asking for input

    public static void printlnBold(Object obj) { System.out.println(Java_Output.BOLD + String.valueOf(obj) + Java_Output.RESET); }

    public static void printlnUnderL(Object obj) { System.out.println(Java_Output.UNDERLINED + String.valueOf(obj) + Java_Output.RESET);}
    //==========================

    // print, same as above but doesn't print new line
    public static void print(Object obj){
        Java_Output.print(String.valueOf(obj),"", ""); }

    public static void print(Object data, String fg, String bg){ System.out.print(String.valueOf(data) + Java_Output.RESET); }

    public static void printInfo(Object location, Object info){ System.out.printf(Java_Output.YELLOW + "INFO: %s | %s\n", String.valueOf(location), String.valueOf(info)+ Java_Output.RESET); }

    public static void printWarning(Object location, Object info){ System.out.printf(Java_Output.PURPLE + "WARNING: %s | %s\n", String.valueOf(location), String.valueOf(info)+ Java_Output.RESET); }

    public static void printError(Object location, Object info){ System.out.printf(Java_Output.RED + "ERROR: %s | %s\n", String.valueOf(location), String.valueOf(info)+ Java_Output.RESET); }

    public static void printNote(Object location, Object info){ System.out.printf(Java_Output.BLUE + "NOTE: %s | %s\n", String.valueOf(location), String.valueOf(info)+ Java_Output.RESET); }

    public static void printOutput(Object obj){System.out.print(Java_Output.CYAN + String.valueOf(obj) + Java_Output.RESET);}

    public static void printUsrinp(Object obj) { System.out.print(String.valueOf(obj) + Java_Output.GREEN + " > " + Java_Output.RESET); }

    public static void printBold(Object obj) { System.out.print(Java_Output.BOLD + String.valueOf(obj) + Java_Output.RESET); }
    
    public static void printUnderL(Object obj) { System.out.print(Java_Output.UNDERLINED + String.valueOf(obj) + Java_Output.RESET);}

    // Other stuff

    private static final String[] yesStrings = {"Y", "y", "yes", "Yes", "YES"};
    private static final String[] noStrings = {"N", "n", "no", "No", "NO"};

    public static boolean askYesNo(){
        Scanner usrInp = new Scanner(System.in);
        Java_Output.printUsrinp("Yes/No");
        String yesNoAnswer = usrInp.next();
        return Arrays.asList(Java_Output.yesStrings).contains(yesNoAnswer);
    }

    











}
