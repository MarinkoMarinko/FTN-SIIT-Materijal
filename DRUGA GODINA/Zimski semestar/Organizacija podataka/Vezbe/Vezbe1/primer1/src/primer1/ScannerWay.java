
package primer1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ScannerWay {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(new File("drzave_gradovi.csv"))) {
            sc.nextLine();

            while (sc.hasNextLine()) {
                System.out.println(sc.nextLine());
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
