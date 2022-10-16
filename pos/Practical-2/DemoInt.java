


class DemoInt implements Runnable
{
	public void run()
	{
		System.out.println("Thread is running...");
	}
	public static void main(String args[])
	{
		DemoInt m1=new DemoInt();
		Thread t1=new Thread(m1);
		t1.start();
	}
}