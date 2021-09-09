package cs578;

/**
 * @author Garrett, Ryan
 * 
 */
public class TheftPrevention {
    private class ShutdownHook extends Thread
  {
    public void run()
    {
      // we need to handle the case where user or theif shuts down app or computer
      // maybe user makes password when app launches and password must be used again to end
      // end app without alarm going off
      System.out.println("Program shutting down.");
    }
  }

  private ACAdapter ac_adapter;

  private ShutdownHook hook;

  private SecurePassword s_password;

  public TheftPrevention() {
    s_password = new SecurePassword();
    ac_adapter = new ACAdapter();

    hook = new ShutdownHook();
    Runtime.getRuntime().addShutdownHook(hook);
    
  }

  /*
   * This is only here for testing. I think it
   * would be better to have enable & disable methods
   * for the system.
   */
  public void run() {
    try{

      /*
      // code to test secure password.
      // I think we need to implement password so that theif cannot exit application. - Ryan 
      Console con = System.console();
      System.out.print("Set password: ");
      s_password.set(con.readPassword());

      System.out.print("Enter password: ");
      System.out.println(s_password.compare(con.readPassword()));
      */

      int i = 0;
      while(true)
      {
        System.out.println("isPluggedIn (" + (++i) + "):" + ac_adapter.isPluggedIn());
        Thread.sleep(1000);
      }
    }catch(Exception e){
      e.printStackTrace();
    }
  }
}
