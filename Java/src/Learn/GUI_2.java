package Learn;

//import java.awt.FlowLayout;
//import java.awt.event.ActionEvent;
//import java.awt.event.ActionListener;
//import javax.swing.JFrame;
//import javax.swing.JTextField;
//import javax.swing.JPasswordField;
//import javax.swing.JLabel;
//import javax.swing.JOptionPane;
//import javax.swing.Icon
//import javax.ImageIcon
//import javax.swing.border.EmptyBorder;
//import javax.swing.event.ListSelectionEvent;
//import javax.swing.event.ListSelectionListener;
//import java.util.logging.Handler;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.border.*;
import DT.Java_Output;


public class GUI_2{
    public static void main(String args[]){
        System.out.println("GUI Demo File");

    }
}


class GUI_13_ColorChooser extends JFrame{
    private final JButton b1;  // button
    private Color color = (Color.WHITE);  // color
    private final JPanel panel1;  // panel to set color to

    public GUI_13_ColorChooser(){
        super("GUI_13_ColorChosser"); // title
        // don't have the setLayout();

        this.panel1 = new JPanel();  // create new panel
        this.panel1.setBackground(this.color);  //  set panel bg color

        this.b1 = new JButton("Pick Color");  //  create new button
        this.b1.addActionListener(new ActionListener() {  //  action listener. this listens for the button press and this will handle it
            @Override  // overrides the actionPerformed method. don't NEED this always, but SHOULD
            public void actionPerformed(ActionEvent e) {
                GUI_13_ColorChooser.this.color = JColorChooser.showDialog(null, "Color Chooser", GUI_13_ColorChooser.this.color);  // (window position(null for middle), "title bar", default color)
                    // opens color chooser, sets chosen to color variable, which is a Color variable type
                    if(GUI_13_ColorChooser.this.color ==null){
                        GUI_13_ColorChooser.this.color = Color.WHITE; }  // if user doesn't choose a color, it'll set to white
                GUI_13_ColorChooser.this.panel1.setBackground(GUI_13_ColorChooser.this.color);  // sets the panel bg to color

                Java_Output.printlnInfo("GUI_13_ColorChooser", "Color Set = " + GUI_13_ColorChooser.this.color);
                Java_Output.printlnInfo("GUI_13_ColorChooser", "Backgroudn set = " + GUI_13_ColorChooser.this.color);
                    // prints info to console
                }
            }
        );

        this.add(this.panel1, BorderLayout.CENTER);  // adds panel to JFrame
        this.panel1.add(this.b1, BorderLayout.SOUTH);  // adds b1 to panel1

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  // this is so you can close program with the window's x button
        this.setSize(100,100);  // sets the window size
        this.setVisible(true);  // makes window visible
    }


}
// color picker, changes background

class GUI_12_BasicGraphics extends JPanel{

    public void paintComponent(Graphics g)  {
        super.paintComponent(g);
        setBackground(Color.WHITE);

        // basic rectangle
        g.setColor(Color.BLUE);
        g.fillRect(10, 10, 50, 50);  //(x, y, width, height)

        // custom colored rectangle
        g.setColor(new Color(190, 81, 215));
        g.fillRect(50, 50, 100, 100);

        // draw non-filled rectangle
        g.setColor(Color.RED);
        g.drawRect(60, 65, 70, 80);
        // draw vs fill
        
        // draw text
        g.setColor(Color.BLACK);
        g.drawString("This is some text!", 10, 10);

        // draw line
        g.setColor(Color.YELLOW);
        g.drawLine(10, 10, 60, 60);  // draws line from x1/y1 to x2/y2

        // draws oval
        g.setColor(Color.GREEN);
        g.drawOval(150, 150, 60, 60);
        // you can create a circle with this, make width and hieght the same
        
        // draws(fills in) 3d rectangle, not actually 3d, it's just raised a little bit
        g.setColor(Color.ORANGE);
        g.fill3DRect(100, 100, 50, 50, true);
        


    }

/*



JFrame jf = new JFrame("GUI_12_BasicGraphics");
// creates new frame, since I didn't do it in the class
jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
// this is so you can close it with the x button on the window
GUI_12_BasicGraphics G12 = new GUI_12_BasicGraphics();
// creates new class object
jf.add(G12);
// adds to frame
jf.setSize(500, 500);
// sets window size
jf.setVisible(true);
// makes it visible

 */



}
// very basic graphics stuff

