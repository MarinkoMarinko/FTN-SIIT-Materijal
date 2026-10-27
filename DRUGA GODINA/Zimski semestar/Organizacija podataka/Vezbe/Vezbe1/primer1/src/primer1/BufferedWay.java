package primer1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BufferedWay {

	public static void main(String[] args) {
		try (BufferedReader br = new BufferedReader(new FileReader("drzave_gradovi.csv"))) {
			br.readLine();
			
			String line;
			while ((line = br.readLine()) != null) {
				System.out.println(line);
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}

	}

}
