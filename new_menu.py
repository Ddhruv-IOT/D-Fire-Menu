import os
import subprocess as sp

def run_cmd(command): 
	""" will run os based commands """
	os.system(command)

def file_maker(file_name, mode, data):
	""" Make a file or open it """

	fptr = open(file_name, mode)
	fptr.write(data)
	fptr.close()  

def change_dir(dir_path): 
	""" To Change Dir """
	
	os.chdir(dir_path)

def configure_yum_repo():
	""" Configure ISO DVD for installing data """

	data = (r"""
[dvd1]
baseurl=file:///run/media/root/RHEL-8-4-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///run/media/root/RHEL-8-4-0-BaseOS-x86_64/BaseOS
gpgcheck=0

""")

	change_dir(r"/")
	change_dir(r"/etc/yum.repos.d")
	file_maker("dvd.repo", "w", data)

def config_epel():
	""" Will configure EPEL-Release for RHEL 8.4 """
	run_cmd(r"yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")


def config_docker():
	""" Configure docker-ce """

	data = (r"""[docker]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
""")
	
	change_dir(r"/")
	change_dir(r"/etc/yum.repos.d")
	file_maker("docker.repo", "w", data)
	change_dir(r"/root")
	run_cmd("echo `yum -y install docker-ce --nobest --allowerasing`")

def yum_install(pkg_name):
	""" Install from Yum """

	os.system(f"yum -y install {pkg_name}")

def install_depen():
	""" Install dependencies and guest editions """

	yum_install("gcc perl make kernel-headers kernel-devel elfutils-libelf-devel")

	print(""" After this:
	1. Unmount iso using devices
	2. Mount Guest Addition Cd, click Run on PopUp
	3. Once its done force mount your ISO file again
	4. for increasing Screen Size click right ctrl + c and then maximize.
	5. Done!!!""")

def install_httpd():
	yum_install("httpd")
	

def install_chrome():
	data = r"""
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
"""
	change_dir(r"/")
	change_dir(r"/etc/yum.repos.d")
	file_maker("chrome.repo", "w", data)

	yum_install("google-chrome-stable")
	run_cmd("yum update google-chrome-stable")
	

run_cmd("tput setaf 45")
run_cmd("figlet Auto-Installtion")
install_chrome()
#configure_yum_repo()
#config_epel()
#config_docker()
#install_depen()

