
package zadatak3;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.bean.CsvToBeanBuilder;

public class Main {

    public static void main(String[] args) throws IOException {

        List<Polazak> polasci;

        try (FileReader reader = new FileReader("resources/input.csv")) {
            polasci = new CsvToBeanBuilder<Polazak>(reader)
                    .withType(Polazak.class)
                    .build()
                    .parse();
        }

        Set<Polazak> saPovratkom = new LinkedHashSet<>();
        Set<Polazak> bezPovratka = new LinkedHashSet<>();

        for (Polazak p1 : polasci) {
            boolean imaPovratak = false;

            for (Polazak p2 : polasci) {
                if (!p1.getSifraRelacije().equals(p2.getSifraRelacije()) &&
                    p1.getMestoPolaska().equals(p2.getMestoDolaska()) &&
                    p1.getMestoDolaska().equals(p2.getMestoPolaska())) {

                    imaPovratak = true;
                    break;
                }
            }

            if (imaPovratak) {
                saPovratkom.add(p1);
            } else {
                bezPovratka.add(p1);
            }
        }

        DumperOptions opts = new DumperOptions();
        opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
        opts.setIndent(4);

        Yaml yaml = new Yaml(opts);

        try (FileWriter writer = new FileWriter("resources/sa_povratkom.yaml")) {
            yaml.dump(new ArrayList<>(saPovratkom), writer);
        }

        ObjectMapper mapper = new ObjectMapper();

        mapper.writerWithDefaultPrettyPrinter()
              .writeValue(new File("resources/bez_povratka.json"), bezPovratka);
    }
}
