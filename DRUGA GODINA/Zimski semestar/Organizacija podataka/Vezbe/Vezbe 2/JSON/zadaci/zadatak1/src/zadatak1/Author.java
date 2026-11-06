package zadatak1;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Author {
	@JsonProperty("First_Name")
	private String firstName;
	
	@JsonProperty("Last_Name")
	private String lastName;

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	
	public Author() { }
	
	@Override
	public String toString() {
		return this.firstName + " " + this.lastName;
	}
}
