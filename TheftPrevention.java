
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

  private ACAdapter acAdapter;

  private ShutdownHook hook;

  public TheftPrevention() {
    acAdapter = new ACAdapter();

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
      while(true)
      {
        System.out.println("isPluggedIn:" + acAdapter.isPluggedIn());
        Thread.sleep(1000);
      }
    }catch(Exception e){
      e.printStackTrace();
    }
  }

  /**
   * @author
   * @desc enables the TheftPrevention system
   */
  public void enable()
  {

  }

  /**
   * @author
   * @desc disables the TheftPrevention system
   */
  public void disable()
  {

  }
}
