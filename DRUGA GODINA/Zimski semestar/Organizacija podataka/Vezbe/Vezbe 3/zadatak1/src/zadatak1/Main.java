
package zadatak1;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.CSVWriter;
import com.opencsv.bean.CsvToBeanBuilder;

public class Main {

    public static void main(String[] args) throws IOException {
        String datum = "2026-11-02";

        Polazak[] polasci = new Polazak[] {
            new Polazak("R01", "Novi Sad", "Beograd", datum, "06:00", "07:30", "P1", 800, 30),
            new Polazak("R01", "Novi Sad", "Beograd", datum, "09:00", "10:30", "P2", 800, 35),
            new Polazak("R01", "Novi Sad", "Beograd", datum, "13:00", "14:30", "P1", 800, 27),
            new Polazak("R01", "Novi Sad", "Beograd", datum, "17:00", "18:30", "P3", 800, 40),
            new Polazak("R02", "Beograd", "Novi Sad", datum, "07:30", "09:00", "P1", 800, 25),
            new Polazak("R02", "Beograd", "Novi Sad", datum, "12:00", "13:30", "P2", 800, 32),
            new Polazak("R02", "Beograd", "Novi Sad", datum, "18:00", "19:30", "P1", 800, 38),
            new Polazak("R03", "Novi Sad", "Subotica", datum, "07:00", "08:45", "P4", 1100, 22),
            new Polazak("R03", "Novi Sad", "Subotica", datum, "12:00", "13:45", "P4", 1100, 28),
            new Polazak("R03", "Novi Sad", "Subotica", datum, "18:00", "19:45", "P5", 1100, 30),
            new Polazak("R04", "Subotica", "Novi Sad", datum, "09:00", "10:45", "P2", 1100, 20),
            new Polazak("R04", "Subotica", "Novi Sad", datum, "16:00", "17:45", "P3", 1100, 26),
            new Polazak("R05", "Novi Sad", "Zrenjanin", datum, "08:00", "09:00", "P6", 600, 18),
            new Polazak("R05", "Novi Sad", "Zrenjanin", datum, "14:00", "15:00", "P6", 600, 24),
            new Polazak("R05", "Novi Sad", "Zrenjanin", datum, "19:00", "20:00", "P7", 600, 21)
        };

        try (CSVWriter writer = new CSVWriter(
                new FileWriter("resources/input.csv"),
                ',',
                CSVWriter.NO_QUOTE_CHARACTER,
                CSVWriter.DEFAULT_ESCAPE_CHARACTER,
                CSVWriter.DEFAULT_LINE_END
        )) {
            String[] header = {
                "sifra relacije",
                "mesto polaska",
                "mesto dolaska",
                "datum polaska",
                "vreme polaska",
                "planirano vreme dolaska",
                "stanicni peron polaska",
                "cena karte",
                "broj prodatih karata"
            };

            writer.writeNext(header);

            for (Polazak p : polasci) {
                String[] line = new String[] {
                    p.getSifraRelacije(),
                    p.getMestoPolaska(),
                    p.getMestoDolaska(),
                    p.getDatumPolaska(),
                    p.getVremePolaska(),
                    p.getPlanVremeDolaska(),
                    p.getPeron(),
                    String.valueOf(p.getCena()),
                    String.valueOf(p.getBrKarata())
                };

                writer.writeNext(line);
            }
        }

        List<Polazak> polasci_new;

        try (FileReader reader = new FileReader("resources/input.csv")) {
            polasci_new = new CsvToBeanBuilder<Polazak>(reader)
                    .withType(Polazak.class)
                    .build()
                    .parse();
        }

        LinkedHashMap<String, List<Polazak>> relacije = new LinkedHashMap<>();

        for (Polazak p : polasci_new) {
            if (!relacije.containsKey(p.getSifraRelacije())) {
                relacije.put(p.getSifraRelacije(), new ArrayList<>());
            }
            relacije.get(p.getSifraRelacije()).add(p);
        }

        ObjectMapper mapper = new ObjectMapper();
        mapper.writerWithDefaultPrettyPrinter()
              .writeValue(new File("resources/output.json"), relacije);
    }
}