class GUI_11_LayoutAlignment extends JFrame{
    private final JButton leftB;
    private final JButton centerB;
    private final JButton rightB;
    private final FlowLayout layout;
    private final Container container;
    // creates variables

    public GUI_11_LayoutAlignment(){
        super("GUI_11_Layout");
        this.layout = new FlowLayout();
        this.container = this.getContentPane();
        this.setLayout(this.layout);
        // sets Layout type to the layout variable


        this.leftB = new JButton("Left");
        this.add(this.leftB);
        this.actionE(this.leftB, 0);


        this.centerB = new JButton("Center");
        this.add(this.centerB);
        this.actionE(this.centerB, 1);


        this.rightB = new JButton("Right");
        this.add(this.rightB);
        this.actionE(this.rightB, 2);
        // creates the buttons, and adds the action listener for each one

    }

    private void actionE(JButton button, int alignment) {
        button.addActionListener(e -> {
                    this.layout.setAlignment(alignment);
            // changes alignment with alignment var
                    this.layout.layoutContainer(this.container);
        }
        );
    }
    // you could make individual addActionListener things for each button, but I thought this might be faster
    
//        GUI_11_LayoutAlignment G = new GUI_11_LayoutAlignment();
//        G.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        G.setSize(400, 100);
//        G.setVisible(true);

}
// changes changes FlowLayout alignment with buttons

class GUI_10_Adapter extends JFrame{
    private final JLabel statusB;
    private final JPanel panel;
    private int clicks;  // keeps how many total clicks there are, no matter what mouse button or mouse posistion

    public GUI_10_Adapter(){
        super("GUI_10_Adapter");

        this.statusB = new JLabel("DEFAULT");
        this.add(this.statusB, BorderLayout.SOUTH);
        // creates status bar area, that shows how many clicks and with what button

        this.panel = new JPanel();
        this.add(this.panel, BorderLayout.CENTER);
        this.panel.setBackground(Color.WHITE);
        this.panel.addMouseListener(new MouseClass());
        // adds MouseClass as panel's mouse handler, don't need to create new object outside of this,
    }

    private class MouseClass extends MouseAdapter{
        // this uses the abstract mouseAdapter class, so you don't have to override every method from MouseEvent, just the ones you'll use
        private String B = "_";
        private final String[] txt = {"Pressed: ", " | Total: "};
        public void mouseClicked(MouseEvent e){
            GUI_10_Adapter.this.clicks += 1;
            // adds one to clicks, this happens everytime this mouseClicked method gets called, which is when you click a mouse button whether R click, Middle click, etc
            // I didn't use e.getClickCount() because that resets when you move the cursor to another xy coord
            if(e.isMetaDown()) {
                this.B = "RB"; }
            else if(e.isAltDown()) {
                this.B = "MB"; }
            else {
                this.B = "LB"; }
            // this changes B string to MB/RB/LB depending on what mouse button you click

            GUI_10_Adapter.this.statusB.setText(String.format(this.txt[0] + this.B + this.txt[1] + GUI_10_Adapter.this.clicks));
            // updates the statusB text
            GUI_10_Adapter.this.panel.setBackground(Color.RED);

            System.out.println("e.getButton: "+ e.getButton());
        }

        public void mouseEntered(MouseEvent e){
            GUI_10_Adapter.this.panel.setBackground(Color.WHITE);
        }

    }
}
// use of MouseAdapter instead of MouseListener, the adapter you don't have to override all of the methods unlike MouseListener


class GUI_9_MouseEvent extends JFrame{

    private final JPanel mouseP;
    private final JLabel statusB;

