package project;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Order {
	@JsonProperty("sifra")
	private String id;
	
	@JsonProperty("kupac")
	private Customer customer;
	
	@JsonProperty("stavke")
	private List<Item> items;
	
	public Order() { }

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Customer getCustomer() {
		return customer;
	}

	public void setCustomer(Customer customer) {
		this.customer = customer;
	}

	public List<Item> getItems() {
		return items;
	}

	public void setItems(List<Item> items) {
		this.items = items;
	}
}
