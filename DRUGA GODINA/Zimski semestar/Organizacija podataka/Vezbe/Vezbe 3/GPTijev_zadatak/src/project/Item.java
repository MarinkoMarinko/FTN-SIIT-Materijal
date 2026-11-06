package project;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Item {
	@JsonProperty("naziv")
	private String name;
	
	@JsonProperty("kategorija")
	private String category;
	
	@JsonProperty("kolicina")
	private int amount;
	
	@JsonProperty("cena")
	private int price;
	
	public Item() { }

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCategory() {
		return category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public int getAmount() {
		return amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}
}
