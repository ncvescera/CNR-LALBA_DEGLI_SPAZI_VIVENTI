package pygui;

import com.sun.glass.events.KeyEvent;
import java.awt.Font;
import java.awt.TextArea;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.KeyStroke;

public class SimpleDnD extends JFrame implements ActionListener {

    static JTextField field;
    JButton button;
    JLabel labelIn;
    JLabel labelOut;
    static TextArea ta;
    JScrollPane scroll = new JScrollPane(ta);

    JFileChooser fc;

    JPanel p1 = new JPanel();
    JPanel p2 = new JPanel();

    static TextArea ta1;

    JButton mapps;

    JMenuBar menu;
    JMenu file;
    JMenu tools;
    JMenuItem open;
    JMenuItem close;
    JMenuItem fix;

    static List<String> match = new ArrayList<>();

    static Process process;
    

    public SimpleDnD() {

        setTitle("PDF Analizer - IRPI");

        Box r = new Box(BoxLayout.X_AXIS);

        fc = new JFileChooser();

        menu = new JMenuBar();

        file = new JMenu("File");
        file.setMnemonic(KeyEvent.VK_F);

        tools = new JMenu("Tools");
        tools.setMnemonic(KeyEvent.VK_T);

        open = new JMenuItem("Open file", KeyEvent.VK_O);
        open.addActionListener(this);
        open.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_O, ActionEvent.ALT_MASK));

        close = new JMenuItem("Exit", KeyEvent.VK_Q);
        close.addActionListener(this);
        close.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_Q, ActionEvent.ALT_MASK));

        fix = new JMenuItem("Fix", KeyEvent.VK_R);
        fix.addActionListener(this);
        fix.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_R, ActionEvent.ALT_MASK));

        file.add(open);
        file.addSeparator();
        file.add(close);

        tools.add(fix);

        menu.add(file);
        menu.add(tools);

        button = new JButton("Analizza");
        button.setFont(new Font("Times New Romans", Font.PLAIN, 12));
        button.addActionListener(this);

        mapps = new JButton("Visualizza nelle mappe");
        mapps.setFont(new Font("Times New Romans", Font.PLAIN, 18));
        mapps.addActionListener(this);

        field = new JTextField("", 20);
        field.setFont(new Font("Times New Romans", Font.PLAIN, 18));

        labelIn = new JLabel("Trascina il file qui");
        labelOut = new JLabel("Output: ");
        labelOut.setBounds(10, 10, 10, 10);

        field.setDragEnabled(true);

        ta = new TextArea(" ", 20, 10);

        ta.setText(" ");
        ta.setEditable(false);

        ta1 = new TextArea(" ");

        ta1.setText(" ");
        ta1.setEditable(false);

        p1.add(field);
        p1.add(button);

        r.add(p1);

        Box r1 = new Box(BoxLayout.X_AXIS);

        r1.add(Box.createHorizontalStrut(10));
        r1.add(ta);
        r1.add(Box.createHorizontalStrut(10));

        Box r2 = new Box(BoxLayout.Y_AXIS);
        Box r3 = new Box(BoxLayout.X_AXIS);
        Box r4 = new Box(BoxLayout.X_AXIS);
        Box r5 = new Box(BoxLayout.X_AXIS);
        Box r6 = new Box(BoxLayout.X_AXIS);
        Box r7 = new Box(BoxLayout.X_AXIS);

        r3.add(labelIn);
        r4.add(labelOut);
        r4.add(Box.createHorizontalStrut(510));

        r5.add(new JLabel("Final matches:"));
        r5.add(Box.createHorizontalStrut(460));
        r6.add(Box.createHorizontalStrut(10));
        r6.add(ta1);
        r6.add(Box.createHorizontalStrut(10));
        r7.add(mapps);

        r2.add(Box.createVerticalStrut(15));
        r2.add(r3);
        r2.add(r);
        //r2.add(Box.createVerticalStrut(15));
        r2.add(r4);
        r2.add(Box.createVerticalStrut(10));
        r2.add(r1);
        r2.add(Box.createVerticalStrut(15));

        r2.add(r5);
        r2.add(Box.createVerticalStrut(10));
        r2.add(r6);
        r2.add(Box.createVerticalStrut(20));
        r2.add(r7);
        r2.add(Box.createVerticalStrut(15));

        add(r2);

        //button.setTransferHandler(new TransferHandler("text"));
        setJMenuBar(menu);
        setSize(600, 750);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
        setResizable(false);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String bottone = e.getActionCommand();
        if (bottone.equals("Analizza")) {
            ta.setText("");
            ta1.setText("");

            if (field.getText().contains(".pdf")) {
                Thread exec = new Executer();

                try {
                    exec.start();

                    while (Executer.isRunning) {
                        if (Executer.isRunning) {
                            Thread.sleep(250);
                            if (Executer.isRunning)
                                SimpleDnD.ta.setText("Attendere");
                        }
                        if(Executer.isRunning){
                            Thread.sleep(250);
                            if (Executer.isRunning)
                                SimpleDnD.ta.setText("Attendere ...");
                        }
                        
                        Thread.sleep(250);
                        
                    }
                } catch (InterruptedException ex) {
                    Logger.getLogger(SimpleDnD.class.getName()).log(Level.SEVERE, null, ex);
                }
            } else {
                ta.setText("Nessun file PDF inserito !!\n");
            }
        }
        if (bottone.equals("Visualizza nelle mappe")) {
            for (String elem : match) {
                String[] strs = elem.split(",");
                String command = "firefox ";
                try {
                    Process process = Runtime.getRuntime().exec(command + strs[0]);
                } catch (IOException ex) {

                }
            }
        }
        if (bottone.equals("Open file")) {
            int returnVal = fc.showOpenDialog(this);

            if (returnVal == JFileChooser.APPROVE_OPTION) {
                File file = fc.getSelectedFile();

                field.setText(file.getPath());

            }
        }
        if (bottone.equals("Exit")) {
            System.exit(0);
        }
        if (bottone.equals("Fix")) {
            try {
                Process process = Runtime.getRuntime().exec("./installGeon.sh");

                InputStream is = process.getInputStream();
                BufferedReader reader = new BufferedReader(new InputStreamReader(is));

                String line = null;
                while ((line = reader.readLine()) != null) {
                    ta.setText(ta.getText() + "\n" + line);
                }
            } catch (IOException ex) {
                ta.setText("" + ex);
            }
        }
    }

}
