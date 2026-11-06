package zadatak1;

public class Person {
	private String given;
	private String family;
	private Address address;
	
	public Person() { }

	public String getGiven() {
		return given;
	}

	public void setGiven(String given) {
		this.given = given;
	}

	public String getFamily() {
		return family;
	}

	public void setFamily(String family) {
		this.family = family;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}
	
	@Override
	public String toString() {
	    return "Person [given=" + given
	            + ", family=" + family
	            + ", address=" + address + "]";
	}
}
