package packet;

public class Code {

	public static void main(String[] args) {
		int a[] = { -10, 3, 16, 1, 4, -2 };
		int max = a[0];
		int min = a[0];
		int s = 0;
		for(int el: a) {
			if (el > max) {
				max = el;
			}
			else if (el < min) {
				min = el;
			}
			s += el;
		}
		double avg = s / a.length;
		System.out.println("Najveći element je " + max + ", a najmanji: " + min);
		System.out.println("Srednja vrednost niza je: " + avg);
		for(int i = 0; i < a.length; i++) {
			if (a[i] > 0 && a[i] < avg) {
				System.out.println(a[i]);
			}
		}
	}

}
