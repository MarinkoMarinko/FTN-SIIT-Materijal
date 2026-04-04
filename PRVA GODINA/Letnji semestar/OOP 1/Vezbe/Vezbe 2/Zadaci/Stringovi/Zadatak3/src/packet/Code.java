package packet;

public class Code {
	public static int maxEl(int a[]) {
		int max = a[0];
		for (int i = 1; i < a.length; i++) {
			if (a[i] > max) {
				max = a[i];
			}
		}
		return max;
	}
	public static int minEl(int a[]) {
		int min = a[0];
		for (int i = 1; i < a.length; i++) {
			if (a[i] < min) {
				min = a[i];
			}
		}
		return min;
	}
	public static double avg(int a[]) {
		double s = 0;
		for (int i = 0; i < a.length; i++) {
			s += a[i];
		}
		return s / a.length;
	}
	public static void changeArray(int a[]) {
		double avg = avg(a);
		for (int i = 0; i < a.length; i++) {
			if (a[i] < 0) {
				a[i] += avg;
			}
			else {
				a[i] -= avg;
			}
			System.out.print(a[i] + " ");
		}
	}
	public static void main(String[] args) {
		int a[] = {5, -2, -5, 3, -7, 1, -12, 37, 20};
		System.out.println("Najveci element niza: " + maxEl(a));
		System.out.println("Najmanji element niza: " + minEl(a));
		System.out.printf("Srednja vrednost niza: %.2f\n", avg(a));
		System.out.println("Promenjen niz:");
		changeArray(a);
	}

}
