package cs578;
import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.Message;
import com.twilio.type.PhoneNumber;

public class SMS {
  // Find your Account Sid and Token at twilio.com/user/account
  public static final String ACCOUNT_SID = "ACca4c7647cee2c037bda6c60260ac56df";
  public static final String AUTH_TOKEN = "78f1eb8efbeb6c248c33085821a18ccb";

  public static void main(String[] args) {
    Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
    /*
    Message message = Message.creator(new PhoneNumber("+19254378380"),
        "Testing SMS messaging").create();
    
    System.out.println(message.getSid());
    */
  }
}