# Script to clock hours

import subprocess
import time
import io


def clear_screen():
    subprocess.run(["cls"], shell=True)


def timebreak():
    time.sleep(3)


def call_script():
    subprocess.run(["python", "test.py"], shell=True)    


def clock_hours():
    clear_screen()
    clock_hours = open("hoursworked.log", "a")
    clear_screen()
    hours_worked = input("""
    Clock hours below.             
        
    
    Enter hours worked: """)
    clock_hours.write("{}\n".format(hours_worked))
    clock_hours.close()
    print("\n    Hours clocked successfully!")
    time.sleep(1)
    call_script()


def view_hours_worked():
    clear_screen()
    value = 0
    with open("hoursworked.log", "r") as hours_worked:
        for hours in hours_worked:
            val = float(hours) + value 
            value = val
        print("    Hours worked: {}".format(value))
        timebreak()
        call_script()       


def reset_hours_worked():
    with open("hoursworked.log", "w") as remove:
        remove.write("")
        call_script()


def exit_script():
    print("\n    Exiting...")
    time.sleep(0.5)
    exit()


def main():
    clear_screen()
    menu_of_items = input("""    
    Please select from the following
    
    1) Clock hours
    2) View hours worked
    3) Reset hours Worked
    4) Exit

    >> """)
    if (menu_of_items == "1"):
        clock_hours()
    elif (menu_of_items == "2"):
        view_hours_worked()
    elif (menu_of_items == "3"):
        reset_hours_worked()
    elif (menu_of_items == "4"):
        exit_script()


if __name__ == "__main__":
    main()
