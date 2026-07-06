package classes;

import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Student implements Comparable<Student> {
	private int indeks;
	private String ime, prezime;
	private HashMap<String, Integer> predmeti;
	
	public int getIndeks() {
		return indeks;
	}
	
	public void setIndeks(int indeks) throws Exception {
		if (indeks < 0) {
			throw new Exception("Indeks mora biti veći od nule.");
		}
		this.indeks = indeks;
	}
	
	public String getIme() {
		return ime;
	}
	
	public void setIme(String ime) throws Exception {
		ime = ime.trim();
		if (ime.length() == 0) {
			throw new Exception("Morate uneti ime");
		}
		this.ime = ime;
	}
	
	public String getPrezime() {
		return prezime;
	}
	
	public void setPrezime(String prezime) throws Exception {
		prezime = prezime.trim();
		if (prezime.length() == 0) {
			throw new Exception("Morate uneti prezime");
		}
		this.prezime = prezime;
	}
	
	public HashMap<String, Integer> getPredmeti() {
		return predmeti;
	}
	
	public void setPredmeti(HashMap<String, Integer> predmeti) {
		if (predmeti == null) {
			this.predmeti = new HashMap<>();
		}
		else {
			this.predmeti = predmeti;
		}

	}
	
	public Student(int indeks, String ime, String prezime, HashMap<String, Integer> predmeti) throws Exception {
		setIndeks(indeks);
		setIme(ime);
		setPrezime(prezime);
		setPredmeti(predmeti);
	}
	
	public void polaganjePredmeta(String nazivPredmeta, int ocena) throws Exception {
		if (this.predmeti.containsKey(nazivPredmeta)) {
			throw new Exception("Izabrani predmet je već položen.");
		}
		else {
			this.predmeti.put(nazivPredmeta, ocena);
		}
	}
	
	public double racunanjeProsecneOcene() {
		int suma = 0;
		if (this.predmeti.size() == 0) {
			return 0;
		}
		else {
			for(int ocena: this.predmeti.values()) {
				suma += ocena;
			}
		}
		return (double)suma / this.predmeti.size();
	}
	
	@Override
	public String toString() {
		return this.indeks + " " + this.ime + " " + this.prezime + " " + String.format("%.2f", racunanjeProsecneOcene());
	}
	
	public static void procitajPodatke(ArrayList<Student> studenti) throws Exception {
		List<String> linije = Files.readAllLines(Path.of("src/data/studenti.txt"));
		for (String linija: linije) {
			String podaci[] = linija.split(";");
			int indeks = Integer.parseInt(podaci[0]);
			String ime = podaci[1];
			String prezime = podaci[2];
			HashMap<String, Integer> tempPredmeti = new HashMap<>();
			for (int i = 3; i < podaci.length - 1; i += 2) {
				tempPredmeti.put(podaci[i], Integer.parseInt(podaci[i + 1]));
			}
			if (podaci.length % 2 == 0) {
				String tema = podaci[podaci.length - 1];
				MasterStudent student = new MasterStudent(indeks, ime, prezime, tempPredmeti, tema);
				studenti.add(student);
			}
			else {
				Student student = new Student(indeks, ime, prezime, tempPredmeti);
				studenti.add(student);
			}
		}
	}
	
	public static void upisiPodatke(ArrayList<Student> studenti) throws Exception {
		PrintWriter pw = new PrintWriter("src/data/studenti.txt");
		for (Student s: studenti) {
			String red = "";
			red += s.getIndeks() + ";";
			red += s.getIme() + ";";
			red += s.getPrezime();
			for (String nazivPredmeta: s.getPredmeti().keySet()) {
				int ocena = s.getPredmeti().get(nazivPredmeta);
				red += ";" + nazivPredmeta + ";" + ocena;
			}
			if (s instanceof MasterStudent) {
				MasterStudent ms = (MasterStudent) s;
				red += ";" + ms.getTema();
			}
			pw.println(red);
		}
		pw.close();
	}
	
	@Override
	public int compareTo(Student s) {
		return Double.compare(s.racunanjeProsecneOcene(), this.racunanjeProsecneOcene());
	}
}