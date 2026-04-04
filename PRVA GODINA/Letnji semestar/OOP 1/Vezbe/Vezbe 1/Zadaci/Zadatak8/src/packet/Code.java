package packet;

import java.util.Scanner;

public class Code {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Unesite broj redova: ");
		int n = scanner.nextInt();
		System.out.print("Unesite broj kolona: ");
		int m = scanner.nextInt();
		int a[][] = new int[n][m];
		for(int i = 0; i < n; i++) {
			int value = i;
			for(int j = 0; j < m; j++) {
				a[i][j] = value++;
			}
		}
		System.out.println("Matrica A je oblika: ");
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				System.out.print(a[i][j] + "\t");
			}
			System.out.println();
		}
		scanner.close();
	}

}
