package zadatak1;


import java.util.List;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Bookstore {

    @JsonProperty("Books")
    private List<Book> books;

    @JsonProperty("Magazines")
    private List<Magazine> magazines;

    public Bookstore() {
    }

    public List<Book> getBooks() {
        return books;
    }

    public void setBooks(List<Book> books) {
        this.books = books;
    }

    public List<Magazine> getMagazines() {
        return magazines;
    }

    public void setMagazines(List<Magazine> magazines) {
        this.magazines = magazines;
    }

    @Override
    public String toString() {
        return "Bookstore{" +
                "books=" + books +
                ", magazines=" + magazines +
                "}";
    }
}
