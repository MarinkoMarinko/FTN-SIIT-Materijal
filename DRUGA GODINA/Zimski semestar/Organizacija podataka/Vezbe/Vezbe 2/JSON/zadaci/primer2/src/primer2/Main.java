package primer2;


import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.core.JsonEncoding;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonToken;

public class Main {

    private static final String FILE =
        "resources/Book_generated.json";

    public static void main(String[] args) throws IOException {
        generateJSON();
        parseJSON();
    }

    public static void generateJSON() throws IOException {

        JsonFactory factory = new JsonFactory();

        try (JsonGenerator generator = factory.createGenerator(
                new File(FILE), JsonEncoding.UTF8)) {

            generator.useDefaultPrettyPrinter();

            generator.writeStartObject();

            generator.writeObjectFieldStart("Author");
            generator.writeStringField("First_Name", "Stephen");
            generator.writeStringField("Last_Name", "King");
            generator.writeEndObject();

            generator.writeStringField("Title", "The Green Mile");

            generator.writeEndObject();
        }
    }

    public static void parseJSON() throws IOException {

        JsonFactory factory = new JsonFactory();

        try (JsonParser parser =
                factory.createParser(new File(FILE))) {

            String firstName = null;
            String lastName = null;
            String title = null;

            parser.nextToken();

            while (parser.nextToken() != JsonToken.END_OBJECT) {

                String fieldName = parser.getCurrentName();
                parser.nextToken();

                if ("Author".equals(fieldName)) {

                    while (parser.nextToken() != JsonToken.END_OBJECT) {

                        String nameField = parser.getCurrentName();
                        parser.nextToken();

                        if ("First_Name".equals(nameField)) {
                            firstName = parser.getText();
                        } else if ("Last_Name".equals(nameField)) {
                            lastName = parser.getText();
                        }
                    }

                } else if ("Title".equals(fieldName)) {
                    title = parser.getText();
                }
            }

            System.out.println("Autor: " + firstName + " " + lastName);
            System.out.println("Knjiga: " + title);
        }
    }
}
