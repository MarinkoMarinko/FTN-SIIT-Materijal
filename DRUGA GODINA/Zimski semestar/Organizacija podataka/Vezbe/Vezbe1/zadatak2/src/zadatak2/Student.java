package zadatak2;

import com.opencsv.bean.CsvBindByName;

public class Student {
	@CsvBindByName(column = "br_indeksa", required = true)
	private int index;
	
	@CsvBindByName(column = "ime", required = true)
	private String name;
	
	@CsvBindByName(column = "prezime", required = true)
	private String surname;
	
	@CsvBindByName(column = "predmet", required = true)
	private String subject;
	
	@CsvBindByName(column = "ocena", required = true)
	private int grade;

	public int getIndex() {
		return index;
	}

	public void setIndex(int index) {
		this.index = index;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSurname() {
		return surname;
	}

	public void setSurname(String surname) {
		this.surname = surname;
	}

	public String getSubject() {
		return subject;
	}

	public void setSubject(String subject) {
		this.subject = subject;
	}

	public int getGrade() {
		return grade;
	}

	public void setGrade(int grade) {
		this.grade = grade;
	}
	
	public Student() { }
	
	public Student(int index, String name, String surname, String subject, int grade) {
		super();
		this.index = index;
		this.name = name;
		this.surname = surname;
		this.subject = subject;
		this.grade = grade;
	}
	
	@Override
	public String toString() {
		return this.index + " " + this.name + " " + this.surname;
	}
}