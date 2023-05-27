
public class Main1 {
  public static void main(String[] args) {
      Bird myBird = new Bird("Eagle", "Brown", true);
      System.out.println(myBird.getSpecies());
  }
}

class Bird {
  private String species;
  private String color;
  private boolean canFly;

  public Bird(String str, String col, boolean cf) {
      species = str;
      color = col;
      canFly = cf;
  }

  public Bird() {
    species = "unknown";
    color = "unknown";
    canFly = false;
  }

  public Bird (boolean cf)
  {
    species = "unknown";
    color = "unknown";
    canFly = cf;
  }

  public Bird(String col, String str)
  {
    species = str;
    color = col;
    canFly = false;
  }

  public Bird(boolean cf, String str, String col)
  {
    species = str;
    color = col;
    canFly = cf;
  }

  public Bird(String col, String str, boolean cf)
  {
    species = str;
    color = col;
    canFly= cf;
  }

  public String getSpecies() {
      return species;
  }
}



/*
(A) public Bird()
    {
      species = "unknown";
      color = "unknown";
      canFly = false;
    }

(B) public Bird (boolean cf) //canFly
    {
      species = "unknown";
      color = "unknown";
      canFly = cf;
    }

(C) public Bird(String col, String str)
    {
      species = str;
      color = col;
      canFly = false;
    }

(D) public Bird(boolean cf, String str, String col)
    {
      species = str;
      color = col;
      canFly = cf;
    }

(E) public Bird(String col, String str, boolean cf)
    {
      species = str;
      color = col;
      canFly= cf;
    }

E有问题, 

*/