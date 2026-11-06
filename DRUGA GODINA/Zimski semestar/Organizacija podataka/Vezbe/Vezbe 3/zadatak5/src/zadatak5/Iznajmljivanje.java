package zadatak5;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Iznajmljivanje {
	@JsonProperty("Sifra_iznajmljivanja")
	private String sifra;
	
	@JsonProperty("Mesto_iznajmljivanja")
	private String mestoIznajmljivanja;
	
	@JsonProperty("Datum_iznajmljivanja")
	private String datumIznajmljivanja;
	
	@JsonProperty("Datum_vracanja")
	private String datumVracanja;
	
	@JsonProperty("Predjeno_kilometara")
	private Integer predjenoKilometara;
	
	@JsonProperty("Cena_za_dan")
	private int cenaZaDan;
	
	@JsonProperty("Broj_dana")
	private int brojDana;
	
	@JsonProperty("Iznajmljivac")
	private Osoba iznajmljivac;
	
	public Iznajmljivanje() { }

	public Iznajmljivanje(String sifra, String mestoIznajmljivanja, String datumIznajmljivanja, String datumVracanja,
			Integer predjenoKilometara, int cenaZaDan, int brojDana, Osoba iznajmljivac) {
		super();
		this.sifra = sifra;
		this.mestoIznajmljivanja = mestoIznajmljivanja;
		this.datumIznajmljivanja = datumIznajmljivanja;
		this.datumVracanja = datumVracanja;
		this.predjenoKilometara = predjenoKilometara;
		this.cenaZaDan = cenaZaDan;
		this.brojDana = brojDana;
		this.iznajmljivac = iznajmljivac;
	}

	public String getSifra() {
		return sifra;
	}

	public void setSifra(String sifra) {
		this.sifra = sifra;
	}

	public String getMestoIznajmljivanja() {
		return mestoIznajmljivanja;
	}

	public void setMestoIznajmljivanja(String mestoIznajmljivanja) {
		this.mestoIznajmljivanja = mestoIznajmljivanja;
	}

	public String getDatumIznajmljivanja() {
		return datumIznajmljivanja;
	}

	public void setDatumIznajmljivanja(String datumIznajmljivanja) {
		this.datumIznajmljivanja = datumIznajmljivanja;
	}

	public String getDatumVracanja() {
		return datumVracanja;
	}

	public void setDatumVracanja(String datumVracanja) {
		this.datumVracanja = datumVracanja;
	}

	public Integer getPredjenoKilometara() {
		return predjenoKilometara;
	}

	public void setPredjenoKilometara(Integer predjenoKilometara) {
		this.predjenoKilometara = predjenoKilometara;
	}

	public int getCenaZaDan() {
		return cenaZaDan;
	}

	public void setCenaZaDan(int cenaZaDan) {
		this.cenaZaDan = cenaZaDan;
	}

	public int getBrojDana() {
		return brojDana;
	}

	public void setBrojDana(int brojDana) {
		this.brojDana = brojDana;
	}

	public Osoba getIznajmljivac() {
		return iznajmljivac;
	}

	public void setIznajmljivac(Osoba iznajmljivac) {
		this.iznajmljivac = iznajmljivac;
	}
}
