package packet;

import java.util.Scanner;

public class Main {
    public static String[][] products = new String[100][5];
    public static int counter = 0;
    public static void menu() {
        System.out.println("***** GLAVNI MENI *****");
        System.out.println("1. Dodavanje artikla");
        System.out.println("2. Dodavanje količine u magacinu");
        System.out.println("3. Prikaz količina iz magacina");
        System.out.println("4. Prikaz prosečne količine artikla iz magacina");
        System.out.println("x. Izlaz iz aplikacije");
    }
    public static void addProduct(String pwd, String name) {
        products[counter][0] = pwd;
        products[counter][1] = name;
        products[counter][2] = "0";
        products[counter][3] = "0";
        products[counter][4] = "0";
        counter++;
    }
    public static int findById(String productId) {
        for (int i = 0; i < counter; i++) {
            if (products[i][0].equals(productId)) {
                return i;
            }
        }
        return -1;
    }
    public static void addCount(String[] countData, int index) {
        products[index][2] = countData[0];
        products[index][3] = countData[1];
        products[index][4] = countData[2];
    }
    public static void showProductCounts(int index) {
        System.out.printf(
            "Artikal %s %s se u magacinima nalazi u količinama %s, %s i %s.\n",
            products[index][0],
            products[index][1],
            products[index][2],
            products[index][3],
            products[index][4]
        );
    }
    public static double avg(String a, String b, String c) {
        int x = Integer.parseInt(a);
        int y = Integer.parseInt(b);
        int z = Integer.parseInt(c);
        return (double) (x + y + z) / 3;
    }
    public static void showProductAverages() {
        if (counter == 0) {
            System.out.println("Nema podataka za prikaz!");
        } 
        else {
            for (int i = 0; i < counter; i++) {
                double average = avg(products[i][2], products[i][3], products[i][4]);
                System.out.printf(
                    "Artikal %s %s ima prosečnu količinu %.2f\n",
                    products[i][0],
                    products[i][1],
                    average
                );
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            menu();
            System.out.print("Unesite Vaš izbor: ");
            String choice = sc.nextLine().toLowerCase();
            switch (choice) {
                case "1":
                    while (true) {
                        System.out.print("Unesite podatke o artiklu [šifra;naziv]: ");
                        String productInput = sc.nextLine().toLowerCase();
                        String[] productData = productInput.split(";");
                        if (productData.length != 2) {
                            System.out.println("Uneli ste podatke u pogrešnom formatu. Pokušajte ponovo.");
                        } 
                        else {
                            String pwd = productData[0].trim();
                            String name = productData[1].trim();
                            addProduct(pwd, name);
                            System.out.printf("Uspešno dodat artikal %s %s.\n", pwd, name);
                            break;
                        }
                    }
                    break;
                case "2":
                    System.out.print("Unesite šifru artikla: ");
                    String productId = sc.nextLine().toLowerCase();
                    int index = findById(productId);
                    if (index != -1) {
                        while (true) {
                            System.out.print("Unesite količine artikla u magacinima u formatu [količina1 količina2 količina3]: ");
                            String countInput = sc.nextLine();
                            String[] countData = countInput.trim().split(" ");
                            if (countData.length != 3) {
                                System.out.println("Pogrešan unos. Pokušajte ponovo!");
                            } 
                            else {
                                addCount(countData, index);
                                System.out.println("Uspešno unete količine.");
                                break;
                            }
                        }
                    } 
                    else {
                        System.out.println("Ne postoji traženi artikal.");
                    }
                    break;
                case "3":
                    System.out.print("Unesite šifru artikla: ");
                    String productPwd = sc.nextLine().toLowerCase();
                    int productIndex = findById(productPwd);
                    if (productIndex != -1) {
                        showProductCounts(productIndex);
                    } 
                    else {
                        System.out.println("Ne postoji traženi artikal.");
                    }
                    break;
                case "4":
                    showProductAverages();
                    break;
                case "x":
                    System.out.println("Izlazak iz aplikacije...");
                    sc.close();
                    return;
                default:
                    System.out.println("Nepostojeća opcija.");
            }
        }
    }
}