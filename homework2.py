students = [""]

def addStudent():   
    name = input("Enter student name: ")
    students.append(name)
    print(name+ "added to the list")

def removeStudent():
    name = input("Enter student name for deletion: ")
    if name in students:
        students.remove(name)
        print(name+ "removed from the list")
    else:
        print(name+ "is not on the list")

def addMultipleStudents():
    number = int(input("How many students you want to add: "))
    i=0
    while i<number:
        addStudent()
        i +=1
    print(students)

def deleteMultipleStudents():
    number = int(input("How many students you want to delete: "))
    i=0
    while i<number:
        name= input("Enter student name: ")
        list.remove(name)
        print("Successfully deleted")

def printStudents():
    print("Students: ")
    for students in range(len(students)):
        print(f"{students} "-" {students[student]}")

def findStudentSNumber():
    name = input("Enter the student whose number you want to inquire: ")
    if name in list:
        num = list.index(name)
        print(str(name), "Find Student ", str(num))
    else:
        print("Unsuccessful")

print("""
To Add a Student --->1
To Delete the Student --->2
To Add More Than One Student --->3
To Delete More than One Student ---->4
Print  Students             ------->5
To Find Student number ---->6
""")

while True:
    number = int(input("Enter the number"))

    if number ==1:
        addStudent()

    elif number ==2:
        removeStudent()

    elif number ==3:
        addMultipleStudents()

    elif number ==4:
        deleteMultipleStudents()

    elif number ==5:
        printStudents()

    elif number ==6:
        findStudentSNumber()

        break

