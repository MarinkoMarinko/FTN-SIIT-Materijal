package kvadratnaJednacina;

import java.util.Scanner;


public class Code {
	// a x^2 + b x + c = 0
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Unesite a: ");
		double a = scanner.nextDouble();
		System.out.print("Unesite b: ");
		double b = scanner.nextDouble();
		System.out.print("Unesite c: ");
		double c = scanner.nextDouble();
		scanner.close();
		double d = b * b - 4 * a * c;
		if (d < 0) {
			System.out.println("Rešenja su imaginarna.");
		}
		else if(d == 0) {
			double x = (-b + d) / (2 * a);
			System.out.println("Rešenje je jednoznačno i iznosi: " + x);
		}
		else {
			double x1 = (b + Math.sqrt(d)) / (2 * a);
			double x2 = (b - Math.sqrt(d)) / (2 * a);
			System.out.println("Postoje 2 rešenja: " +  x1 + " i " + x2);
		}
	}

}
