# Student Hub Program, Made by Pushkar and Kartik
data = {
    6911: {1: "Pushkar", 2: "11th - A", 3: "39", "M": 40, "P": 40, "C": 40, "E": 40, "CS": 40, 4: 100, 5: "A"},
    7104: {1: "Kartik", 2: "11th - A", 3: "29", "M": 40, "P": 40, "C": 40, "E": 40, "CS": 40, 4: 100, 5: "A"}
}

while True:  # running an infinite loop for smoother functioning

    user_input = int(input(
        "Choose from the given actions: View(1), Edit(2), Delete(3), Delete Database(4), search(5), generate report(6), Add another record(7), View Database(8), Exit(9): "))

    if user_input == 1:  # code for View command
        choice = int(input("Enter serial no. to access the info: "))

        if choice not in data:
            print("Enter a valid serial no.")
            continue
        else:
            choice2 = int(input(
                "Enter what info you want to view: Name(1), Class(2), Roll no(3), percentage(4), Grade(5), Whole record(6): "))

            if choice2 == 1 or choice2 == 2 or choice2 == 3 or choice2 == 4 or choice2 == 5:
                print("The info you asked for is this: ",
                      data[choice][choice2])
            elif choice2 == 6:
                print("The whole record is this: ", data[choice])
            else:
                print("Enter a valid option")
                continue

            choice3 = int(
                input("Do you want to see marks too? Yes(1), No(2): "))
            if choice3 == 1:
                choice4 = input(
                    "Enter the subject whose marks you want to see: Math Marks(M), Physics Marks(P), Chemistry Marks(C), English Marks(E), CS Marks(CS) : \n")
                print("The info you asked for is this", data[choice][choice4])
            elif choice3 == 2:
                continue
            else:
                print("Enter a valid input")
                continue

    elif user_input == 2:  # code for edit command
        choice = int(
            input("Enter serial no. to select the info to be changed: "))

        if choice not in data:
            print("Enter a valid serial no.")
            continue
        else:
            choice2 = int(input(
                "Choose from the options to change: Name(1), Roll no.(3), class(2): "))

            if choice2 in [1, 2, 3]:
                data[choice][choice2] = input("Enter the changed data: ")
                print("The data you have changed looks like this",
                      data[choice][choice2])
            else:
                print("Enter valid input")

            choice3 = int(
                input("Do you want to edit marks too? Yes(1), No(2): "))
            if choice3 == 1:
                choice4 = input(
                    "Enter the subject whose marks you want to edit: Math Marks(M), Physics Marks(P), Chemistry Marks(C), English Marks(E), CS Marks(CS): ")
                marks_new = int(input("Enter the new marks: "))
                data[choice][choice4] = marks_new
                print("The info you edited looks like", data[choice][choice4])
            elif choice3 == 2:
                continue
            else:
                print("Enter a valid input")
                continue

    elif user_input == 3:  # code for delete command
        choice = int(
            input("Enter the serial no./Admission no. of the record you want to delete: "))

        if choice not in data:
            print("Please, enter a valid serial no.")
            continue
        else:
            choice2 = int(input(
                "Enter what info you want to delete: Name(1), Class(2), Roll no(3), Whole record(4), Skip to next step(5): "))

            if choice2 == 1 or choice2 == 2 or choice2 == 3:
                del data[choice][choice2]
            elif choice2 == 4:
                data.pop(choice)
            elif choice2 == 4:
                continue

        choice3 = int(
            input("Do you want to delete marks too? Yes(1), No(2): "))

        if choice3 == 1:
            choice4 = input(
                "Enter the subject whose marks you want to delete: Math Marks(M), Physics Marks(P), Chemistry Marks(C), English Marks(E), CS Marks(CS): ")
            del data[choice][choice4]
        elif choice3 == 2:
            continue
        else:
            print("Enter a valid input")
            continue

    elif user_input == 4:  # code for delete database command
        choice = int(
            input("Are you sure on deleting the whole database: yes(1), no(2): "))

        if choice == 2:
            print("Alrigh then.")
        elif choice == 1:
            print("Ohk then, its deleted")
            del data
        else:
            continue

    elif user_input == 5:  # code for search command
        choice = int(
            input("Enter the admission number of the student to search: "))

        if choice in data.keys():
            print("The student was found in the database")
            choice3 = int(
                input("Do you want to extract that student's info: Yes(1), No(2): "))

            if choice3 == 1:
                choice2 = int(input(
                    "Enter what info you want to view: Name(1), Class(2), Roll no(3), Whole record(4): "))

                if choice2 == 1 or choice2 == 2 or choice2 == 3:
                    print("The info you asked for is this: ",
                          data[choice][choice2])
                elif choice2 == 4:
                    print("The whole record is this: ", data[choice])
                else:
                    print("Enter a valid option")

                choice3 = int(
                    input("Do you want to see marks too? Yes(1), No(2): "))
                if choice3 == 1:
                    choice4 = input(
                        "Enter the subject whose marks you want to see: Math Marks(M), Physics Marks(P), Chemistry Marks(C), English Marks(E), CS Marks(CS) : \n")
                    print("The info you asked for is this",
                          data[choice][choice4])
                elif choice3 == 2:
                    continue
                else:
                    print("Enter a valid input")
                    continue
            elif choice3 == 2:
                continue
        else:
            print("The Student was not found in the database")
            continue

    elif user_input == 6:  # code for generating report command

        choice = int(
            input("Enter the serial no./Admission no. of student to generate report: "))

        if choice not in data:
            print("Enter a valid serial no./Admission no.")
        else:
            print("Here is the report of the student")

            print("Name: ", data[choice][1])
            print("Class: ", data[choice][2])
            print("Roll no.: ", data[choice][3])
            print("Marks in Mathemathics: ", data[choice]["M"])
            print("Marks in Physics: ", data[choice]["P"])
            print("Marks in Chemistry: ", data[choice]["C"])
            print("Marks in English: ", data[choice]["E"])
            print("Marks in Computer Science: ", data[choice]["CS"])

    elif user_input == 7:  # code for adding another record
        choice3 = int(
            input("Enter a serial no./Admission no for the new info: "))
        if choice3 in data:
            print("The Student is already there in the database")
        else:
            name = input("Enter the name of the student: ")
            grade = input("Enter the class of the student: ")
            roll_no = input("Enter the roll no. of the student: ")
            maths_marks = int(input("Enter the marks in Maths: "))
            physics_marks = int(input("Enter the marks in Physics: "))
            chemistry_marks = int(input("Enter the marks in Chemistry: "))
            english_marks = int(input("Enter the marks in English: "))
            cs_marks = int(input("Enter the marks in Computer Science: "))
            percentage = (maths_marks + physics_marks + chemistry_marks + english_marks + cs_marks)/5
            if percentage in range(80, 101):
                grade = "A"
            elif percentage in range(60, 80):
                grade = "B"
            elif percentage in range(40, 60):
                grade = "C"
            elif percentage in range(20, 40):
                grade = "D"
            elif percentage in range(0, 20):
                grade = "E"
            data[choice3] = {1: name, 2: grade, 3: roll_no, "M": maths_marks, "P": physics_marks,
                             "C": chemistry_marks, "E": english_marks, "CS": cs_marks, 4: percentage, 5: grade}
            print("The info you've added is", data[choice3])

    elif user_input == 8:  # code for viewing database command
        print("Here is the info you asked for:")
        for i in data:
            print("The data of student with admin no.", i, "is", data[i])

    elif user_input == 9:  # Code for exit command
        print("Okay then, thank you for entering The Student Hub, will interact with you next time, have a nice day, bye.")
        break

    else:  # Closing the elif ladder
        print("Enter a valid choice")
