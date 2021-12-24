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
        else:
            break

veirfy_pass()
#install_chrome()
#configure_yum_repo()
#config_epel()
#config_docker()
#install_depen()
