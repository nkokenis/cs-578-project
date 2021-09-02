

class Detection{

  public static String getOperatingSysetem() {
    String os = System.getProperty("os.name");
    // System.out.println("Using SystemUtils: " + os);
    return os;
  }
  public static void main(String[] args){
    System.out.println(getOperatingSysetem());
  }
}
