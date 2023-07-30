import getpass
import time
from menu import menu

def get_pass():
    """
    Get Password: This function prompts the user to enter a password and returns it.

    Returns:
        str: The password entered by the user.
    """
    passwd = getpass.getpass("Enter your password: ")
    return passwd

def veirfy_pass():
    """
    Verify Password: This function verifies the user's password and allows for re-verification if the password is incorrect.

    If the password is 'q', the program will exit.

    Returns:
        None
    """
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
        menu()
        

if __name__ == "__main__":
    veirfy_pass()