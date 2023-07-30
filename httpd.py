import os
import subprocess as sp
from time import sleep


def web():
    """
    HTTPD Menu: This function provides a menu-driven interface to interact with Apache Web Server (httpd) functionalities.

    The user can choose from the following options:
        1. Press 1 to install Apache Web Server Software
        2. Press 2 To Create Web Pages
        3. Press 3 To Start Services
        4. Press 4 To Stop Services
        5. Press 5 TO Back to the main menu
        6. Press 6 Close The Program

    Returns:
        None
    """
    print("\n\n\t\t\t Welcome to HTTPD Menu. How may we help you ?")

    while True:
        print(
            """\033[0;34m
        1. Press 1 to install Apache Web Server Software
        2. Press 2 To Create Web Pages
        3. Press 3 To Start Services
        4. Press 4 To Stop Services
        5. Press 5 TO Back to the main menu
        6. Press 6 Close The Program
        """
        )

        ch = input("\nEnter your choice: ")
        os.system("tput setaf 3")

        if ch == '1':
            x = sp.getstatusoutput("rpm -q httpd")
            if x[0] != 0:
                os.system("yum install httpd")
                sleep(2)
            else:
                print("\nAlready installed ")
                sleep(2)

        elif ch == '2':
            page = input("\nEnter name of html page: ")
            os.system(f"vim /var/www/html/{page}.html")
            print("\nWeb Page created successfully")
            sleep(2)

        elif ch == '3':
            os.system("systemctl start httpd")
            print("\nYour service has been started")
            sleep(2)

        elif ch == '4':
            os.system("systemctl stop httpd")
            print("\nYour service has been stopped")
            sleep(2)

        elif ch == '5':
            break
        
        elif ch == "6":
            exit()

        else:
            input("\n\t\t Press enter a valid choice to continue: ")


if __name__ == "__main__":
    web()
