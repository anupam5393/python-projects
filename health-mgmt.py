"""
Health Management System
"""
import datetime
import os

print(f"\t\t\t\tWelcome to Health Management System!!\n")

patients = {1: 'Harsh', 2: 'Anupam', 3: 'Tanmay'}
tasks = {1: 'check', 2: 'enter'}
events = {1: 'diet', 2: 'exercise'}


def run_system():
    print(f"\tWhat you want to do ?\n")
    for key, t in tasks.items():
        print(f"\t{key}-{t.capitalize()} Diet/Exercise")
    print(f"\t{len(tasks)+1}-Exit")
    choice = int(input(f"\tEnter your Choice:> "))
    print()

    for p, task in tasks.items():
        if choice == p:
            for key, e in events.items():
                print(f"\t{key}-{task.capitalize()} {e.capitalize()}")
            print(f"\t{len(events) + 1}-Exit")
            check_choice = int(input(f"\tEnter your Choice:> "))
            for k, event in events.items():
                if check_choice == k:
                    print(f"\n\tWhose {event.capitalize()} you want to {task.capitalize()} ?\n")
                    for key, person in patients.items():
                        print(f"\t{key}-{person.capitalize()}")
                    name_choice = int(input(f"\tEnter your Choice:> "))
                    file_name = patients[name_choice] + f"-{event}.txt"

                    if task.lower() == 'check'.lower():
                        if os.path.exists(file_name):
                            with open(file_name, 'r') as f:
                                print(f"\n\t\t\t\t{event.capitalize()} chart of {patients[name_choice].capitalize()}")
                                for line in f:
                                    print(f"\t{line}", end="")
                        else:
                            print("\n\tFile Do not Exists!!")

                    elif task.lower() == 'enter'.lower():
                        var = 'items' if event.lower() == 'diet' else 'tasks'
                        count = int(input(f"\n\tEnter the number of {var} to be added:> "))
                        items = []
                        for i in range(1, count + 1):
                            txt = str(datetime.datetime.now()).ljust(35, ' ') + str(
                                input(f"\tEnter {var[:-1]} {i}:> ")).ljust(5, ' ') + '\n'
                            items.append(txt)
                        with open(file_name, 'a') as f:
                            if os.path.getsize(file_name) == 0:
                                header = 'Date/Time'.ljust(35, ' ') + var.capitalize().ljust(5, ' ') + '\n'
                                header2 = '-'.ljust(70, '-') + '\n'
                                f.write(header)
                                f.write(header2)
                            f.writelines(items)
                        print(f"\t{var.capitalize()} logged successfully!!\n")

            if check_choice == len(events) + 1:
                exit()
            elif check_choice not in events.keys():
                print(f"\n\tYou Entered an invalid Choice!!\n")
                exit()
    if choice == len(tasks)+1:
        exit()
    elif choice not in tasks.keys():
        print(f"\n\tPlease Enter a valid Choice!!\n")
        run_system()


run_system()