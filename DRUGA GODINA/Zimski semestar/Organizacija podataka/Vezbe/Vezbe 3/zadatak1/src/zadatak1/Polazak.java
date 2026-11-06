
package zadatak1;

import com.opencsv.bean.CsvBindByName;

public class Polazak {
    @CsvBindByName(column = "sifra relacije")
    private String sifraRelacije;

    @CsvBindByName(column = "mesto polaska")
    private String mestoPolaska;

    @CsvBindByName(column = "mesto dolaska")
    private String mestoDolaska;

    @CsvBindByName(column = "datum polaska")
    private String datumPolaska;

    @CsvBindByName(column = "vreme polaska")
    private String vremePolaska;

    @CsvBindByName(column = "planirano vreme dolaska")
    private String planVremeDolaska;

    @CsvBindByName(column = "stanicni peron polaska")
    private String peron;

    @CsvBindByName(column = "cena karte")
    private int cena;

    @CsvBindByName(column = "broj prodatih karata")
    private int brKarata;

    public Polazak() { }

    public Polazak(String sifraRelacije, String mestoPolaska, String mestoDolaska,
            String datumPolaska, String vremePolaska, String planVremeDolaska,
            String peron, int cena, int brKarata) {
        this.sifraRelacije = sifraRelacije;
        this.mestoPolaska = mestoPolaska;
        this.mestoDolaska = mestoDolaska;
        this.datumPolaska = datumPolaska;
        this.vremePolaska = vremePolaska;
        this.planVremeDolaska = planVremeDolaska;
        this.peron = peron;
        this.cena = cena;
        this.brKarata = brKarata;
    }

    public String getSifraRelacije() {
        return sifraRelacije;
    }

    public void setSifraRelacije(String sifraRelacije) {
        this.sifraRelacije = sifraRelacije;
    }

    public String getMestoPolaska() {
        return mestoPolaska;
    }

    public void setMestoPolaska(String mestoPolaska) {
        this.mestoPolaska = mestoPolaska;
    }

    public String getMestoDolaska() {
        return mestoDolaska;
    }

    public void setMestoDolaska(String mestoDolaska) {
        this.mestoDolaska = mestoDolaska;
    }

    public String getDatumPolaska() {
        return datumPolaska;
    }

    public void setDatumPolaska(String datumPolaska) {
        this.datumPolaska = datumPolaska;
    }

    public String getVremePolaska() {
        return vremePolaska;
    }

    public void setVremePolaska(String vremePolaska) {
        this.vremePolaska = vremePolaska;
    }

    public String getPlanVremeDolaska() {
        return planVremeDolaska;
    }

    public void setPlanVremeDolaska(String planVremeDolaska) {
        this.planVremeDolaska = planVremeDolaska;
    }

    public String getPeron() {
        return peron;
    }

    public void setPeron(String peron) {
        this.peron = peron;
    }

    public int getCena() {
        return cena;
    }

    public void setCena(int cena) {
        this.cena = cena;
    }

    public int getBrKarata() {
        return brKarata;
    }

    public void setBrKarata(int brKarata) {
        this.brKarata = brKarata;
    }
}
