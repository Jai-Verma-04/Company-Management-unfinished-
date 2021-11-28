from time import sleep

run = True
while True:
    print("\nWelcome to the Company Management Program.\n")
    print("Login as: ")
    print("1. Admin")
    print("2. Employee")
    print("3. Exit")
    print()
    
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            print("Thanks for using the program!")
            sleep(1)
            run = False
        else:
            print("Invalid Choice")
            continue
    except:
        print("Wrong Input")

    