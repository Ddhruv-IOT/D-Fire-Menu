import os
import time

def aws():
	
	print("\n\n\t\t\t  Welcome to Aws Menu. How may we help you? ")
	while True:
	
		print("""
		\033[0;34m
		Press 1 : To configure AWS
		Press 2 : To create a key-pair
		Press 3 : To create a security-group
		Press 4 : To launch an instance
		Press 5 : To start an instance
		Press 6 : To stop an instance
		Press 7 : To create an EBS volume of 1 GB.
		Press 8 : To create an S3 bucket
		Press 9 : To upload an image in bucket
		Press 10 : To create Cloudfront Distribution
		press 11 : To create Snapshot
		press 12 : TO back main menu
		press 13 : Close the program
	
		""")
		
		ch = input("Enter your choice : ")
		os.system("tput setaf 3")

	
		if int(ch) == 1:
			os.system('aws configure')
	
		elif int(ch) ==2:
			keyname = input("\nEnter the keyname :- ")
			os.system('aws ec2 create-key-pair --key-name {}'.format(keyname))
	
		elif int(ch) ==3:
			description = input("\nEnter The Description :-")
			group_name = input("\nEnter The Group Name :-")
			os.system('aws ec2 create-security-group --description {} --group-name {}'.format(description, group_name ))
   
		elif int(ch) ==4:
			imageid =input("\nEnter the image id :- ")
			securityid = input("\nEnter the security group id :-")
			keyname = input("\nEnter the keyname :-")
			os.system('aws ec2 run-instances --image-id {} --instance-type t2.micro --security-group-ids {} --key-name {}'.format(imageid, securityid ,keyname))


		elif int(ch) ==5:
			instanceid = input("\nEnter your instance-id :-")
			os.system('aws ec2 start-instances --instance-ids {}'.format(instanceid))
   
		elif int(ch) ==6:
			instanceid = input("\nEnter your instance-id :-")
			os.system('aws ec2 stop-instances --instance-ids {}'.format(instanceid))

		elif int(ch) ==7:
			print("Select the Availabilty Zones ")
			print("""
				\n
				Press 1 : ap-south-1a
				Press 2 : ap-south-1b
				Press 3 : ap-south-1c
				""")
			s = input("\nSelect Availability Zone :-")
			if int(s) == 1:
				az = "ap-south-1a"
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1a")
			elif int(s) == 2:
				az = "ap-south-1b"
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1b")

			elif int(s) == 3:
				az = "ap-south-1c"
				os.system("aws ec2 create-volume --volume-type gp2 --size 1 --availability-zone ap-south-1c")


		elif int(ch) ==8:
			bname = input("\nEnter the bucket name :-")
			region = input("\nEnter the region :-")
			os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint=ap-south-1'.format(bname, region))
	
		elif int(ch) ==9:
			bname = input("\nEnter your bucket name :-")
			location = input("\nEnter the loaction of image :-")
			iname = input("\nEnter image name :-")
			os.system('aws s3api put-object --bucket {} --body {} --key {}'.format(bname, location, iname))

		elif int(ch) ==10:
			domain_name = input("\nEnter the Domain name :-")
			iname = input("\nEnter the image name :-")
			os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}'.format(domain_name,iname))

		elif int(ch) ==11:
			vd =input("Enter the volume id :- ")
			desc =input("Enter the description :- ")
			os.system("aws ec2 create-snapshot --volume-id {} --description {}".format(vd,desc))

		elif int(ch) ==12:
			break

		elif int(ch) ==13:
			exit()

		else :
			print("\n\t\t Press enter a valid choice to continue")

if __name__ == "__main__":
	aws()