package code;

import java.io.File;
import java.io.IOException;
import java.util.Map;

import com.fasterxml.jackson.databind.ObjectMapper;

public class PrviNacin {

    public static void main(String[] args) throws IOException {

        ObjectMapper mapper = new ObjectMapper();

        // 1. Ucitavanje JSON datoteke
        Map<String, Object> book = mapper.readValue(
            new File("resources/books.json"),
            Map.class
        );

        // 2. Ispis podataka
        System.out.println(book);

        // 3. Izmena podataka
        book.put("Title", "New Book Title");
        book.put("Price", 100);

        // 4. Cuvanje izmena u novi JSON
        mapper.writerWithDefaultPrettyPrinter().writeValue(
            new File("resources/Books_changed.json"),
            book
        );
    }
}
