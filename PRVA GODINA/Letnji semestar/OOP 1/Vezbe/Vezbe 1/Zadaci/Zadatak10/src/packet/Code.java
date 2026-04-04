package packet;

import java.util.Scanner;

public class Code {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Unesite dimenziju kvadratne matrice: ");
		int n = scanner.nextInt();
		int a[][] = new int[n][n];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.printf("a[%d][%d] = ", i, j);
				a[i][j] = scanner.nextInt();
			}
			System.out.println();
		}
		for(int i = 0; i < n; i++) {
			int temp = a[i][i];
			a[i][i] = a[i][n - 1 - i];
			a[i][n -1 - i] = temp;
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				System.out.print(a[i][j] + "\t");
			}
			System.out.println();
		}
		scanner.close();
	}

}
