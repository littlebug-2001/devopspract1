import java.io.*;
class Job extends Thread
{
  Job()
{ 
  this.start();
}
  public void run()
{
   
   try{
        System.out.println("thread is Running");
     this.sleep(6000);
     System.out.println("thread is Back");

}
catch(Exception e)
  {
     System.out.println("Error...."+e);
}
}
}
public class Demo1
{ 
public static void main(String[]args)
{
  Job f=new Job();
}
}