package zadatak5;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Osoba {
	@JsonProperty("ime")
	private String ime;
	
	@JsonProperty("prezime")
	private String prezime;
	
	@JsonProperty("maticni_broj")
	private String maticniBroj;
	
	public Osoba() { }

	public Osoba(String ime, String prezime, String maticniBroj) {
		super();
		this.ime = ime;
		this.prezime = prezime;
		this.maticniBroj = maticniBroj;
	}

	public String getIme() {
		return ime;
	}

	public void setIme(String ime) {
		this.ime = ime;
	}

	public String getPrezime() {
		return prezime;
	}

	public void setPrezime(String prezime) {
		this.prezime = prezime;
	}

	public String getMaticniBroj() {
		return maticniBroj;
	}

	public void setMaticniBroj(String maticniBroj) {
		this.maticniBroj = maticniBroj;
	}
}
