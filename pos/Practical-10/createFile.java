import java.io.*;
public class createFile
{
	public static void main(String[] args)
	{
		try
		{
			File file = new File("C://Users//admin//Desktop//javafile.txt");
			if (file.createNewFile())
			{
				System.out.println("New File is created!");
			}
			else
			{
				System.out.println("File Name Already Exists...");
			}
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
	}
}



