// Consider the following class definitions

class Person
{
    private String name;
    public String getName()
    {return name;}
}

public class Book
{
    private String author;
    private String title;
    private Person borrower;

    public Book (String a, String t)
    {
        author = a;
        title = t;
        borrower = null;
    }

    public void printDetails()
    {
        System.out.print ("Author: " + author + "Title: " + title);

        //if( !borrower.equals(null))
        //if(borrower.getName() != null)
        //if (borrower != null)
        if(<>)
        {
            System.out.println("Borrower:" + borrower.getName());
        }
    }

    public void setBorrower (Person b)
    {  borrower = b; }

}
