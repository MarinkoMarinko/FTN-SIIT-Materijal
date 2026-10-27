
package primer2;

import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedHashMap;

import com.opencsv.CSVWriter;

public class CSVWriterWay {

    public static void main(String[] args) {
        LinkedHashMap<String, String> countries = TownData.getDrzaveGradovi();
        try (CSVWriter writer = new CSVWriter(new FileWriter("drzave_gradovi2.csv"))) {
            writer.writeNext(new String[]{"Drzave", "gradovi"}, false);
            for (String country : countries.keySet()) {
                String[] line = {country, countries.get(country)};
                writer.writeNext(line, false);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
