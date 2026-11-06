package zadatak5;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.CSVWriter;

public class Main {

    public static void main(String[] args) throws IOException {
        Iznajmljivanje[] podaci = new Iznajmljivanje[] {

            new Iznajmljivanje("I01", "Novi Sad", "2026-05-03", "2026-05-06",
                    180, 3000, 3, new Osoba("Marko", "Markovic", "0101998000001")),

            new Iznajmljivanje("I02", "Beograd", "2026-05-08", "2026-05-10",
                    120, 3500, 2, new Osoba("Jovan", "Jovanovic", "0202999000002")),

            new Iznajmljivanje("I03", "Novi Sad", "2026-05-18", "2026-05-23",
                    450, 3000, 5, new Osoba("Marko", "Markovic", "0101998000001")),

            new Iznajmljivanje("I04", "Subotica", "2026-06-02", "2026-06-06",
                    320, 4000, 4, new Osoba("Ana", "Petrovic", "0303000000003")),

            new Iznajmljivanje("I05", "Beograd", "2026-06-10", "2026-06-11",
                    80, 3500, 1, new Osoba("Jovan", "Jovanovic", "0202999000002")),

            new Iznajmljivanje("I06", "Novi Sad", "2026-06-20", "2026-06-27",
                    650, 3000, 7, new Osoba("Petar", "Nikolic", "0404997000004")),

            new Iznajmljivanje("I07", "Beograd", "2026-07-03", "2026-07-06",
                    270, 3500, 3, new Osoba("Ana", "Petrovic", "0303000000003")),

            new Iznajmljivanje("I08", "Subotica", "2026-07-12", "2026-07-15",
                    210, 4000, 3, new Osoba("Marko", "Markovic", "0101998000001")),

            new Iznajmljivanje("I09", "Novi Sad", "2026-10-28", null,
                    null, 3000, 5, new Osoba("Petar", "Nikolic", "0404997000004")),

            new Iznajmljivanje("I10", "Beograd", "2026-11-01", null,
                    null, 3500, 2, new Osoba("Jovan", "Jovanovic", "0202999000002"))
        };
        
        ObjectMapper mapper = new ObjectMapper();
        try (FileWriter writer = new FileWriter("resources/input.json")) {
        	mapper.writerWithDefaultPrettyPrinter().writeValue(writer, podaci);
        }
        
        
        Iznajmljivanje[] iznajmljivanja;
        try (FileReader reader = new FileReader("resources/input.json")) {
        	iznajmljivanja = mapper.readValue(reader, Iznajmljivanje[].class);
        }
        
        String line;
        try (Scanner sc = new Scanner(System.in)) {
        	System.out.print("Unesite mesec i godinu (mm.yyyy): ");
        	line = sc.nextLine();
        }
        
        String[] tokens = line.split("\\.");
        int month = Integer.parseInt(tokens[0]);
        int year = Integer.parseInt(tokens[1]);
        
        List<Iznajmljivanje> foundIznajmljivanja = new ArrayList<Iznajmljivanje>();
        for (Iznajmljivanje I: iznajmljivanja) {
        	LocalDate date = LocalDate.parse(I.getDatumIznajmljivanja());
        	if (date.getMonthValue() == month && date.getYear() == year) {
        		foundIznajmljivanja.add(I);
        	}
        }
        
        DumperOptions opts = new DumperOptions();
        opts.setIndent(4);
        opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
        Yaml yaml = new Yaml();
        try (FileWriter writer = new FileWriter("resources/searched_iznajmljivanja.yaml")) {
        	yaml.dump(foundIznajmljivanja, writer);
        }
        
        LinkedHashMap<String, List<Iznajmljivanje>> groupByPerson = new LinkedHashMap<String, List<Iznajmljivanje>>();
        for (Iznajmljivanje I: iznajmljivanja) {
        	if (!groupByPerson.containsKey(I.getIznajmljivac().getMaticniBroj())) {
        		groupByPerson.put(I.getIznajmljivac().getMaticniBroj(), new ArrayList<Iznajmljivanje>());
        	}
        	groupByPerson.get(I.getIznajmljivac().getMaticniBroj()).add(I);
        }
        
        try (CSVWriter writer = new CSVWriter(
        		new FileWriter("resources/customer_analytics.csv"), 
        		CSVWriter.DEFAULT_SEPARATOR,
        		CSVWriter.NO_QUOTE_CHARACTER,
        		CSVWriter.DEFAULT_ESCAPE_CHARACTER,
        		CSVWriter.DEFAULT_LINE_END)) {
        	writer.writeNext(new String[] {"Ime", "Prezime", "Maticni broj", "Ukupan trosak", "Prosecan broj dana"});
        	for (String id: groupByPerson.keySet()) {
        		List<Iznajmljivanje> currIznajmljivanja = groupByPerson.get(id);
        		int spentSum = 0;
        		int totalDays = 0;
        		for (Iznajmljivanje I: currIznajmljivanja) {
        			spentSum += I.getCenaZaDan() * I.getBrojDana();
        			totalDays += I.getBrojDana();
        		}
        		Osoba O = currIznajmljivanja.get(0).getIznajmljivac();
        		String[] data = new String[] {
        				O.getIme(),
        				O.getPrezime(),
        				O.getMaticniBroj(),
        				String.valueOf(spentSum),
        				String.format(Locale.US, "%.2f", (double) totalDays / currIznajmljivanja.size())
        		};
        		writer.writeNext(data);
        	}
        }
        
        List<Iznajmljivanje> vracena = new ArrayList<Iznajmljivanje>();
    	for (Iznajmljivanje I: iznajmljivanja) {
    		if (I.getDatumVracanja() != null && I.getPredjenoKilometara() != null) {
    			vracena.add(I);
    		}
    	}
    	
    	vracena.sort((a, b) -> 
    		Integer.compare(b.getPredjenoKilometara(), a.getPredjenoKilometara())
    	);
    	
    	try (FileWriter writer = new FileWriter("resources/sorted_istrosenost")) {
    		mapper.writerWithDefaultPrettyPrinter().writeValue(writer, vracena);
    	}
    }
}