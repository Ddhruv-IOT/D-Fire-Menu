import os
import subprocess as sp

os.chdir("/")
os.chdir("/etc/yum.repos.d")
print(os.system("pwd"))

f = open("dvd.repo", "w")
f.write(r"""
[dvd1]
baseurl=file:///run/media/root/RHEL-8-4-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///run/media/root/RHEL-8-4-0-BaseOS-x86_64/BaseOS
gpgcheck=0

""")
f.close()

os.system("yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")


os.chdir("/")
os.chdir("/etc/yum.repos.d")
print(os.system("pwd"))

f = open("docker.repo", "w")
f.write(r"""[docker]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
""")
f.close()

os.system("cd")
os.system("echo `yum -y install docker-ce --nobest --allowerasing`")


os.system("yum -y install gcc perl make kernel-headers kernel-devel elfutils-libelf-devel")

print(""" After this:
1. Unmount iso using devices
2. Mount Guest Addition Cd, click Run on PopUp
3. Once its done force mount your ISO file again
4. for increasing Screen Size click right ctrl + c and then maximize.
5. Done!!!"""
)

