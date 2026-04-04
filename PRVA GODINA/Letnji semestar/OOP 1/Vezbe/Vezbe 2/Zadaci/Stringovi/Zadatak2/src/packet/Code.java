package packet;

public class Code {
	public static int[][] makeMatrix(String input) {
		String[] rows = input.split(";");
		int rowCount = rows.length;
		int[][] a = new int[rowCount][];
		for (int i = 0; i < rowCount; i++) {
			String[] data = rows[i].split(",");
			int colCount = data.length;
			a[i] = new int[colCount];
			for (int j = 0; j < colCount; j++) {
				a[i][j] = Integer.parseInt(data[j]);
			}
		}
		return a;
	}
	public static void printMatrix(int[][] a) {
		for(int[] row: a) {
			for(int num: row) {
				System.out.print(num + "\t");
			}
			System.out.println();
		}
	}
	public static void main(String[] args) {
		String input = "4,3,2,1;0,1,0;1,2,3,4";
		int a[][] = makeMatrix(input);
		printMatrix(a);
	}

}
