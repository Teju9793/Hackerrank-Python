import java.util.Scanner;
class hello
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the FIRST number : ");

        double a = sc.nextDouble();

        System.out.print("Enter the SECEND number : ");

        double b = sc.nextDouble();

        System.out.print("Select an oparater | + | - | * | / | :: ");

        String o = sc.next();

        if (o.equals("+"))
        {
            System.out.print("Result is : "+(a + b));
        }
        else if(o.equals("-")){System.out.print("Result is : "+ (a-b));}

        else if(o.equals("*")){System.out.print("Result is :"+(a*b));}

        else if (o.equals("/"))
        {
            if(b==0)
            {
                System.out.print("Number can't devisible by zero");
            }
            else
            {
                System.out.print("Result is : "+ (a/b));
            }
                
        }
        else{System.out.println("you Entered the wrong oparator");}



    }
}
