package cs578;

import java.io.*;

/**
 * @author Ryan
 * @desc Detects if AC adapter/charger is plugged into device.
 */
public class ACAdapter {
    // don't include file extension
    //private static String windows_lib = "theft_lib_winx64";
    private static String windows_lib;

    private String OS;
    private String PATH;
    
    private boolean isWindows;
    private boolean isMac;

    public ACAdapter()
    {
        OS = System.getProperty("os.name").toLowerCase();

        // used to determine which isPluggedIn method to use
        if(OS.contains("windows")){
            try {
                String path = new java.io.File(".").getCanonicalPath() + "\\resources\\theft_lib_winx64.dll";
                System.load(path);
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
                System.exit(1);
            }

            isWindows = true;
        } else if(OS.equals("mac os x")){
            isMac = true;
            isWindows = false;
        }
        else
        {
            isWindows = false;
        }

    }

    public boolean isPluggedIn()
    {
        if(isWindows)
            return isPluggedInWin();
        else
            return isPluggedInShell();
        // executeScript(PATH);
        //  return isPluggedInShell();
    }

    private native boolean isPluggedInWin();

    /**
     * @author Garrett
     * @return boolean
     */
    private boolean isPluggedInShell() {

        try {
            PATH = getFilePath();
            while (executeScript(PATH)) {
                Thread.sleep(1000);
            }
            return false;

        } catch (IOException e) {
            System.out.println("IO Exception!!");
            e.printStackTrace();
            ;
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
    
    /**
     * @author Garrett
     * @return boolean
     */
    public static boolean executeScript(String path) throws IOException, InterruptedException {
        String cmd = "sh " + path + "/resources/CheckPower.sh";
        Process p = Runtime.getRuntime().exec(cmd);
        p.waitFor();

        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        BufferedReader errorReader = new BufferedReader(new InputStreamReader(p.getErrorStream()));

        String line = "";
        while ((line = errorReader.readLine()) != null) {
            System.out.println(line);
            return false;
        }

        line = "";
        line = reader.readLine();
        if (line.equals("Now drawing from \'AC Power\'")) {
            System.out.println("System is connected: " + line);
            return true;
        } else {
            System.out.println("Device is DISCONNECTED: " + line);
            return false;
        }
    }
    
    /**
     * @author Garrett
     * @return String
     */
    public static String getFilePath() throws IOException, InterruptedException {
        Process p = Runtime.getRuntime().exec("pwd");
        p.waitFor();

        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        BufferedReader errorReader = new BufferedReader(new InputStreamReader(p.getErrorStream()));

        String line = "";
        while ((line = errorReader.readLine()) != null) {
            System.out.println(line);
        }

        line = "";
        return new String(reader.readLine());
    }
}
