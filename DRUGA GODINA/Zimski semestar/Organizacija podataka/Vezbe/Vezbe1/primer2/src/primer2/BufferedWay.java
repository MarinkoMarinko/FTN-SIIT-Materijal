package primer2;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.Map;

public class BufferedWay {

	public static void main(String[] args) {
		LinkedHashMap<String, String> countries = TownData.getDrzaveGradovi();
 		try (BufferedWriter bw = new BufferedWriter(new FileWriter("drzave_gradovi2.csv"))) {
			bw.write("Drzave,gradovi\n");
			
			for (String country: countries.keySet()) {
				bw.write(country + "," + countries.get(country) + "\n");
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}

	}

}
