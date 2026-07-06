package classes;

import java.util.HashMap;

public class MasterStudent extends Student {
	private String tema;

	public String getTema() {
		return tema;
	}

	public void setTema(String tema) throws Exception {
		tema = tema.trim();
		if (tema.length() == 0) {
			throw new Exception("Morate uneti temu mastera.");
		}
		this.tema = tema;
	}
	
	public MasterStudent(int indeks, String ime, String prezime, HashMap<String, Integer> predmeti, String tema) throws Exception {
		super(indeks, ime, prezime, predmeti);
		setTema(tema);
	}
	
	@Override
	public String toString() {
		return super.toString() + " " + this.tema;
	}
}