package packet;

import java.util.Scanner;

public class Code {
	public static void makeRomboid(int n, int width) {
		printRow(n, width);
		if (n == 0) {
			return;
		}
		makeRomboid(n - 1, width);
		printRow(n, width);
	}
	
	public static void printRow(int n, int width) {
		int stars = width - 2 * n;
		int dashes = (width - stars) / 2;
		String row = "";
		for (int i = 0; i < dashes; i++) {
            row += '-';
        }
        for (int i = 0; i < stars; i++) {
        	row += '*';
        }
        for (int i = 0; i < dashes; i++) {
        	row += '-';
        }
        System.out.println(row);
	}
	// n * 2 + 1 rows
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Unesite n: ");
		int n = scanner.nextInt();
		int width = n * 2 + 1;
		makeRomboid(n, width);
		scanner.close();
	}

}
