import java.util.Scanner;

class Check
{
  public static void main(String args[])
  {
    int N;
    System.out.println("Enter an Integer number:");
    Scanner input = new Scanner(System.in);
    N = input.nextInt();
    if ( N == 0 )
        System.out.println("Entered number is zero");
     else if(N>0)
        System.out.println("Entered number is positive");
        else
         System.out.println("Entered number is negative");
  }
}
