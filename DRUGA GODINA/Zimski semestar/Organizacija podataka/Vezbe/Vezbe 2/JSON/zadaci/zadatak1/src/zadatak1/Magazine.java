package zadatak1;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Magazine {
	@JsonProperty("Title")
	private String title;
	
	@JsonProperty("Month")
	private String month;
	
	@JsonProperty("Year")
	private int year;
	
	public Magazine() { }

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getMonth() {
		return month;
	}

	public void setMonth(String month) {
		this.month = month;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}
	
	@Override
    public String toString() {
        return "Magazine{" +
                "title='" + title + "'" +
                ", month='" + month + "'" +
                ", year=" + year +
                "}";
    }
}
