import Admin, Employees
from time import sleep

run = True
while run:
    print("\nWelcome to Employee Dashboard..")
    print("1. View your details")
    print("2. Request correction in details")
    print("3. Exit the program\n")

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
            print("Invalid choice!")
            sleep(1)
            continue
    except:
        print("Wrong input")
        continue