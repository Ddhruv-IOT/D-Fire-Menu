import functions
from functions import run_cmd
import getpass

def get_pass():
    passwd = getpass.getpass("Enter your password: ")
    return passwd

def veirfy_pass():
    passwd = get_pass()
    if passwd == 'q':
        exit()
    if passwd != "ss":
        print("Incorrect Password")
        print("Try again or Enter 'q' to exit")
        veirfy_pass()
    else:
        main()

def main():
    while 1:
        print("""
        Press 1 to open Chrome
        Press 2 to open Atom
        """)

        x = input()
        if x == '1':
            run_cmd("google-chrome --no-sandbox&")
        elif x == '2':
            run_cmd("atom --no-sandbox&")
        elif x == '3':
            run_cmd("date")
        elif x == '4':
            while 1:
                print("""
                1. for installing chrome
                2. for configuring yum
                3. for
                4. for
                * to go back to main menu """)
                x = input("Enter ur choice")
                if x == '1':
                    functions.install_chrome()
                elif x == '2':
                    functions.configure_yum_repo()
                elif x == '*':
                    break
        else:
            break

veirfy_pass()
#install_chrome()
#configure_yum_repo()
#config_epel()
#config_docker()
#install_depen()
