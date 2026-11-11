student = {}

while True:
    print("\n ---- STUDENT MANAGER APP ----")
    print("1 Add Student")
    print("2 View Student")
    print("3 Check Result")
    print("4 Exit")

    choice = input("Enter Your Choice: ")

    #Add student

    if choice == "1":
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        student[name] = marks
        print(f"{name} successfully Addedd ")

    #view student 
    elif choice =="2":
        if not student:
            print("No student found: ")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("Student not found! ")


    #Exit

    elif choice == "4":
        print("Exiting....!")
        break

    else:
        print("In-Valid input")

