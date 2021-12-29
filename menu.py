import functions
from functions import run_cmd
from welcome import welcome
import getpass
import time

def get_pass():
    passwd = getpass.getpass("Enter your password: ")
    return passwd

def veirfy_pass():
    passwd = get_pass()
    if passwd == 'q':
        exit()

    print()
    x = ["/", "-", "|", "\\"]
    for i in range(5):
        for i in x:
            print("""Verifying User ....... """, end=" ")
            print(f"{i}", end="")
            time.sleep(0.1)
            print(end="\r")
    print("""Verifying User ....... """,end="\n")

    if passwd != "ss":
        print("""[❌] Invalid Password""")
        time.sleep(0.4)
        print("""[❌] Login Failed""")
        time.sleep(0.4)
        print("""[❌] Try again or Enter 'q' to exit""")
        print()
        veirfy_pass()
    else:
        print("""[✔] User Verified """)
        time.sleep(0.4)
        print("""[✔] Welcome Again """)
        time.sleep(0.4)
        print("""\n\t*********************** At Your Service *********************** """)
        main()

def main():
    while 1:
        print("""
        Press 1 to open Chrome
        Press 2 to open Atom
        Press 3 to run date command
        Press 4 to run cal command
        Press 5 to get set-up and config menu
        Press q to exit
        """)

        x = input("Enter Your choice: ")
        if x == 'q':
            exit()
        elif x == '1':
            run_cmd("google-chrome --no-sandbox&")
        elif x == '2':
            run_cmd("atom --no-sandbox&")
        elif x == '3':
            run_cmd("date")
        elif x == '4':
            run_cmd("cal")
        elif x == '5':
            while 1:
                print("""
        Press 1 to setup chrome browser
        Press 2 to config yum repo
        Press 3 to setup EPEL repo
        Press 4 to config docker
        Press 5 to install dependencies for Guest Additions
        Press * to go back to main menu\n""")

                x = input("Enter your choice: ")
                if x == '1':
                    functions.install_chrome()
                elif x == '2':
                    functions.configure_yum_repo()
                elif x == '3':
                    functions.config_epel()
                elif x == '4':
                    functions.config_docker()
                elif x == '5':
                    functions.install_depen()
                elif x == '*':
                    break
        else:
            continue

welcome()
veirfy_pass()
