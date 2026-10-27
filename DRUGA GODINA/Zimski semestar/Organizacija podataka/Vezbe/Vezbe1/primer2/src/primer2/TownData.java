package primer2;

import java.util.LinkedHashMap;

public class TownData {

    public static LinkedHashMap<String, String> getDrzaveGradovi() {
        LinkedHashMap<String, String> countries = new LinkedHashMap<>();

        countries.put("Australia", "Canberra");
        countries.put("Canada", "Ottawa");
        countries.put("China", "Beijing");
        countries.put("France", "Paris");

        return countries;
    }
}
