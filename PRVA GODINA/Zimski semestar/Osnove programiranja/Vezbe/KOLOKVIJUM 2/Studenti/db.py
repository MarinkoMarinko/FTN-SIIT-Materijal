import inputs
students = []
def load_students(filename = "students.txt"):
    global students
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            students.append(line.strip().split("|"))
def write_students(filename = "students.txt"):
    global students
    with open(filename, "w", encoding="UTF-8") as file:
        file.write("\n".join("|".join(student) for student in students))
def add_student(student):
    students.append(student)
def find_student(index):
    for student in students:
        if student[2] == index:
            return student
def update_student(student):
    name = inputs.name_input("ime")
    surname = inputs.name_input("prezime")
    year = inputs.year_input()
    student[0] = name
    student[1] = surname
    student[3] = year
    print(f"Student sa brojem indeksa {student[2]} je uspešno izmenjen.")
def delete_student(student):
    students.remove(student)
    print(f"Student sa brojem indeksa {student[2]} je uspešno obrisan.")
if __name__ == "__main__":
    load_students()
    # write_students("test.txt")
    print(find_student("SV 54/2025"))
