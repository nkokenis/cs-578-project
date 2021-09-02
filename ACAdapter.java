import java.io.*;

/**
 * @author Ryan
 * @desc Detects if AC adapter/charger is plugged into device.
 */
public class ACAdapter {
    // don't include file extension
    private static String windows_lib = "theft_lib_winx64";

    private String OS;
    
    private boolean isWindows;

    public ACAdapter()
    {
        OS = System.getProperty("os.name").toLowerCase();

        // used to determine which isPluggedIn method to use
        if(OS.contains("windows")){
            System.loadLibrary(windows_lib);
            isWindows = true;
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
    }

    private native boolean isPluggedInWin();

    /**
     * @author Garrett
     * @return
     */
    private boolean isPluggedInShell() {
        try {
        // Process p = Runtime.getRuntime().exec("sh CheckPower.sh", new String[0], new
        // File("."));
        Process p = Runtime.getRuntime()
            .exec("sh /Users/garrettohara/Desktop/sdsu/WirelessNetworks/cs-578-project/CheckPower.sh");
        p.waitFor();

        BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        BufferedReader errorReader = new BufferedReader(new InputStreamReader(p.getErrorStream()));

        // while ((line = reader.readLine()) != null) {
        // System.out.println(line);
        // }

        String line = "";
        while ((line = errorReader.readLine()) != null) {
            System.err.println(line);
        }

        line = "";
        line = reader.readLine();
        if (line.equals("Now drawing from \'AC Power\'")) {
            // System.out.println("System is connected: "+line);
            return true;
        }
        } catch (Exception e) {
        e.printStackTrace();
        System.exit(1);
        }

        return false;
    }
}
