package project;

public class OrderResult {
    private String code;
    private String customer;
    private String city;
    private double startingPrice;
    private double totalSale;
    private double deliveryPrice;
    private double totalPrice;
    private boolean bigOrder;

    public OrderResult(String code, String customer, String city,
                       double startingPrice, double totalSale,
                       double deliveryPrice, double totalPrice,
                       boolean bigOrder) {
        this.code = code;
        this.customer = customer;
        this.city = city;
        this.startingPrice = startingPrice;
        this.totalSale = totalSale;
        this.deliveryPrice = deliveryPrice;
        this.totalPrice = totalPrice;
        this.bigOrder = bigOrder;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getCustomer() {
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public double getStartingPrice() {
        return startingPrice;
    }

    public void setStartingPrice(double startingPrice) {
        this.startingPrice = startingPrice;
    }

    public double getTotalSale() {
        return totalSale;
    }

    public void setTotalSale(double totalSale) {
        this.totalSale = totalSale;
    }

    public double getDeliveryPrice() {
        return deliveryPrice;
    }

    public void setDeliveryPrice(double deliveryPrice) {
        this.deliveryPrice = deliveryPrice;
    }

    public double getTotalPrice() {
        return totalPrice;
    }

    public void setTotalPrice(double totalPrice) {
        this.totalPrice = totalPrice;
    }

    public boolean isBigOrder() {
        return bigOrder;
    }

    public void setBigOrder(boolean bigOrder) {
        this.bigOrder = bigOrder;
    }
}