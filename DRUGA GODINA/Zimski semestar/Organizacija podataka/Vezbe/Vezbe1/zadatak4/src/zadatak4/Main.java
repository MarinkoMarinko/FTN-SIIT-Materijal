package zadatak4;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import com.opencsv.CSVWriter;

public class Main {

    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {

            // Naziv datoteke
            System.out.print("Naziv CSV datoteke: ");
            String naziv = sc.nextLine();

            // Broj kolona
            System.out.print("Broj kolona: ");
            int brojKolona = Integer.parseInt(sc.nextLine());

            if (brojKolona <= 0) {
                System.out.println("Broj kolona mora biti pozitivan.");
                return;
            }

            // Nazivi kolona
            String[] kolone = new String[brojKolona];

            for (int i = 0; i < brojKolona; i++) {
                System.out.print("Naziv kolone " + (i + 1) + ": ");
                kolone[i] = sc.nextLine();
            }

            // Zaglavlje
            System.out.print("Da li zelite zaglavlje (da/ne)? ");
            boolean zaglavlje = sc.nextLine().equalsIgnoreCase("da");

            // Broj redova
            System.out.print("Broj redova za unos: ");
            int brojRedova = Integer.parseInt(sc.nextLine());

            if (brojRedova < 0) {
                System.out.println("Broj redova ne moze biti negativan.");
                return;
            }

            // Pisanje CSV datoteke
            try (CSVWriter writer = new CSVWriter(new FileWriter(naziv))) {

                if (zaglavlje) {
                    writer.writeNext(kolone, false);
                }

                for (int i = 0; i < brojRedova; i++) {
                    System.out.println("\nRed " + (i + 1) + ":");

                    String[] podaci = new String[brojKolona];

                    for (int j = 0; j < brojKolona; j++) {
                        System.out.print(kolone[j] + ": ");
                        podaci[j] = sc.nextLine();
                    }

                    writer.writeNext(podaci, false);
                }

                System.out.println("\nCSV datoteka je uspesno kreirana!");

            } catch (IOException e) {
                e.printStackTrace();
            }

        } catch (NumberFormatException e) {
            System.out.println("Broj kolona i redova moraju biti celi brojevi.");
        }
    }
}
