
x = int(input())
while(x != 0):
    print(
        "Enter choice : \n"
        "1: Show Names \n"
        "2: Names of marks above 90 \n"
        "3: Show Topper \n"
        "4: Names from kopergaon \n"
        "5: Name NOT from Kopergaon \n"
        "0: Quit \n"
    )

    if x == 1:
        # Show Names
        print([student[0] for student in students])
    elif x == 2:
        # Names of marks above 90
        print([student[0] for student in students if student[2] > 90])
    elif x == 3:
        # Show Topper
        topper = list(filter(lambda x: max(x[2]), students))
        print(topper)
    elif x == 4:
        # Names from kopergaon
        print([student[0] for student in students if student[3].lower() == "kopergaon"])
    elif x == 5:
        # Name NOT from Kopergaon
        print([student[0] for student in students if student[3].lower() != "kopergaon"])
    elif x == 0:
        print("Quitting...")
        break
    else:
        print("Invalid choice")