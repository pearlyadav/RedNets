
def header():
    print("""\033[1;32;40m
            __________
            |         |     __________      _____________       |\        |     __________   --------------   --------------                       
            |         |     |                   |       |       | \       |     |                  |          |                   
            |         |     |                   |       |       |  \      |     |                   |         |                        
            |_________|     |                   |       |       |   \     |     |                  |          |               
            |\              |______             |       |       |    \    |     |_____              |         |------------                    
            |   \           |                   |       |       |     \   |     |                  |                      |        
            |     \         |                   |       |       |      \  |     |                   |                     |         
            |       \       |                   |       |       |       \ |     |                  |                      |        
            |         \     |_________      ____|_______|       |        \|     |_________          |         ------------|
            """)
    print("\033[0;37;40m")

def printmenu():
    print("""
\tPress 1: to see date
\tPress 2: to check cal
\tPress 3: conf web server
\tPress 4: to create user
\tPress 5: to create file
\tPress 6: to setup n/w
\tPress 7: to exit""")

def checkIP(ip):
    try:
        octets = list(map(int, ip.split('.')))
    except ValueError:
        return False
    if len(octets) != 4 :
        return False
    for i in octets:
        i = int(i)
        if i<0 or i>255:
            return False
    return True

def IPconfig():
    try:
        ipaddr = input("\tEnter the IP Address of the machine: ")
    except KeyboardInterrupt:
        print("\n\tKeyboard Interrupted!!!\n")
        return IPconfig()
    if checkIP(ipaddr):
        return ipaddr
    else:
        print("\n\tInvalid IP Address!!!\n\tPlease Try Again\n")
        return IPconfig()

while(True):
    header()
    ip = IPconfig()
    print("\tYour IP is: {0}".format(ip))
    printmenu()
    choice = input("\n\tEnter your choice: ")
    if choice == '7':
        break;

