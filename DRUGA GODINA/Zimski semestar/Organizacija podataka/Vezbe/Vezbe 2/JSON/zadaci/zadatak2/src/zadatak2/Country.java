package zadatak2;

import com.opencsv.bean.CsvBindByName;

public class Country {
    @CsvBindByName(column = "CountryName")
    private String countryName;

    @CsvBindByName(column = "CapitalName")
    private String capitalName;

    @CsvBindByName(column = "CapitalLatitude")
    private double capitalLatitude;

    @CsvBindByName(column = "CapitalLongitude")
    private double capitalLongitude;

    @CsvBindByName(column = "CountryCode")
    private String countryCode;

    @CsvBindByName(column = "ContinentName")
    private String continentName;

    public Country() {
    }

    public String getCountryName() {
        return countryName;
    }

    public void setCountryName(String countryName) {
        this.countryName = countryName;
    }

    public String getCapitalName() {
        return capitalName;
    }

    public void setCapitalName(String capitalName) {
        this.capitalName = capitalName;
    }

    public double getCapitalLatitude() {
        return capitalLatitude;
    }

    public void setCapitalLatitude(double capitalLatitude) {
        this.capitalLatitude = capitalLatitude;
    }

    public double getCapitalLongitude() {
        return capitalLongitude;
    }

    public void setCapitalLongitude(double capitalLongitude) {
        this.capitalLongitude = capitalLongitude;
    }

    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getContinentName() {
        return continentName;
    }

    public void setContinentName(String continentName) {
        this.continentName = continentName;
    }

    @Override
    public String toString() {
        return "Country{" +
                "countryName='" + countryName + "'" +
                ", capitalName='" + capitalName + "'" +
                ", capitalLatitude=" + capitalLatitude +
                ", capitalLongitude=" + capitalLongitude +
                ", countryCode='" + countryCode + "'" +
                ", continentName='" + continentName + "'" +
                "}";
    }
}
