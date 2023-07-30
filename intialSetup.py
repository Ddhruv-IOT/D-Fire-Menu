import time
import functions
import os


def initial_setup():
    while True:
        print(
            """\033[0;34m
        1.  Press 1 To setup chrome browser.
        2.  Press 2 To config yum repo.
        3.  Press 3 To setup EPEL repo.
        4.  Press 4 To config docker.
        5.  Press 5 To install dependencies for Guest Additions.
        6.  Press 6 To install Apache Server.
        7.  Press 7 To go back to main menu.
        8.  Press 8 To Exit!
        """
        )

        x = input("Enter your choice: ")
        os.system("tput setaf 3")

        if x == "1":
            functions.install_chrome()

        elif x == "2":
            functions.configure_yum_repo()

        elif x == "3":
            functions.config_epel()
        elif x == "4":
            functions.config_docker()
        elif x == "5":
            functions.install_depen()
        elif x == "6":
            functions.install_httpd()
        elif x == "7":
            break
        elif x == "8":
            exit()

if __name__ == "__main__":
    initial_setup()