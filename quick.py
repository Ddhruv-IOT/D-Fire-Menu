from new_menu import run_cmd

print("""
Press 1 to open Chrome
Press 2 to open Atom
""")

x = input()
if x == '1':
    run_cmd("google-chrome --no-sandbox&")
elif x == '2':
    run_cmd("atom --no-sandbox&")
