import java.io.*;


class TheftPrevention{

  public static String getOperatingSysetem() {
    String os = System.getProperty("os.name");
    // System.out.println("Using SystemUtils: " + os);
    return os;
  }
  public static void main(String[] args){
    String system = getOperatingSysetem();
    System.out.println(system);
    if(system.equals("Mac OS X")){
      try{
        
        while(executeScript()){
          Thread.sleep(1000);
        }

      } catch (IOException e) {
        System.out.println("IO Exception!!");
        e.printStackTrace();;
      } catch (InterruptedException e) {
        e.printStackTrace();
      }catch (Exception e){
        e.printStackTrace();
      }
      
    } else {
      System.out.println("No");
    }
  }


  public static boolean executeScript() throws IOException, InterruptedException {
    Process p = Runtime.getRuntime().exec("sh /Users/garrettohara/Desktop/sdsu/WirelessNetworks/cs-578-project/CheckPower.sh");
    p.waitFor();

    BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
    BufferedReader errorReader = new BufferedReader(new InputStreamReader(p.getErrorStream()));

    // while ((line = reader.readLine()) != null) {
    // System.out.println(line);
    // }

    String line = "";
    while ((line = errorReader.readLine()) != null) {
      System.out.println(line);
    }

    line = "";
    line = reader.readLine();
    if(line.equals("Now drawing from \'AC Power\'")){
      System.out.println("System is connected: "+line);
      return true;
    } else {
      System.out.println("Device is DISCONNECTED: "+line);
      return false;
    }    
  }
}
