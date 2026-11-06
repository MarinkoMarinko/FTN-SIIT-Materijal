package zadatak2;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.Duration;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import com.opencsv.bean.CsvToBeanBuilder;

public class Main {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		List<Polazak> polasci;
		try (FileReader reader =  new FileReader("resources/input.csv")) {
			polasci = new CsvToBeanBuilder<Polazak>(reader)
					.withType(Polazak.class)
					.build().parse();
		}
		
		LinkedHashMap<String, List<Polazak>> relacije = new LinkedHashMap<String, List<Polazak>>();
		for (Polazak p: polasci) {
			if (!relacije.containsKey(p.getSifraRelacije())) {
				relacije.put(p.getSifraRelacije(), new ArrayList<Polazak>());
			}
			relacije.get(p.getSifraRelacije()).add(p);
		}
		
		String maxPolazak = "";
		int maxNumPolazak = 0;
		for (String polazakId: relacije.keySet()) {
			if (relacije.get(polazakId).size() > maxNumPolazak) {
				maxNumPolazak = relacije.get(polazakId).size();
				maxPolazak = polazakId;
			}
		}
		
		String longestPolazak = "";
		long maxTime = 0;
		for (String polazakId: relacije.keySet()) {
			long currTime = 0;
			for (Polazak p: relacije.get(polazakId)) {
				LocalTime start = LocalTime.parse(p.getVremePolaska());
				LocalTime end = LocalTime.parse(p.getPlanVremeDolaska());
				long duration = Duration.between(start, end).toMinutes();
				if(duration < 0) {
					duration += 60 * 24;
				}
				currTime += duration;
			}
			if (currTime > maxTime) {
				maxTime = currTime;
				longestPolazak = polazakId;
			}
		}
		
		String costiestPolazak = "";
		long maxCost = 0;
		for (String polazakId: relacije.keySet()) {
			long currCost = 0;
			for (Polazak p: relacije.get(polazakId)) {
				currCost += (long) p.getCena() * p.getBrKarata();
			}
			if (currCost > maxCost) {
				maxCost = currCost;
				costiestPolazak = polazakId;
			}
		}
		
		LinkedHashMap<String, String> output = new LinkedHashMap<String, String>();
		output.put("Relacija sa najvise polazaka", maxPolazak);
		output.put("Relacija sa najduzim ukupnim vremenom putovanja", longestPolazak);
		output.put("Relacija koja je najisplativija", costiestPolazak);
		
		
		DumperOptions options = new DumperOptions();
		options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
		options.setIndent(4);
		options.setWidth(50);
		Yaml yaml = new Yaml(options);
		try (FileWriter writer = new FileWriter("resources/output.yaml")) {
			yaml.dump(output, writer);
		}
	}

}
