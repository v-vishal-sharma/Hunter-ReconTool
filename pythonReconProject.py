import os

def nmap():
	print("\n")
	ip = input("Enter the ip address: ")
	cmd = f"sudo nmap -A -p- -Pn {ip} -v > scan.txt"
	print(f"Command being run {cmd}")
	os.system(cmd)
	print("Output saved in file 'scan.txt'")

def gobuster():
	print("\n")
	url = input("Enter the ip address or host url: ")
	wl = input("Enter wordlist path from root: ")
	cmd = f"gobuster dir {url} -w {wl} -t 100 -x php,html > dir.txt"
	print(f"Command being run {cmd}")
	os.system(cmd)
	print("Output saved in file 'dir.txt'")





print(
'''
                                                   
@@@  @@@  @@@  @@@  @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@   
@@@  @@@  @@@  @@@  @@@@ @@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@!@!@@@    @@!    @@!       @@!  @@@  
!@!  @!@  !@!  @!@  !@!!@!@!    !@!    !@!       !@!  @!@  
@!@!@!@!  @!@  !@!  @!@ !!@!    @!!    @!!!:!    @!@!!@!   
!!!@!!!!  !@!  !!!  !@!  !!!    !!!    !!!!!:    !!@!@!    
!!:  !!!  !!:  !!!  !!:  !!!    !!:    !!:       !!: :!!   
:!:  !:!  :!:  !:!  :!:  !:!    :!:    :!:       :!:  !:!  
::   :::  ::::: ::   ::   ::     ::     :: ::::  ::   :::  
 :   : :   : :  :   ::    :      :     : :: ::    :   : :  
                                                           
'''
)



while True :
	print('''
	1. NMAP scan
	2. Gobuster scan
	3. Exit
	''')
	
	choice = int(input(" Enter your choice: "))
	
	if choice == 1:
		nmap()
		
	elif choice == 2:
		gobuster()

	elif (choice==3):
		break
	else:
		continue
	
	