    public GUI_9_MouseEvent(){
        super("GUI_9_MouseEvent");

        this.mouseP = new JPanel();
        this.mouseP.setBackground(Color.WHITE);
        this.add(this.mouseP, BorderLayout.CENTER);
        // the panel that the mouse well be interacting with

        this.statusB = new JLabel("Default");
        this.add(this.statusB, BorderLayout.SOUTH);
        // this will show what is happening

        GUI_9_MouseEvent.HandlerClass handler = new GUI_9_MouseEvent.HandlerClass();
        this.mouseP.addMouseListener(handler);
        this.mouseP.addMouseMotionListener(handler);
        // making a handler class


    }

    private class HandlerClass implements MouseListener, MouseMotionListener{
        private String button;
        public void mouseClicked(MouseEvent e){
            if(2 == e.getClickCount() && !e.isConsumed()){
                e.consume();
                if (e.isMetaDown()){
                    this.button = "Meta(Right)"; }
                else if(e.isAltDown()){
                    this.button = "Alt(Middle)"; }
                else if(e.isShiftDown()){
                    this.button = "Shift"; }
                else if(e.isControlDown()){
                    this.button = "Control"; }
                else {
                    this.button = "Left"; }
                System.out.printf("DOUBLE %s Click at %d, %d\n", this.button, e.getX(), e.getY());
            }
            // prints to console if you double clicked, and prints different depending on what extra button is held downs

            GUI_9_MouseEvent.this.mouseP.setBackground(Color.YELLOW);
            GUI_9_MouseEvent.this.statusB.setText(String.format("Clicked at %d, %d", e.getX(), e.getY()));
            // this prints the coords of the mouse, e.getX/Y() gets the X,Y coords
            // 0,0 is the top left corner of panel

        }
        // mouse clicked in mouseP panel

        public void mousePressed(MouseEvent e){
            GUI_9_MouseEvent.this.statusB.setText("Pressed Mouse");
            GUI_9_MouseEvent.this.mouseP.setBackground(Color.PINK);
        }
        public void mouseReleased(MouseEvent e){
            GUI_9_MouseEvent.this.statusB.setText("Released Mouse");
            GUI_9_MouseEvent.this.mouseP.setBackground(Color.CYAN);
        }
        // release is when you hold and drag then release, if you press and release in the same spot it's a click

        public void mouseEntered(MouseEvent e){
            GUI_9_MouseEvent.this.statusB.setText("Mouse Entered");
            GUI_9_MouseEvent.this.mouseP.setBackground(Color.GREEN);
        }
        // when mouse enters the mouseP panel it'll change the bg to green and the statusB text
        public void mouseExited(MouseEvent e){
            GUI_9_MouseEvent.this.statusB.setText("Mouse Exited");
            GUI_9_MouseEvent.this.mouseP.setBackground(Color.RED);
        }
        // when mouse leave mouseP panel it'll change bg to red and change statusB text

        public void mouseMoved(MouseEvent e){
            GUI_9_MouseEvent.this.statusB.setText("Mouse is Moving");
            GUI_9_MouseEvent.this.mouseP.setBackground(Color.BLUE);

        }

        public void mouseDragged(MouseEvent e){
            GUI_9_MouseEvent.this.statusB.setText("Mouse is Dragging");
            GUI_9_MouseEvent.this.mouseP.setBackground(Color.ORANGE);
        }
    }

}
// mouse events, depending on mouse event it'll change the bg color

class GUI_8_2List1Button extends JFrame{
    private final JList leftList;
    private JList rightList;
    // yu can set the object type here as well, private Jlist leftList = new Jlist(); ... , but i think it's just easier to do it later on
    private final JButton moveB;
    private static final String[] foods = {"Apple", "Banana", "Watermelon", "Pineapple", "Peach", "Strawberry"};


