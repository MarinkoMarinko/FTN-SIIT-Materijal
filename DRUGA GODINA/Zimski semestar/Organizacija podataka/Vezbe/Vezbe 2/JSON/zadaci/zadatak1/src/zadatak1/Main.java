package zadatak1;

import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {

    public static void main(String[] args) throws IOException {

        ObjectMapper mapper = new ObjectMapper();

        Bookstore bookstore = mapper.readValue(
            new File("resources/bookstore.json"),
            Bookstore.class
        );

        for(Book b: bookstore.getBooks()) {
        	System.out.println(b);
        }
        
        for(Magazine m: bookstore.getMagazines()) {
        	System.out.println(m);
        }
    }
}
