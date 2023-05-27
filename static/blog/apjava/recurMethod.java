
public static boolean recurMethod(String str) {
    
  if(str.length() <= 1)
  {
    return true;
  }
  else if (str.substring(0, 1).compareTo(str.substring(1,2)) > 0)
  {
    return recurMethod(str.substring(1));
  }
  else
  {
    return false;
  }
    
}
