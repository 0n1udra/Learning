package Learn;

import javax.swing.*;
import java.awt.*;



public class Basic_GUI {

    public static void main(String args[]){






    }


    public static void adding1Nums(){
        String firstNum = JOptionPane.showInputDialog("Input First Number");
        String secondNum = JOptionPane.showInputDialog("Input Second Number");
        // shows input dialogs to ask for input. it'll show you two dialogs

        int Num1 = Integer.parseInt(firstNum);
        int Num2 = Integer.parseInt(secondNum);
        // converts to integer. you CAN'T get other input from the JOP dialog

        int sum = Num1 + Num2;
        // adds

        JOptionPane.showMessageDialog(null, "The Answer is: " + sum, "Title Bar", JOptionPane.PLAIN_MESSAGE);
        // shows a message dialog.           Position                  Message                      title bar             message type
    }

}
