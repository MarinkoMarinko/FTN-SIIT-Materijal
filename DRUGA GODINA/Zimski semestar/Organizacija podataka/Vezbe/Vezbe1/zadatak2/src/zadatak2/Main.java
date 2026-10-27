package zadatak2;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.List;

import com.opencsv.bean.CsvToBeanBuilder;

// NIJE ZAVRSENO!!!
public class Main {

	public static void main(String[] args) {
		try (Reader r = new FileReader("input.csv")) {
			List<Student> studenti = new CsvToBeanBuilder<Student>(r)
					.withType(Student.class)
					.build()
					.parse();
			for (Student s: studenti) {
				System.out.println(s);
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
