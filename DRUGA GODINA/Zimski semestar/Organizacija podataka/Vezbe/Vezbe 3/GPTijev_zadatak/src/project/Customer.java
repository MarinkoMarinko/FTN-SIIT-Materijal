package project;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Customer {
	@JsonProperty("ime")
	private String name;
	
	@JsonProperty("grad")
	private String city;
	
	public Customer() { }

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}
}
