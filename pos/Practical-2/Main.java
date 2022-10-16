import java.io.*;
class Fibonacci extends Thread
{
    public void run()
    {
        try
        {
            int a=0,b=1,c=0;
            BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    
    
            System.out.print("Enter the limit for fibonacci:");
        
            int n=Integer.parseInt(br.readLine());
            System.out.println("\n====================");
            System.out.println("Fibonacci series:");
            while(n>0)
            {
                System.out.print(c+" ");
                a=b;
                b=c;
                c=a+b;
                n=n-1;
            }
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }
    }
}
public class Main
{
    public static void main(String[] args)
    {
        Fibonacci f=new Fibonacci();
        f.run();
    }
}

