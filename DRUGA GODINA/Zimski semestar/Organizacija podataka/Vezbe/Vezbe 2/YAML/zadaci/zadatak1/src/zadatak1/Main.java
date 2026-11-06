package zadatak1;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Map;
import java.util.Scanner;

import org.yaml.snakeyaml.Yaml;
import org.yaml.snakeyaml.LoaderOptions;
import org.yaml.snakeyaml.DumperOptions;
import org.yaml.snakeyaml.constructor.Constructor;

public class Main {

    public static void main(String[] args) throws IOException {

        // Ucitavanje fakture
        Yaml yamlInvoice = new Yaml(
            new Constructor(Invoice.class, new LoaderOptions())
        );

        Invoice invoice;

        try (FileReader reader = new FileReader("resources/invoice.yaml")) {
            invoice = yamlInvoice.load(reader);
        }

        // Ucitavanje kurseva
        Yaml yamlExchange = new Yaml();

        Map<String, Double> exchange;

        try (FileReader reader = new FileReader("resources/exchange.yaml")) {
            exchange = yamlExchange.load(reader);
        }

        // Izbor valute
        System.out.println("Dostupne valute:");

        for (String valuta : exchange.keySet()) {
            System.out.println(valuta);
        }

        String valuta;

        try (Scanner sc = new Scanner(System.in)) {
            do {
                System.out.print("Izaberite valutu: ");
                valuta = sc.nextLine().trim().toUpperCase();
            } while (!exchange.containsKey(valuta));
        }

        float kurs = exchange.get(valuta).floatValue();

        // Konverzija cena proizvoda
        for (Product p : invoice.getProduct()) {
            float novaCena = Math.round(
                p.getPrice() * kurs * 100
            ) / 100f;

            p.setPrice(novaCena);
        }

        // Konverzija poreza
        invoice.setTax(
            Math.round(invoice.getTax() * kurs * 100) / 100f
        );

        // Konverzija ukupnog iznosa
        invoice.setTotal(
            Math.round(invoice.getTotal() * kurs * 100) / 100f
        );

        // Zapisivanje u YAML
        DumperOptions opts = new DumperOptions();
        opts.setIndent(4);
        opts.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);

        Yaml yamlOutput = new Yaml(opts);

        String path = "resources/invoice_" + valuta + ".yaml";

        try (FileWriter writer = new FileWriter(path)) {
            yamlOutput.dump(invoice, writer);
        }

        System.out.println("Faktura je sacuvana u: " + path);
    }
}
