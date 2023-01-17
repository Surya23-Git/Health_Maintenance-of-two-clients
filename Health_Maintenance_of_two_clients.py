import os
import datetime

def users():
    print("This algorithm is for maintening health of Two Users")
    print("----- Users Available ------")
    print("""1. Clint
2. Loki\n""")

    user = {1: "Clint", 2: "Loki"}

    print("Each user need to maintain Diet and Excercise for proper health")
    print("------ Maintenance Menu -----")
    print("""1. Diet
2. Excercise""")
    Main_menu = {1: "Diet", 2: "Exercise"}
    print("\n------------------------------------------------------------------------------------\n")


def logic():
    while (True):

        while (True):
            print("Input -- 1. For Clint, 2. Loki, 'q' for exit\n")
            user_input = (input("Choose the Available Options: "))
            if (user_input == '1' or user_input == '2' or user_input == 'q'):
                break
            else:
                print("Enter the Right Parameter")

        if user_input == '1':
            print(f"This is the Clint Profile Menu")
            print("""Choose: 
            A. Diet
            B. Execercise
            C. Previous Menu""")

            while (True):

                while (True):
                    item = str(input("Choose among [A/B/C]:")).upper()
                    if (item == 'A' or item == 'B' or item == 'C'):
                        break
                    else:
                        print("Enter the Right Parameter")

                if item == 'A':
                    # menu = int(input("Choose 1. For Add, 2. For read, 3. Previous Menu "))
                    if (os.path.exists('Clint_Diet.txt')):
                        pass
                    else:
                        Client_Diet = open('Clint_Diet.txt', 'x')
                    print(f"This section is to view and edit the Clint Diet")
                    print("""Choose: 
                X. To add data
                Y. To read data
                Z. Previous Menu""")
                    C_Data_mod_d = str(input("Please choose among [X/Y/Z]: ")).upper()

                    if (C_Data_mod_d == 'X'):
                        data = str(input("\nWhat do you want to add: "))
                        with open('Clint_Diet.txt', 'a') as diet_clint:
                            diet_clint.write(
                                "\n" + str(datetime.datetime.now().strftime('%D %H:%M:%S')) + ": " + data + "\n\n")
                        print(f"This is the Clint Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (C_Data_mod_d == 'Y'):
                        diet_clint = open('Clint_Diet.txt', 'r')
                        print(f"\n{diet_clint.read()}")
                        print(f"This is the Clint Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (C_Data_mod_d == 'Z'):
                        print("You will be directed to Previous Menu")
                        print(f"This is the Clint Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")

                if item == 'B':
                    if (os.path.exists('Clint_Exercise.txt')):
                        pass
                    else:
                        Clint_Exercise = open('Clint_Exercise.txt', 'x')
                    print(f"This section is to view and edit the Clint Exercise")
                    print("""Choose: 
                X. To add data
                Y. To read data
                Z. Previous Menu\n""")

                    C_Data_mod_E = str(input("Please choose among [X/Y/Z]: ")).upper()

                    if (C_Data_mod_E == 'X'):
                        data = str(input("\nWhat do you want to add: "))
                        with open('Clint_Exercise.txt', 'a') as exercise_clint:
                            exercise_clint.write(
                                "\n" + str(datetime.datetime.now().strftime('%D %H:%M:%S')) + ": " + data + "\n\n")
                        print(f"This is the Clint Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (C_Data_mod_E == 'Y'):
                        exercise_clint = open('Clint_Exercise.txt', 'r')
                        print(f"\n{exercise_clint.read()}")
                        print(f"This is the Clint Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (C_Data_mod_E == 'Z'):
                        print("You will be directed to Previous Menu\n")
                        print(f"This is the Clint Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")

                if item == 'C':
                    print("You will be directed to Previous Menu")
                    logic()


        if user_input == '2':
            print(f"This is the Loki Profile Menu")
            print("""Choose: 
            A. Diet
            B. Execercise
            C. Previous Menu""")
            while (True):

                while (True):
                    item = str(input("Choose among [A/B/C]:")).upper()
                    if (item == 'A' or item == 'B' or item == 'C'):
                        break
                    else:
                        print("Enter the Right Parameter")

                if item == 'A':
                    # menu = int(input("Choose 1. For Add, 2. For read, 3. Previous Menu "))
                    if (os.path.exists('Loki_Diet.txt')):
                        pass
                    else:
                        Loki_Diet = open('Loki_Diet.txt', 'x')
                    print(f"This section is to view and edit the Clint Diet")
                    print("""Choose: 
                X. To add data
                Y. To read data
                Z. Previous Menu""")
                    L_Data_mod_d = str(input("Please choose among [X/Y/Z]: ")).upper()

                    if (L_Data_mod_d == 'X'):
                        data = str(input("\nWhat do you want to add: "))
                        with open('Loki_Diet.txt', 'a') as diet_loki:
                            diet_loki.write(
                                "\n" + str(datetime.datetime.now().strftime('%D %H:%M:%S')) + ": " + data + "\n\n")
                        print(f"This is the Loki Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (L_Data_mod_d == 'Y'):
                        diet_loki = open('Loki_Diet.txt', 'r')
                        print(f"\n{diet_loki.read()}")
                        print(f"This is the Loki Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (L_Data_mod_d == 'Z'):
                        print("You will be directed to Previous Menu")
                        print(f"This is the Loki Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")

                if item == 'B':
                    if (os.path.exists('Loki_Exercise.txt')):
                        pass
                    else:
                        Loki_Exercise = open('Loki_Exercise.txt', 'x')
                    print(f"This section is to view and edit the Clint Exercise")
                    print("""Choose: 
                X. To add data
                Y. To read data
                Z. Previous Menu\n""")

                    L_Data_mod_E = str(input("Please choose among [X/Y/Z]: ")).upper()

                    if (L_Data_mod_E == 'X'):
                        data = str(input("\nWhat do you want to add: "))
                        with open('Loki_Exercise.txt', 'a') as exercise_loki:
                            exercise_loki.write(
                                "\n" + str(datetime.datetime.now().strftime('%D %H:%M:%S')) + ": " + data + "\n\n")
                        print(f"This is the Loki Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (L_Data_mod_E == 'Y'):
                        exercise_loki = open('Loki_Exercise.txt', 'r')
                        print(f"\n{exercise_loki.read()}")
                        print(f"This is the Loki Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")
                    elif (L_Data_mod_E == 'Z'):
                        print("You will be directed to Previous Menu\n")
                        print(f"This is the Loki Profile Menu")
                        print("""Choose: 
                        A. Diet
                        B. Execercise
                        C. Previous Menu""")

                if item == 'C':
                    print("You will be directed to Previous Menu")
                    logic()

        if user_input == 'q':
            break


users()
logic()
