
/**
 * @author Garrett, Ryan
 * 
 */
public class TheftPrevention {
  private ACAdapter acAdapter;

  public TheftPrevention() {
    acAdapter = new ACAdapter();
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
