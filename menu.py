import newmenu
from newmenu import run_cmd
import getpass

passwd = getpass.getpass("enter ur password :" )

if passwd != "ss":
    print("password incorrect....")
    exit()

print("""
Press 1 to open Chrome
Press 2 to open Atom
""")

x = input()
if x == '1':
    run_cmd("google-chrome --no-sandbox&")
elif x == '2':
    run_cmd("atom --no-sandbox&")

#install_chrome()
#configure_yum_repo()
#config_epel()
#config_docker()
#install_depen()
