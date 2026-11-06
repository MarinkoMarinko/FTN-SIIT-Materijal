package code;


import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.databind.ObjectMapper;

public class DrugiNacin {

    public static void main(String[] args) throws IOException {

        ObjectMapper mapper = new ObjectMapper();

        // 1. Ucitavanje JSON-a
        Book book = mapper.readValue(
            new File("resources/books.json"),
            Book.class
        );

        // 2. Ispis podataka
        System.out.println(book.getTitle());
        System.out.println(book.getPrice());
        System.out.println(book.getAuthor().getFirstName());

        // 3. Izmena podataka
        book.setTitle("New Book Title");
        book.setPrice(100);
        book.getAuthor().setFirstName("Marko");

        // 4. Cuvanje izmena
        mapper.writerWithDefaultPrettyPrinter().writeValue(
            new File("resources/Books_changed.json"),
            book
        );
    }
}
