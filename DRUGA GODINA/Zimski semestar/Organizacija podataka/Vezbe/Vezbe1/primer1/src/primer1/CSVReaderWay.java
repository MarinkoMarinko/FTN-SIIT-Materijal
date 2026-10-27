
package primer1;

import java.io.FileReader;
import java.io.IOException;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.exceptions.CsvValidationException;

public class CSVReaderWay {

    public static void main(String[] args) {

        CSVParser parser = new CSVParserBuilder()
                .withSeparator(',')
                .withQuoteChar('"')
                .build();

        try (CSVReader reader = new CSVReaderBuilder(
                new FileReader("drzave_gradovi.csv"))
                .withCSVParser(parser)
                .withSkipLines(1)
                .build()) {

            String[] line;
            while ((line = reader.readNext()) != null) {
            	System.out.println(String.join(",", line));
            }

        } catch (IOException | CsvValidationException e) {
            e.printStackTrace();
        }
    }
}
