package code;


import java.util.List;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Book {

    @JsonProperty("ISBN")
    private String isbn;

    @JsonProperty("Price")
    private int price;

    @JsonProperty("Edition")
    private int edition;

    @JsonProperty("Title")
    private String title;

    @JsonProperty("Author")
    private Author author;

    @JsonProperty("Tags")
    private List<String> tags;

    public Book() {
    }

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public int getEdition() {
        return edition;
    }

    public void setEdition(int edition) {
        this.edition = edition;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Author getAuthor() {
        return author;
    }

    public void setAuthor(Author author) {
        this.author = author;
    }

    public List<String> getTags() {
        return tags;
    }

    public void setTags(List<String> tags) {
        this.tags = tags;
    }
}