    public GUI_8_2List1Button(){
        super("GUI_8: 2 List, 1 Button");
        this.setLayout(new FlowLayout());

        this.leftList = new JList(GUI_8_2List1Button.foods);
        this.leftList.setVisibleRowCount(3);
        this.leftList.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        this.add(new JScrollPane(this.leftList));
        // creates and sets up leftList

        this.moveB = new JButton("Move -->");
        this.moveB.addActionListener(
                e -> this.rightList.setListData(this.leftList.getSelectedValuesList().toArray())
                // you can use leftList.getSelectedValues() , but that is being deprecated, a quick(not permanent fix) is to use leftList.getSelectedValuesList().toArray()
                // e -> { ... } also works. this ^ is called an expression lambda
                // can use lambda instead of making the whole public void ActionListener(){new ActionListener{}} method
        );
        this.add(this.moveB);
        // sets up move button and the action handler for it, in this demo it uses a expression lambda

        this.rightList = new JList();
        this.rightList.setVisibleRowCount(3);
        this.rightList.setFixedCellWidth(100);
        this.rightList.setFixedCellHeight(20);
        // sets the width and height, overrides the FlowLayout
        this.rightList.setSelectionMode(ListSelectionModel.MULTIPLE_INTERVAL_SELECTION);
        this.add(new JScrollPane(this.rightList));
        // creates and sets up right list

        // when you select item(s) from the left list then click the move button it'll remove everything from the right list then add
    }


//        GUI_8_2List1Button G = new GUI_8_2List1Button();
//        G.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        G.setSize(300, 300);
//        G.setVisible(true);


}
// 2 list, the button moves selected items from left list to right list

class GUI_7_List extends JFrame{
    private final JList list;
    private static final String[] colorNames = {"Black", "White", "Red", "Green", "Blue"};
    private static final Color[] colors = {Color.BLACK, Color.WHITE, Color.RED, Color.GREEN, Color.BLUE};


    public GUI_7_List(){
        super("GUI_7: List");
        this.setLayout(new FlowLayout());


        this.list = new JList(GUI_7_List.colorNames);
        // creates a list, with the options from colorNames list
        this.list.setVisibleRowCount(4);
        // sets how many items to show at once, if there is more it'll show a scroll bar. you'll need to add the scrollbar, you can add it when you call add() to add the list.
        this.list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        // sets the selection mode of list, this is set so you can only select only one at a time
        this.add(new JScrollPane(this.list));
        // adds list object to screen, but with scrollbar

        this.list.addListSelectionListener(e -> {
            this.getContentPane().setBackground(GUI_7_List.colors[this.list.getSelectedIndex()]);
                    // changes the windows background color depending on the selection, by getting the selected index and using the colors list index
                }
        );
    }

//        GUI_7_List G = new GUI_7_List();
//        G.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        G.setSize(300, 200);
//        G.setVisible(true);


}
// list, change background depending on item selected from list

class GUI_6_Combobox extends JFrame{
    private final JComboBox cBox;
    private final JLabel pic;

    private static final String[] filename = {"a.png", "b.png"};
    private final Icon[] pics = {new ImageIcon(this.getClass().getResource(GUI_6_Combobox.filename[0])),
                            new ImageIcon(this.getClass().getResource(GUI_6_Combobox.filename[1]))};
    // adds picture as icons. you could skip the Stirng[] part and just add the file name in the .getResource()
    public GUI_6_Combobox(){
        super("GUI_6: ComboBox");
        this.setLayout(new FlowLayout());

        this.cBox = new JComboBox(GUI_6_Combobox.filename);
        // you don't need to create a whole new class just for handling something simple like this
        this.cBox.addItemListener(
            new ItemListener() {
                public void itemStateChanged(ItemEvent e) {
                    if(ItemEvent.SELECTED == e.getStateChange()){
                        // checks if the selected item is the same as the state
                        GUI_6_Combobox.this.pic.setIcon(GUI_6_Combobox.this.pics[GUI_6_Combobox.this.cBox.getSelectedIndex()]);
                        // changes pic var to the selected item by index
                    }
                }
            }
        );

        this.add(this.cBox);
        this.pic = new JLabel(this.pics[0]);
        this.add(this.pic);

    }

// you don't need this
//    private class Handler_Class implements ItemListener{
//        @Override
//        public void itemStateChanged(ItemEvent e) {
//            if(e.getStateChange()==ItemEvent.SELECTED){
//                pic.setIcon(pics[cBox.getSelectedIndex()]);
//            }
//        }
//    }





}
// combo box, change icon depending on selected

