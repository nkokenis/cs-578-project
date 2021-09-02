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
        
        executeScript();

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


  public static void executeScript() throws IOException, InterruptedException {
    Process p = Runtime.getRuntime().exec("sh /Users/garrettohara/Desktop/sdsu/WirelessNetworks/cs-578-project/SystemDetection.sh");
    p.waitFor();

    BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
    BufferedReader errorReader = new BufferedReader(new InputStreamReader(p.getErrorStream()));


    String line = "";
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }

    line = "";
    while ((line = errorReader.readLine()) != null) {
        System.out.println(line);
    }
  }
}
