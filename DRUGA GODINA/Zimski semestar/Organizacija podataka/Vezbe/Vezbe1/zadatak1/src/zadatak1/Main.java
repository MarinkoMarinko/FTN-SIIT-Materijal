package zadatak1;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Reader;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;

import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVWriter;
import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;



public class Main {
	public static void upisiCSV(List<Tacka> tacke, String naziv) throws IOException {
		try (CSVWriter cw = new CSVWriter(
		        new FileWriter(naziv),
		        '#',
		        CSVWriter.DEFAULT_QUOTE_CHARACTER,
		        CSVWriter.DEFAULT_ESCAPE_CHARACTER,
		        CSVWriter.DEFAULT_LINE_END)) {

		    cw.writeNext(new String[] {"x", "y", "z", "d"}, false);
		    
		    for (Tacka t: tacke) {
		    	String[] line = {
		    			String.valueOf(t.getX()),
		    			String.valueOf(t.getY()),
		    			String.valueOf(t.getZ()),
		    			String.format(Locale.US, "%.3f", t.calculateDistance())
		    	};
		    	cw.writeNext(line, false);
		    }
		}
	}
	
	public static void main(String[] args) {
		try (Reader r = new FileReader("input.csv")) {
			CsvToBean<Tacka> csvToBean = new CsvToBeanBuilder<Tacka>(r)
					.withType(Tacka.class)
					.build();
			List<Tacka> tacke = csvToBean.parse();
			
			for (Tacka t: tacke) {
				System.out.println(t);
			}
			
			upisiCSV(tacke, "output_a.csv");
			
			tacke.sort((t1, t2) -> 
				Double.compare(t2.calculateDistance(), t1.calculateDistance())
			);
			
			upisiCSV(tacke, "output_b.csv");
		}
		catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		

	}

}
