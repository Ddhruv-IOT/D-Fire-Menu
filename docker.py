import os

def docker():
    print("\n\n\t\t\t  Welcome to the Docker Menu. How may we help you?")

    while True:
        print("""\033[0;34m
        1.  press 1 for Search image on Dockerhub.
        2.  press 2 for Download Docker image.
        3.  press 3 for List of Docker image.
        4.  press 4 for List of Docker container.
        5.  Press 5 To Create container.
        6.  Press 6 To All exited container.
        7.  Press 7 To start container and attach container.
        8.  Press 8 To Remove container.
        9.  Press 9 To Remove images.
        10. press 10 To Move Back to main menu.
        11. press 11 To Exit!
        """)

        x = input("\nEnter your choice: ")
        os.system("tput setaf 3")

        if x == "1":
            img = input("\nEnter the image name: ")
            os.system("docker search {}".format(img))
            input("\n\t\t Press enter to continue: ")

        elif x == "2":
            z = input("\nEnter the image name: ")
            os.system("docker pull {}:latest".format(z))
            input("\n\t\t Press enter to continue: ")

        elif x == "3":
            os.system("docker images")
            input("\n\t\t Press enter to continue: ")          

        elif x == "4":
            os.system("docker ps")
            input("\n\t\t Press enter to continue: ")          

        elif x == "5":
            os.system("docker images")
            img = input("\nEnter the image name:- ")
            name = input("\nEnter container name:- ")
            os.system("docker run -it --name {}  {}:latest".format(name, img))
            input("\n\t\t Press enter to continue: ")          
            

        elif x == "6":
            os.system("docker ps -a")
            input("\n\t\t Press enter to continue: ")          
            

        elif x == "7":
            os.system("docker ps -a")
            i = input("\nEnter the container name:- ")
            os.system("docker start {}".format(i))
            os.system("docker attach {}".format(i))

        elif x == "8":
            while True:
                os.system("tput setaf 1")
                print("\n1. press 1 for Remove one container.")
                print("2. press 2 for Remove all container.")
                print("3. press 3 for Back to the main menu.")
                print("4. press 4 for Exit.")

                a = input("Enter your choice:- ")

                if a == "1":
                  
                    os.system("docker ps -a")
                    x = input("\nEnter ID or container name:- ")
                    os.system("docker rm {}".format(x))
                    os.system("docker ps -a")
                    input("\n\t\t Press enter to continue: ")          

                elif a == "2":
                    os.system("docker ps -a")
                    os.system("docker rm `docker ps -a -q`")
                    os.system("docker ps -a")
                    input("\n\t\t Press enter to continue: ")          
                    
                    os.system("tput sgr0")

                elif a == "3":
                    break

                elif a == "4":
                    exit()

                else:
                    input("\n\t\t Press enter a valid choice to continue: ")          
                    

        elif x == "9":
          
            os.system("docker images")
            img = input("\nEnter image name:- ")
            os.system("docker rmi -f {}".format(img))
            os.system("docker images")

            input("\n\t\t Press enter to continue: ")          
            

        elif x == "10":
            break

        elif x == "11":
            exit()
if __name__ == "__main__":
    docker()