import java.io.*;
class Job extends Thread
{
  String tname;
  Job(String name)
{
  tname=name; 
  this.start();
}
  public void run()
{
   
   try{
        System.out.println("thread is Running" +tname);
     this.sleep(6000);
     System.out.println(tname+ "thread is Back");

}
catch(Exception e)
  {
     System.out.println("Error...."+e);
}
}
}
public class Demo2
{ 
public static void main(String[]args)
{
  Job f1=new Job("1");
  Job f2=new Job("2");
  Job f3=new Job("3");
  Job f4=new Job("4");
}
}