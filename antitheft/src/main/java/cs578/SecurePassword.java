package cs578;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.Arrays;

/**
 * @author Ryan
 * @desc A password which is only has it's hash stored
 */
public class SecurePassword
{
    private String hash_algorithm = "SHA-256";
    private byte[] salt;
    private byte[] hashed_password;

    public SecurePassword()
    {
      salt = new byte[20];
      try{
        SecureRandom.getInstanceStrong().nextBytes(salt);
      }catch(NoSuchAlgorithmException ex){
        SecureRandom random = new SecureRandom();
        random.nextBytes(salt);
      }
      
     // System.out.println(Arrays.toString(salt));
    }

    public String getHashAlgorithm()
    {
        return hash_algorithm;
    }

    public void setHashAlgorithm(String hash_algorithm)
    {
        this.hash_algorithm = hash_algorithm;
    }

    public void set(String password)
    {
        this.set(password.toCharArray());
    }

    public void set(char[] chars)
    {
        // convert char[] to byte[]
        this.set(charToByte(chars));
    }

    public void set(byte[] bytes)
    {
      try{
        MessageDigest md = MessageDigest.getInstance(hash_algorithm);
        md.update(bytes);
        hashed_password = md.digest(salt);
      }catch(NoSuchAlgorithmException e){
        e.printStackTrace();
        System.exit(1);
      }
    }
  
    public boolean compare(String password)
    {
      return this.compare(password.toCharArray());
    }

    public boolean compare(char[] chars)
    {
      return this.compare(charToByte(chars));
    }

    public boolean compare(byte[] bytes)
    {
      try{
        MessageDigest md = MessageDigest.getInstance(hash_algorithm);
        md.update(bytes);
        //md.update(salt.getBytes());
        byte[] other_hashed_password = md.digest(salt);
  
        if(Arrays.equals(other_hashed_password, hashed_password))
          return true;
      }catch(NoSuchAlgorithmException e){
        e.printStackTrace();
        System.exit(1);
      }
  
      return false;
    }

    private static byte[] charToByte(char[] chars)
    {
        // java chars are 2 bytes.
        byte[] bytes = new byte[chars.length * 2];

        for(int i = 0; i < chars.length; ++i){
          char c = chars[i];

          byte b1 = (byte)(c >> 8);
          byte b2 = (byte)c;

          bytes[i*2] = b1;
          bytes[i*2 + 1] = b2;
        }

        return bytes;
    }
}