students = []


def load_all(filename="files/students.txt"):
    global students
    students = []

    with open(filename, encoding="utf-8") as file:
        for line in file:
            students.append(line.strip("\n").split("|"))


def save_all(filename="files/students.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            file.write("|".join(student) + "\n")


def find(index):
    for student in students:
        if student[2] == index:
            return student
    return None


def add(student):
    students.append(student)


def remove(index):
    for student in students:
        if student[2] == index:
            students.remove(student)
            return


def update(new_student):
    index = new_student[2]
    for i in range(len(students)):
        if students[i][2] == index:
            students[i] = new_student
            return


if __name__ == "__main__":
    load_all(filename="test.txt")
    print(students)
    save_all(filename="test.txt")
