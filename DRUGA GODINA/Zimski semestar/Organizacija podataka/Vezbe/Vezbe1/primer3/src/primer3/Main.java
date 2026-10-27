
package primer3;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.List;

import com.opencsv.bean.CsvToBean;
import com.opencsv.bean.CsvToBeanBuilder;

public class Main {

    public static void main(String[] args) {
        try (Reader reader = new FileReader("drzave_gradovi.csv")) {
            CsvToBean<Grad> csvToBean = new CsvToBeanBuilder<Grad>(reader)
                    .withType(Grad.class)
                    .build();

            List<Grad> gradovi = csvToBean.parse();

            for (Grad grad : gradovi) {
                System.out.println(grad.getDrzava() + ", " + grad.getGrad());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
