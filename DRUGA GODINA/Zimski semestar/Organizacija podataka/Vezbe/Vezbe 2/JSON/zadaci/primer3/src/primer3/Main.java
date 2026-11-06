package primer3;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

public class Main {

    public static void main(String[] args) throws IOException {

        ObjectMapper mapper = new ObjectMapper();

        // 1. Ucitavanje JSON-a
        JsonNode root = mapper.readTree(
            new File("resources/books.json")
        );

        // 2. Citanje podataka
        String title = root.get("Title").asText();

        JsonNode author = root.get("Author");

        String firstName = author.get("First_Name").asText();
        String lastName = author.get("Last_Name").asText();

        System.out.println("Autor: " + firstName + " " + lastName);
        System.out.println("Naslov: " + title);

        // 3. Izmena naslova knjige
        ObjectNode book = (ObjectNode) root;
        book.put("Title", "New Book Title");

        // 4. Cuvanje izmena
        mapper.writerWithDefaultPrettyPrinter().writeValue(
            new File("resources/Books_changed.json"),
            root
        );
    }
}
