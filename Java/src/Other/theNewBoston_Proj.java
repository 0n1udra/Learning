package Other; /**
 * Created by drake on 7/30/17.
 */
import java.text.MessageFormat;
import java.util.*;

public class theNewBoston_Proj {
    public static void main(String args[]) {

        theNewBoston_Proj.timeClass_36 time = new theNewBoston_Proj.timeClass_36();
        time.printTime();
        time.setTime(1, 12, 13);
        time.print12Time();

        int[] Time = {12, 0, 50};
        time.setTImeWithArr(Time);
        System.out.println(time.returnTimeStr());
    }

    public static double simpleAveragingProgram() {
        Scanner input = new Scanner(System.in);

        int total = 0;
        int grade;
        int average;
        int counter = 0;
        // create needed variables

        while (10 > counter) {
            grade = input.nextInt();
            total = total + grade;
            counter++;

        }

        average = total / 10;
        System.out.println("Your average is " + average);
        return (average);
    }

    public static double simpleAveragingProgram2() {
        Scanner input = new Scanner(System.in);


        System.out.print("Input # of grades > ");
        int numGrades = input.nextInt();


        double[] grades = new double[numGrades];
        for (int i = 0; i < numGrades; i++) {
            System.out.print("Input grade > ");
            grades[i] = input.nextDouble();
        }
        double sum = 0.0;

        for (double i : grades) {
            sum += i;
        }
        double average = sum / grades.length;

        String Final = String.format("%1$d Grade, Average is : %2$.2f", numGrades, average);
        System.out.println(Final);
        System.out.println(average);

        return (average);


    }

    public static void arrayInMethod_32(int x[], int y) {
        for (int i = 0; i < x.length; i++) {
            x[i] += y;
            // goes through each item in list x, and adds y to each item
        }
        // demonstrates for loop as a method. arrayInMethod(list, number);


    }

    public static void tableMultiArray_34(int x[][]) {
        for (int row = 0; row < x.length; row++) {
            for (int col = 0; col < x[row].length; col++) {
                System.out.println(x[row][col] + "\t");

            }
            System.out.println();
        }
    }
    public static void tableMultiArray_34_2(int x[][]) {
        for (int[] aX : x) {
            for (int anAX : aX) {
                System.out.println(anAX + "\t");

            }
            System.out.println();
        }
    }
        // prints out deep arrays in columns and row,
        // int[][] x = {{1,2,3}, {4,5,6}}; tableMultiArray(x);



    public static class timeClass_36{
        private int hour, minute, second;
        // create individual variables for parts of the time
        private int[] fullTimeArr = {0, 0, 0};
        private String fullTimeStr = "00:00:00 Not Set";
        // these are mostly for returning and printing the time, there also have default values in case setTime didn't run

        public void setTImeWithArr(int[] time){
            this.setTime(time[0], time[1], time[2]);
        }
        // this is so you can set the time by inputting a int array

        public void setTime(int h, int m, int s) {
            this.hour = ((0 <= h && 24 > h) ? h : 0);
            this.minute = ((0 <= m && 60 > m) ? m : 0);
            this.second = ((0 <= s && 60 > s) ? s : 0);
            int [] fullTimeArr2 = {this.hour, this.minute, this.second};
            this.fullTimeArr = fullTimeArr2;
            this.fullTimeStr = String.format("%02d:%02d:%02d", this.hour, this.minute, this.second);
        }
        // sets the time, also checks if permitted data was inputted, you don't get 80:67:88

        public void printTime(){
            System.out.println(this.fullTimeStr);
        }
        // prints time

        public void print12Time(){
            if (12 < this.fullTimeArr[0]){
                System.out.println(String.format("%02d:%02d:%02d AM", this.hour -12, this.minute, this.second));
            } else {
                System.out.println(this.fullTimeStr + " PM");
            }
        }
        // prints 12h time. checks if hour is over 12, if so subtracts 12 to get 12h time


        public int[] returnTimeArr(){
            return this.fullTimeArr;
        }
        // returns the array with the inputted time

        public String returnTimeStr(){
            return this.fullTimeStr;
        }
        // returns the string



    }


}















