package pygui;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Executer extends Thread {

    static boolean isRunning;

    public Executer() {
        super();
        isRunning = true;
    }

    public void run() {
        try {
            SimpleDnD.process = Runtime.getRuntime().exec("./main.py " + SimpleDnD.field.getText());

            InputStream is = SimpleDnD.process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(is));
            
            String line = null;
            while ((line = reader.readLine()) != null) {
                if (line.contains("Final matches:")) {
                    isRunning = false;
                    while ((line = reader.readLine()) != null) {
                        SimpleDnD.ta1.setText(SimpleDnD.ta1.getText() + line + "\n");
                        SimpleDnD.match.add(line);
                        
                    }
                    
                    break;
                }
                SimpleDnD.ta.setText(SimpleDnD.ta.getText() + "\n" + line);
            }

            //isRunning = false;
        } catch (IOException ex) {
            System.out.println(ex);
        }
        
        isRunning = false;
    }

}
