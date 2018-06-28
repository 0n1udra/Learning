import java.util.*;

public class Challenges {
    public static void main(String args[]){

       threeNPlusOne();

    }


    public static void deepArrForLoop(){

        int[][] deepArray = new int[10][10];
        for (int i=0; i<deepArray.length; i++){
            // loops 10 times to loop in each deeper array
            for (int i2=0; i2<deepArray[i].length; i2++){
                // loop 10 times to set each item in the array
                deepArray[i][i2] = Integer.parseInt(Integer.toString(i) + Integer.toString(i2));

            }
        }

       System.out.println(Arrays.deepToString(deepArray));
    }

    public static void threeNPlusOne(){
        Scanner usrInp = new Scanner(System.in);
        int n = 0, x = 0;
        DTJO.printUsrinp("Starting # > ");
        try{ x = usrInp.nextInt(); }
        catch (Exception e) {
            DTJO.printlnError("threeNPlusOne", "Wrong Input Type");
            x = 2;
        }

        while(x != 1) {
            n += 1;
            if(x % 2 == 0) { x /= 2; }
            else { x = x * 3 + 1; }
            System.out.printf("%d) %d\n", n, x);
        }
        System.out.println("Number until 1: " + n);
    }


}
