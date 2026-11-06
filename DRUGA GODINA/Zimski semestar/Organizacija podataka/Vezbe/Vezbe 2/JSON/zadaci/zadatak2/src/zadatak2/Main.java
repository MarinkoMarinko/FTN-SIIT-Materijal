package zadatak2;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.bean.CsvToBeanBuilder;

public class Main {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		List<Country> countries;
		try(FileReader reader = new FileReader("resources/countries_cities.csv")) {
			countries = new CsvToBeanBuilder<Country>(reader)
					.withType(Country.class)
					.build()
					.parse();
		}
		
		Map<String, List<Country>> continents = new LinkedHashMap<String, List<Country>>();
		for (Country c: countries) {
			String continent = c.getContinentName();
			if (!continents.containsKey(continent)) {
				continents.put(continent, new ArrayList<>());
			}
			continents.get(continent).add(c);
		}
		
		ObjectMapper mapper = new ObjectMapper();
		
		File output = new File("output");
		output.mkdir();
		
		for (String continent: continents.keySet()) {
			mapper.writerWithDefaultPrettyPrinter().writeValue(
				new File(output, continent + ".json"),
				continents.get(continent)
			);
		}
	}

}
