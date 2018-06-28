package Other; /**
 * Created by drake on 7/29/17.
 */

import java.io.IOException;
import java.util.*;
import java.util.logging.*;

public class Java_Utils {

    public static void main(String args[]) {
        Logging_Class lC = new Logging_Class();
    }

    public static void Random() {
        // --- java.util.Random ---
        // Random integer number generator
        Random rand = new Random();
        int randNum;

        for (int i = 1; 10 >= i; i++) {
            randNum = rand.nextInt(6);
            System.out.println(randNum + " ");
        }

    }


    public static void Scanner(){
        // --- java.util.Scanner ---
        // Scanner is used to get input from console
        Scanner usrInput = new Scanner(System.in);

        // Integer Input
        System.out.print("Input Integer > ");
        int usrIntInp1 = usrInput.nextInt();
        System.out.println();

        // String Input
        System.out.print("Input String > ");
        String usrStrInp1 = usrInput.next();
        System.out.println();

        // Double Input
        System.out.print("Input Double > ");
        double usrDoubInp1 = usrInput.nextDouble();
        System.out.println();

        // Boolean Input
        System.out.print("Input Boolean > ");
        boolean usrBoolInp1 = usrInput.nextBoolean();
        System.out.println();

        System.out.println(usrIntInp1);
        System.out.println(usrStrInp1);
        System.out.println(usrDoubInp1);
        System.out.println(usrBoolInp1);
    }

    //TODO ===== Arrays =====
    public static void Arrays(){

        // java.util.Arrays;

        // ----- Sets -----
        int[] arr = {1,2,1,2,1,4,1,5,6,1,2,1};
        // an array
        Set<Integer> set = new HashSet<Integer>();
        // makes a new blank set

        for (int anArr : arr) {
            set.add(anArr);
        }
        // adds items from arr to set

        Iterator it = set.iterator();
        while(it.hasNext()) {
            System.out.println(it.next());
        }
        // prints item from set
    }

    //TODO ===== Logging =====
    static class Logging_Class{
        private static final Logger LOGGER = Logger.getLogger(Logging_Class.class.getName());

        Logging_Class() {
            LogManager.getLogManager().reset();
            // resets any root logging handler


            FileHandler FH = null;
            try {
                FH = new FileHandler("File_Class_LOG.log");
                FH.setLevel(Level.ALL);
                LOGGER.addHandler(FH);
            } catch (IOException e) {
                e.printStackTrace();
            }


            ConsoleHandler CH = new ConsoleHandler();
            CH.setLevel(Level.WARNING);
            LOGGER.addHandler(CH);

            LOGGER.setLevel(Level.ALL);
            // sets the level of log info that'll be outputted to console, so anything FINE and above will be, anything below won't be seen in console just the log file
            //SEVERE, WARNING, INFO, CONFIG, FINE, FINER, FINEST, ALL, OFF

            LOGGER.info("My First log");

            
        }
    }

}
