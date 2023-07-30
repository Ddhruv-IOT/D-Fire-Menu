import os
import time


def linux():
    print("\n\n\t\t\t  Welcome to Linux Menu. How may we help you?")

    while True:
        os.system("tput setaf 3")
        print(
            """\033[0;34m
		1. Press 1 : Run Linux Command
		Enter 'Exit' to exit from the command line
		2. Press 2 : Create Partition
		3. Press 3 : Create LVM
		4. Press 4 : Check mounted disk
		5. Press 5 : Volume Group List
		6. Press 6 : Yum Configure
		7. Press 7 : Back to main menu
		8. Press 8 : Close the program
		
		"""
        )

        a = input("\nEnter your choice: ")
        os.system("tput setaf 3")

        if a == "1":
            while True:
                command = input("\nInput the command: ")
                os.system(command)
                if (
                    command == "exit"
                ):  # or (z=="Exit") or (z=="EXIT") or (z=="Y")or(z=="y"):
                    break

        elif a == "2":
            os.system("fdisk -l")
            b = input("\tEnter disk name: ")
            os.system("fdisk {}".format(b))
            time.sleep(2)

            print("\n\nFormatting the Partition")
            os.system("mkfs.ext4 {}".format(b))
            print("Successfully Formatted")
            time.sleep(2)

            d = input("\n\n Make Directory for mounting: ")
            os.system("mkdir /{}".format(d))
            print("Directory successfully Created")
            time.sleep(2)

            os.system("\n\nfdisk -l")
            m = input("\t Mount The Directory, Please enter the disk name: ")
            os.system("mount {} {} ".format(m, d))
            print("successfully Mounted")
            time.sleep(2)

        elif a == "3":
            os.system("\n\nfdisk -l")
            print("Enter the both disks name: ")
            i = input("pvcreate ")
            j = input("pvcreate ")
            os.system("pvcreate {} {}".format(i, j))
            print("Successfully pv created")
            time.sleep(2)

            print("\n\nCreate volume group")
            l = input("Give me group name: ")
            os.system("vgcreate {} {} {}".format(l, i, j))
            print("Successfully volume group created")
            time.sleep(2)

            print("\n\nSet the Size of lv")
            n = input("Size(in GB) -  ")
            o = input("Set Name -")
            os.system("lvcreate --size {}GB --name {} {}".format(n, o, l))
            print("Successfully lv created")
            time.sleep(2)

            print("\n\nFormat the lv")
            os.system("mkfs.ext4 /dev/{}/{}".format(l, o))
            print("Successfully Formatted")
            time.sleep(2)

            print("\n\nBefore the mounting please create Directory")
            p = input("mkdir ")
            os.system("mkdir {}".format(p))
            print("Directory created")
            time.sleep(2)

            print("\n\nMount your Directory")
            os.system("mount /dev/{}/{} /{}".format(l, o, p))
            print("Successfully Mounted please check with df -h command ")
            print("\n Back to the menu")

        elif a == "4":
            os.system("df -h")

        elif a == "5":
            os.system("vgdisplay")

        elif a == "6":
            os.system(
                "yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm"
            )

        elif a == "7":
            break

        elif a == "8":
            exit()

        else:
            input("\n\t\t Press enter a valid choice to continue: ")
            continue


if __name__ == "__main__":
    linux()
