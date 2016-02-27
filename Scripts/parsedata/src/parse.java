import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class parse {
	public static void main(String [ ] args) throws FileNotFoundException, IOException
	{
		String file = "src/data2.txt";
		try(BufferedReader br = new BufferedReader(new FileReader(file))) {
		    for(String line; (line = br.readLine()) != null; ) {
		        String time = line.substring(0, 8);
		        String status = line.contains("OK") ? "OK" : "FAIL";
		        String link = "0";
		        if (status.equals("OK")) {
		        	int endIndex = line.length() - 1;
		        	link = line.substring(endIndex - 4, endIndex);
		        }
//		        	int endIndex = line.length();
//		        	line.lastIndexOf(":");
//		        	link = line.substring(line.lastIndexOf(": ") + 2, endIndex);
//		        }
//		        System.out.println(line);
		    	System.out.println(time + ", " + status + ", " + link);
		    }
		}
	}
}
