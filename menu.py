from functions import run_cmd
from aws import aws
from docker import docker
from lnx import linux
from httpd import web
from intialSetup import initial_setup

def menu():
    while True:
        print('''
        Press 1 To open Chrome
        Press 2 To open Atom Editor
        Press 3 To get initail Setup & Guest Additions
        Press 4 Manage Amazon Web Service
        Press 5 Manage Docker
        Press 6 Manage Linux & Partitions
        Press 7 Manage Web Configuration
        Press 8 Get Current Date 
        Press 9 Get Calendar
        Press 0 Exit
        ''')
        i = input("\nEnter Your Choice: ")
        if i == "1":
            run_cmd("google-chrome --no-sandbox &")
        elif i == "2":
            run_cmd("atom --no-sandbox &")
        elif i == "3":
            initial_setup()
        elif i == "4":
            aws()
        elif i == "5":
            docker()
        elif i == "6":
            linux()
        elif i == "7":
            web()
        elif i == "8":
            run_cmd("date")
        elif i == "9":
            run_cmd("cal")
        elif i == "0":
            print("Bye... Thank you for using our services! ")
            exit()
        else:
            input("\n\t\t\t Invalid Input! Press Enter to Continue...")

if __name__ == "__main__":
	menu()