class GUI_5_Radiobuttons extends JFrame{
    private final JLabel textField;
    private final Font plainF; //  plain font
                private final Font boldF;  // bold font
                private final Font italicF;  // italic font
                private final Font boldItalicF; // bold italic font


    private final JRadioButton plainB;
    private final JRadioButton boldB;
    private final JRadioButton italicB;
    private final JRadioButton boldItalicB;
                        // creates radio buttons

    private final ButtonGroup group;
    // creates ButtonGroup. this is so the buttons know what each others state is and so only one can be true

    public GUI_5_Radiobuttons(){
        super("GUI_5: Radio Button");
        this.setLayout(new FlowLayout());


        this.textField = new JLabel("This is another fun sentence! :)");
        this.add(this.textField);
        // creates label

        this.plainB = new JRadioButton("Plain", true);
        this.boldB = new JRadioButton("Bold", false);
        this.italicB = new JRadioButton("Italic", false);
        this.boldItalicB = new JRadioButton("Bold + Italic", false);
        this.add(this.plainB);
        this.add(this.boldB);
        this.add(this.italicB);
        this.add(this.boldItalicB);
        // creates and adds buttons

        this.group = new ButtonGroup();
        this.group.add(this.plainB);
        this.group.add(this.plainB);
        this.group.add(this.boldB);
        this.group.add(this.boldItalicB);
        // adds buttons to group

        this.plainF = new Font("serf", Font.PLAIN, 14);
        this.boldF = new Font("serf", Font.BOLD, 14);
        this.italicF = new Font("serf", Font.ITALIC, 14);
        this.boldItalicF = new Font("serf", Font.BOLD + Font.ITALIC, 14);
        // create fonts

        this.textField.setFont(this.plainF);
        this.plainB.addItemListener(new Handler_Class(this.plainF));
        this.boldB.addItemListener(new Handler_Class(this.boldF));
        this.italicB.addItemListener(new Handler_Class(this.italicF));
        this.boldItalicB.addItemListener(new Handler_Class(this.boldItalicF));
        // itemListener


    }

    private class Handler_Class implements ItemListener{
        private final Font font;  //  current font
        public Handler_Class(Font f){
            this.font = f; }
        // sets font to what is passed in

        @Override
        public void itemStateChanged(ItemEvent e) {
            GUI_5_Radiobuttons.this.textField.setFont(this.font);
        }
        // updates textField to current font
    }

//    GUI_5 G = new GUI_5();
//    G.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//    G.setSize(250, 100);
//    G.setVisible(true);

}
// radio buttons, changes text font style

class GUI_4_Checkbox extends JFrame {
    private final JLabel textField;
    private final JCheckBox boldBox;
    private final JCheckBox italicBox;

    public GUI_4_Checkbox() {
        super("GUI_4: Checkboxes");  //  title, should know this by know!
        this.setLayout(new FlowLayout());  // layout

        this.textField = new JLabel("This is a sentence");
        this.textField.setBorder(new EmptyBorder(10, 10, 10, 10));
        // adds small border to make it look little nicer
        this.textField.setFont(new Font("serif", Font.PLAIN, 14));
        this.add(this.textField);
        // creates text field, Jlabel, there is a JTextField for input

        this.boldBox = new JCheckBox("Bold");
        this.italicBox = new JCheckBox("Italic");
        // creates new check boxes
        this.add(this.boldBox);
        this.add(this.italicBox);


        GUI_4_Checkbox.Handler_Class handler = new GUI_4_Checkbox.Handler_Class();
        this.boldBox.addItemListener(handler);
        this.italicBox.addItemListener(handler);
        // sets event handling for checkboxes
    }

