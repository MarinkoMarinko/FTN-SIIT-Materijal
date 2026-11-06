package zadatak4;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.bean.CsvToBeanBuilder;

public class Main {

	public static void main(String[] args) throws IOException {
		LinkedHashMap<String, String> yamlData = new LinkedHashMap<String, String>();
		yamlData.put("Polazna stanica", "Beograd");
		yamlData.put("Dolazna stanica", "Novi Sad");
		yamlData.put("Vreme polaska", "07:30");
		
		DumperOptions opts = new DumperOptions();
		opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
		opts.setIndent(4);
		Yaml yaml = new Yaml(opts);
		try (FileWriter writer = new FileWriter("resources/search_parameters.yaml")) {
			yaml.dump(yamlData, writer);
		}
		
		List<Polazak> polasci;
		try (FileReader reader = new FileReader("resources/input.csv")) {
			polasci = new CsvToBeanBuilder<Polazak>(reader)
					.withType(Polazak.class)
					.build()
					.parse();
		}
		
		Map<String, String> searchData;
		try (FileReader reader = new FileReader("resources/search_parameters.yaml")) {
			searchData = (Map<String, String>) yaml.load(reader);
		}
		List<Polazak> rezultat = new ArrayList<Polazak>();
		
		for (Polazak p: polasci) {
			if (p.getMestoPolaska().equals(searchData.get("Polazna stanica")) &&
				p.getMestoDolaska().equals(searchData.get("Dolazna stanica")) &&
				p.getVremePolaska().equals(searchData.get("Vreme polaska"))) {
				
				rezultat.add(p);
			}
		}
		
		ObjectMapper mapper = new ObjectMapper();
		try (FileWriter writer = new FileWriter("resources/output.json")) {
			mapper.writerWithDefaultPrettyPrinter().writeValue(writer, rezultat);
		}
	}

}
