package zadatak1;

public class Product {
	private String sku;
	private int quantity;
	private String description;
	private float price;
	
	public Product() { }

	public String getSku() {
		return sku;
	}

	public void setSku(String sku) {
		this.sku = sku;
	}

	public int getQuantity() {
		return quantity;
	}

	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public float getPrice() {
		return price;
	}

	public void setPrice(float price) {
		this.price = price;
	}
	
	@Override
	public String toString() {
	    return "Product [sku=" + sku
	            + ", quantity=" + quantity
	            + ", description=" + description
	            + ", price=" + price + "]";
	}
}