    private class Handler_Class implements ItemListener {
        public void itemStateChanged(ItemEvent event) {
            Font font = null;

            if (GUI_4_Checkbox.this.boldBox.isSelected() && GUI_4_Checkbox.this.italicBox.isSelected())  // sets if both checkboxes are checked
                font = new Font("Self", Font.BOLD + Font.ITALIC, 14);
            else if (GUI_4_Checkbox.this.boldBox.isSelected())
                font = new Font("Self", Font.BOLD, 14);
            else if (GUI_4_Checkbox.this.italicBox.isSelected())
                font = new Font("Self", Font.ITALIC, 14);
            else  // if none are checked
                font = new Font("Serif", Font.PLAIN, 14);

            GUI_4_Checkbox.this.textField.setFont(font);  // updates textField with new font
        }
    }
//    GUI_4 G = new GUI_4();
//    G.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//    G.setSize(180, 100);
//    G.setVisible(true);
}
// checkboxes changing font style

class GUI_3_Button extends JFrame{


    private final JButton reg;
    private final JButton custom;


    public GUI_3_Button(){
        super("GUI_3: Buttons");  //  set window title
        this.setLayout(new FlowLayout());  // sets the layout config

        this.reg = new JButton("reg Button");
        this.add(this.reg);
        // creates and shows reg button


        Icon a = new ImageIcon((this.getClass().getResource("a.png")));
        Icon b = new ImageIcon((this.getClass().getResource("b.png")));

        this.custom = new JButton("custom", a);
        this.custom.setRolloverIcon(b);
        this.add(this.custom);


        GUI_3_Button.Handler_Class handler = new GUI_3_Button.Handler_Class();
        this.reg.addActionListener(handler);
        this.custom.addActionListener(handler);


    }

    private class Handler_Class implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e) {
            JOptionPane.showMessageDialog(null, String.format("%s", e.getActionCommand()));
        }
    }




}
// change image of button when mouse hover


class GUI_2_Baiscs extends JFrame {

    private final JLabel labelF1;
    private final JTextField textF1;
    private final JTextField textF2;
    private final JTextField noEditField;
    private final JPasswordField pwdField;
    // create items to show

    public GUI_2_Baiscs() {
        super("GUI_2: Basics");  //  title bar
        this.setLayout(new FlowLayout());  //  set layout type

        this.labelF1 = new JLabel("Hello this is a text label");
        this.labelF1.setToolTipText("Tooltip Text Here");
        this.add(this.labelF1);
        // a text label

        this.textF1 = new JTextField(10);
        this.add(this.textF1);
        // set width of text input field

        this.textF2 = new JTextField("Enter Text here");
        this.add(this.textF2);
        // text entry field

        this.noEditField = new JTextField("Can't edit this", 20);
        this.noEditField.setEditable(false);
        this.add(this.noEditField);
        // doesn't allow edits to it

        this.pwdField = new JPasswordField("Password");
        this.add(this.pwdField);
        // a password field. similar to regular text field but shows input as dots

        GUI_2_Baiscs.theHandler handler = new GUI_2_Baiscs.theHandler();
        this.textF1.addActionListener(handler);
        this.textF2.addActionListener(handler);
        this.noEditField.addActionListener(handler);
        this.pwdField.addActionListener(handler);


    }

    private class theHandler implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String string = "";
            if (e.getSource() == GUI_2_Baiscs.this.textF1)
                string = String.format("Text Field 1: %s", e.getActionCommand());
            else if (e.getSource() == GUI_2_Baiscs.this.textF2)
                string = String.format("Text Field 2: %s", e.getActionCommand());
            else if (e.getSource() == GUI_2_Baiscs.this.noEditField)
                string = String.format("No Edit Field: %s", e.getActionCommand());
            else if (e.getSource() == GUI_2_Baiscs.this.pwdField)
                string = String.format("Password Field: %s", e.getActionCommand());
            // checks if any of the input boxes had interaction, Enter to be specific, then sets the string variable to what the box has in it

            JOptionPane.showMessageDialog(null, string);
            // shows dialog with input from the different input boxes
        }
    }

}
// Java GUI basics
