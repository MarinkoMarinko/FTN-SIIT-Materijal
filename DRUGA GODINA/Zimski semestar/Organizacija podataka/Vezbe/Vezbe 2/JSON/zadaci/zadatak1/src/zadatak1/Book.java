package zadatak1;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;


import java.util.List;
import com.fasterxml.jackson.annotation.JsonProperty;

public class Book {

    @JsonProperty("ISBN")
    private String isbn;

    @JsonProperty("Price")
    private int price;

    @JsonProperty("Edition")
    private Integer edition;

    @JsonProperty("Title")
    private String title;

    @JsonProperty("Authors")
    private List<Author> authors;

    @JsonProperty("Tags")
    private List<String> tags;

    @JsonProperty("Remark")
    private String remark;

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

    public Integer getEdition() {
        return edition;
    }

    public void setEdition(Integer edition) {
        this.edition = edition;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<Author> getAuthors() {
        return authors;
    }

    public void setAuthors(List<Author> authors) {
        this.authors = authors;
    }

    public List<String> getTags() {
        return tags;
    }

    public void setTags(List<String> tags) {
        this.tags = tags;
    }

    public String getRemark() {
        return remark;
    }

    public void setRemark(String remark) {
        this.remark = remark;
    }
    

	@Override
	public String toString() {
	    return "Book{" +
	            "isbn='" + isbn + '\'' +
	            ", price=" + price +
	            ", edition=" + edition +
	            ", title='" + title + '\'' +
	            ", authors=" + authors +
	            ", tags=" + tags +
	            ", remark='" + remark + '\'' +
	            '}';
	}

}
