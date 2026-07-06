package main;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

import classes.Student;

public class Main {

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	try {
    		ArrayList<Student> studenti = new ArrayList<>();
    		Student.procitajPodatke(studenti);
//    		studenti.add(new MasterStudent(
//			    studenti.size() + 1,
//			    "marko",
//			    "markovic",
//			    new HashMap<String, Integer>() {{
//			        put("Matematika", 9);
//			        put("Programiranje", 10);
//			    }},
//			    "ambasador"
//    		));
    		Collections.sort(studenti);
    		for (Student s: studenti) {
    			System.out.println(s);
    		}
    		Student.upisiPodatke(studenti);
    	}
        catch (Exception e){
        	System.out.println(e.getMessage());
        }
    	finally {
    		sc.close();
    	}
    }
}