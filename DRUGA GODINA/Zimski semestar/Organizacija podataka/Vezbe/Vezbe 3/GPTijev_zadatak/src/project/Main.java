package project;

/* Ovaj zadatak je napisao chatGPT.
Iskreno, previse je iskomplikovao i ne verujem da biste stigli ovo za 1h:30min.
Ovo sam uradio cisto da izvezbam citanje iz svih tipova (CSV, JSON, YAML)
i upis u sve tipove (CSV, JSON, YAML).
Pozdrav :D.
*/

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

import org.yaml.snakeyaml.Yaml;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;
import com.opencsv.CSVWriter;

public class Main {

    public static void main(String[] args) throws IOException {

        // 1. CITANJE JSON-a

        Order[] orders;
        ObjectMapper mapper = new ObjectMapper();

        try (FileReader reader = new FileReader("resources/porudzbine.json")) {
            orders = mapper.readValue(reader, Order[].class);
        }

        // 2. CITANJE CSV-a

        LinkedHashMap<String, Integer> sales = new LinkedHashMap<>();

        CSVParser parser = new CSVParserBuilder()
                .withSeparator('#')
                .build();

        try (CSVReader reader = new CSVReaderBuilder(
                new FileReader("resources/popusti.csv"))
                .withSkipLines(1)
                .withCSVParser(parser)
                .build()) {

            String[] line;

            while ((line = reader.readNext()) != null) {
                sales.put(line[0], Integer.parseInt(line[1]));
            }
        }

        // 3. CITANJE YAML-a

        Map<String, Map<String, Integer>> settings;
        Yaml yaml = new Yaml();

        try (FileReader reader = new FileReader("resources/podesavanja.yaml")) {
            settings = (Map<String, Map<String, Integer>>) yaml.load(reader);
        }

        int freeDeliveryLimit = settings.get("dostava").get("prag_besplatne_dostave");
        int deliveryPrice = settings.get("dostava").get("cena_dostave");
        int bigDeliveryLimit = settings.get("analiza").get("prag_velike_porudzbine");

        // 4. OBRADA PORUDZBINA

        List<OrderResult> orderResults = new ArrayList<>();

        for (Order O : orders) {

            double startingPrice = 0;
            double totalSale = 0;

            for (Item I : O.getItems()) {
                startingPrice += I.getAmount() * I.getPrice();

                double itemSale = sales.getOrDefault(I.getCategory(), 0);

                totalSale += I.getAmount() * I.getPrice() * (itemSale / 100);
            }

            double priceAfterSale = startingPrice - totalSale;

            double currDeliveryPrice = 0;

            if (priceAfterSale < freeDeliveryLimit) {
                currDeliveryPrice = deliveryPrice;
            }

            double totalPrice = priceAfterSale + currDeliveryPrice;
            boolean isBigOrder = totalPrice >= bigDeliveryLimit;

            orderResults.add(new OrderResult(
                    O.getId(),
                    O.getCustomer().getName(),
                    O.getCustomer().getCity(),
                    startingPrice,
                    totalSale,
                    currDeliveryPrice,
                    totalPrice,
                    isBigOrder
            ));
        }

        // 5. SORTIRANJE

        orderResults.sort(
                Comparator.comparingDouble(OrderResult::getTotalPrice).reversed()
        );

        // 6. UPIS U CSV

        try (CSVWriter writer = new CSVWriter(
                new FileWriter("resources/obracunate_porudzbine.csv"),
                '#',
                CSVWriter.DEFAULT_QUOTE_CHARACTER,
                CSVWriter.DEFAULT_ESCAPE_CHARACTER,
                CSVWriter.DEFAULT_LINE_END)) {

            writer.writeNext(new String[]{
                    "sifra", "kupac", "grad", "pocetnaCena",
                    "ukupanPopust", "dostava", "konacnaCena", "velika"
            }, false);

            for (OrderResult O : orderResults) {

                String[] line = new String[]{
                        O.getCode(),
                        O.getCustomer(),
                        O.getCity(),
                        String.format(Locale.US, "%.2f", O.getStartingPrice()),
                        String.format(Locale.US, "%.2f", O.getTotalSale()),
                        String.format(Locale.US, "%.2f", O.getDeliveryPrice()),
                        String.format(Locale.US, "%.2f", O.getTotalPrice()),
                        String.valueOf(O.isBigOrder())
                };

                writer.writeNext(line, false);
            }
        }

        // 7. GRUPISANJE PORUDZBINA PO GRADOVIMA

        LinkedHashMap<String, List<OrderResult>> cities = new LinkedHashMap<>();

        for (OrderResult O : orderResults) {
            cities.putIfAbsent(O.getCity(), new ArrayList<>());
            cities.get(O.getCity()).add(O);
        }

        // 8. FORMIRANJE JSON STRUKTURE

        LinkedHashMap<String, Object> gradovi = new LinkedHashMap<>();
        LinkedHashMap<String, Double> cityRevenues = new LinkedHashMap<>();

        for (String city : cities.keySet()) {

            double cityRevenue = 0;
            List<Map<String, Object>> cityOrders = new ArrayList<>();

            for (OrderResult O : cities.get(city)) {

                cityRevenue += O.getTotalPrice();

                Map<String, Object> order = new LinkedHashMap<>();

                order.put("sifra", O.getCode());
                order.put("kupac", O.getCustomer());
                order.put("konacnaCena", O.getTotalPrice());
                order.put("velika", O.isBigOrder());

                cityOrders.add(order);
            }

            Map<String, Object> cityData = new LinkedHashMap<>();

            cityData.put("ukupanPrihod", cityRevenue);
            cityData.put("porudzbine", cityOrders);

            gradovi.put(city, cityData);
            cityRevenues.put(city, cityRevenue);
        }

        // 9. UPIS U JSON

        Map<String, Object> root = new LinkedHashMap<>();
        root.put("gradovi", gradovi);

        try (FileWriter writer = new FileWriter("resources/porudzbine_po_gradovima.json")) {
            mapper.writerWithDefaultPrettyPrinter().writeValue(writer, root);
        }

        // 10. RACUNANJE STATISTIKE ZA YAML

        int totalOrders = orderResults.size();
        double totalRevenue = 0;
        int bigOrders = 0;

        for (OrderResult O : orderResults) {

            totalRevenue += O.getTotalPrice();

            if (O.isBigOrder()) {
                bigOrders++;
            }
        }

        double averageRevenue = totalOrders == 0 ? 0 : totalRevenue / totalOrders;

        // Grad sa najvecim prihodom

        String bestCity = "";
        double maxCityRevenue = 0;

        for (String city : cityRevenues.keySet()) {

            if (cityRevenues.get(city) > maxCityRevenue) {
                maxCityRevenue = cityRevenues.get(city);
                bestCity = city;
            }
        }

        // Najskuplja porudzbina (lista je vec sortirana)

        Map<String, Object> mostExpensive = new LinkedHashMap<>();

        if (!orderResults.isEmpty()) {
            OrderResult maxOrder = orderResults.get(0);

            mostExpensive.put("sifra", maxOrder.getCode());
            mostExpensive.put("konacna_cena", maxOrder.getTotalPrice());
        }

        // 11. FORMIRANJE YAML STRUKTURE

        Map<String, Object> statistics = new LinkedHashMap<>();

        statistics.put("ukupan_broj_porudzbina", totalOrders);
        statistics.put("ukupan_prihod", totalRevenue);
        statistics.put("prosecna_vrednost_porudzbine", averageRevenue);
        statistics.put("broj_velikih_porudzbina", bigOrders);
        statistics.put("grad_sa_najvecim_prihodom", bestCity);
        statistics.put("najskuplja_porudzbina", mostExpensive);

        Map<String, Object> yamlRoot = new LinkedHashMap<>();
        yamlRoot.put("statistika", statistics);

        // 12. UPIS U YAML

        try (FileWriter writer = new FileWriter("resources/statistika.yaml")) {
            yaml.dump(yamlRoot, writer);
        }
    }
}
