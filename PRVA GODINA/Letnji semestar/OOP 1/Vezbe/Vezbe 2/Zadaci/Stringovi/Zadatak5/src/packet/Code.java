package packet;

import java.util.Scanner;

public class Code {
	public static String input = "Coko plazma|s01|Bambi|85.30|akcija\n"
	        + "Smoki|s02|Stark|55.00|nije na akciji\n"
	        + "Cipsi|s03|Marbo |115.20|nije na akciji\n"
	        + "Krem Bananica|s04|Stark|11.00|akcija\n";
	public static void menu() {
		System.out.println("a) Spisak naziva svih artikala");
		System.out.println("b) Podaci određenog artikla");
		System.out.println("c) Spisak artikala na akciji");
		System.out.println("d) Spisak artikala određenog proizvođača");
		System.out.println("x) Izlaz iz aplikacije");
	}
	public static void allItemNames() {
		String items[] = input.strip().split("\n");
		for (String item: items) {
			String parts[] = item.split("\\|");
			System.out.println(parts[0].trim());
		}
	}
	public static void singleItem(String searchedItem) {
		String items[] = input.strip().split("\n");
		for (String item: items) {
			String parts[] = item.split("\\|");
			String name = parts[0].trim();
			if (name.equals(searchedItem)) { 
				String pwd = parts[1].trim();
				String owner = parts[2].trim();
				Double price = Double.parseDouble(parts[3].trim());
				String auction = parts[4].trim();
				System.out.printf("%s %s %s %.2f %s\n", name, pwd, owner, price, auction);
			}
		}
	}
	public static void itemsOnDiscount() {
		String items[] = input.strip().split("\n");
		for (String item: items) {
			String parts[] = item.split("\\|");
			String auction = parts[4].trim();
			if (auction.equals("akcija")) {
				String name = parts[0].trim();
				String pwd = parts[1].trim();
				String owner = parts[2].trim();
				Double price = Double.parseDouble(parts[3].trim());
				System.out.printf("%s %s %s %.2f %s\n", name, pwd, owner, price, auction);
			}
		}
	}
	public static void itemsBySeller(String searchedSeller) {
		String items[] = input.strip().split("\n");
		for (String item: items) {
			String parts[] = item.split("\\|");
			String owner = parts[2].trim();
			if (owner.equals(searchedSeller)) { 
				String name = parts[0].trim();
				String pwd = parts[1].trim();
				Double price = Double.parseDouble(parts[3].trim());
				String auction = parts[4].trim();
				System.out.printf("%s %s %.2f %s\n", name, pwd, price, auction);
			}
		}
	}
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			menu();
			System.out.print("Unesite svoj izbor: ");
			String choice = scanner.next().toLowerCase();
			switch (choice) {
				case "a": 
					allItemNames();
					break;
				case "b":
					System.out.print("Unesite traženi artikal: ");
					scanner.nextLine();
					String searchedItem = "";
					while (true) {
						searchedItem = scanner.nextLine();
						searchedItem = searchedItem.trim();
						if (searchedItem.equals("")) {
							System.out.println("Pogrešan unos! Pokušajte ponovo!");
							continue;
						}
						break;
					}
					singleItem(searchedItem);
					break;
				case "c":
					itemsOnDiscount();
					break;
				case "d":
					System.out.print("Unesite traženog prodavca: ");
					scanner.nextLine();
					String searchedSeller = "";
					while (true) {
						searchedSeller = scanner.nextLine();
						searchedSeller = searchedSeller.trim();
						if (searchedSeller.equals("")) {
							System.out.println("Pogrešan unos! Pokušajte ponovo!");
							continue;
						}
						break;
					}
					itemsBySeller(searchedSeller);
					break;
				case "x":
					System.out.println("Izlaz iz aplikacije...");
					scanner.close();
					return;
				default:
					System.out.println("Pogrešan unos. Pokušajte ponovo.");
			}
		}
	}
}
