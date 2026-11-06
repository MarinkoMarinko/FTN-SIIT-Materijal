package zadatak1;

import java.util.List;

public class Invoice {
	private int invoice;
	private String date;
	private Person billTo;
	private Person shipTo;
	private List<Product> product;
	private float tax;
	private float total;
	private String comments;
	public int getInvoice() {
		return invoice;
	}
	public void setInvoice(int invoice) {
		this.invoice = invoice;
	}
	public String getDate() {
		return date;
	}
	public void setDate(String date) {
		this.date = date;
	}
	public Person getBillTo() {
		return billTo;
	}
	public void setBillTo(Person billTo) {
		this.billTo = billTo;
	}
	public Person getShipTo() {
		return shipTo;
	}
	public void setShipTo(Person shipTo) {
		this.shipTo = shipTo;
	}
	public List<Product> getProduct() {
		return product;
	}
	public void setProduct(List<Product> product) {
		this.product = product;
	}
	public float getTax() {
		return tax;
	}
	public void setTax(float tax) {
		this.tax = tax;
	}
	public float getTotal() {
		return total;
	}
	public void setTotal(float total) {
		this.total = total;
	}
	public String getComments() {
		return comments;
	}
	public void setComments(String comments) {
		this.comments = comments;
	}
	
	@Override
	public String toString() {
	    return "Invoice [invoice=" + invoice
	            + ", date=" + date
	            + ", billTo=" + billTo
	            + ", shipTo=" + shipTo
	            + ", product=" + product
	            + ", tax=" + tax
	            + ", total=" + total
	            + ", comments=" + comments + "]";
	}
}
