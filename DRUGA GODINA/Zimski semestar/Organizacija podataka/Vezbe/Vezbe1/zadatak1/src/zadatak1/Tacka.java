package zadatak1;

import com.opencsv.bean.CsvBindByName;

public class Tacka {
	@CsvBindByName(column = "x", required = true)
	private double x;
	
	@CsvBindByName(column = "y", required = true)
	private double y;
	
	@CsvBindByName(column = "z", required = true)
	private double z;
	
	public Tacka() { }
	
	public Tacka(double x, double y, double z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}

	public double getZ() {
		return z;
	}

	public void setZ(double z) {
		this.z = z;
	}
	
	public double calculateDistance() {
		return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
	}
	
	@Override
	public String toString() {
		return this.getX() + ", " + this.getY() + ", " + this.getZ();
	}
}