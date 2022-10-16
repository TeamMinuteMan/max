import java.io.*;

class WriteToFile
{
	public static void main(String[] args)
	{
		try
		{
			FileWriter fwrite = new FileWriter("WrittenFile.txt");
			fwrite.write("Hi, I am Max currently in Shiv sir's lecture");
			fwrite.close();
			System.out.println("File has been created and the content has been generated");
		}
		catch (IOException e)
		{
			System.out.println("Unexception error occurred");
			e.printStackTrace();
		}
	}
}
