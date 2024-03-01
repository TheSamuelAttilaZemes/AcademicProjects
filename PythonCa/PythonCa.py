import csv
import socket
import platform
import os
import sys
import psutil

# Function to get the host's IP address
def Host ():
    global hostname  # Declaring 'hostname' as global
    hostname = platform.node()
    print(hostname)
    IPaddress = socket.gethostbyname(hostname)
    print(IPaddress)
    return IPaddress

# Function to perform a ping test and provide user interaction
def PingTest ():
    Get_IP = Host()
    while True:
        ping = os.system('ping ' + Get_IP )
        if ping  :
            print(f'{hostname} is down')
        else :
            print(f'{hostname} is up')
        #user decision
        print('If you wish to continue in Test please YES or NO')
        userInput = input()
        if userInput == 'NO':
            print('Do you wish to go to main menu ? ')
            x = input('YES or NO ? : ')
            if x == 'YES':
                print('You will be returned to the main menu.')
                MainMenu()
            elif x == 'NO':
                print('Thank you and enjoy your day. The script is ending.')
                sys.exit()
            else:
                print('Invalid input')
        elif userInput == 'YES':
            continue
        else:
            print('Invalid Response : Code will continue')
            continue

# Function to collect host information
def PassingHostInfo ():
    HostInfo = {
        'username': os.getlogin(),
        'system': platform.uname().system,
        'Node Name': platform.uname().node,
        'Release': platform.uname().release,
        'Version': platform.uname().version,
        'Machine': platform.uname().machine,
        'Processor': platform.processor(),
        'userDirectory': os.path.expanduser('~'),
        'Physical cores': psutil.cpu_count(logical=False),
        'Total cores': psutil.cpu_count(logical=True),
        'cpufre': psutil.cpu_freq(),
        'Max Frequency': int(psutil.cpu_freq().max / 1000000),
        'Min Frequency': int(psutil.cpu_freq().min / 1000000),
        'Current Frequency': int(psutil.cpu_freq().current / 1000000),
        'Total CPU Usage': psutil.cpu_percent(),
        'svmem': psutil.virtual_memory(),
        # Ram
        'Total Memory': int(psutil.virtual_memory().total / (1024 ** 3)),
        'Available Memory': int(psutil.virtual_memory().available / (1024 ** 3)),
        'Used Memory': int(psutil.virtual_memory().used / (1024 ** 3)),
        'Memory Percentage': psutil.virtual_memory().percent,
        'swap': psutil.swap_memory(),
        'Swap Percentage': psutil.swap_memory().percent,
        # Disk Information
        'partitions': psutil.disk_partitions(),
        'AllPartitions': f"{int(psutil.disk_usage('C:').total / (1024 ** 3))} GB"
    }
    return HostInfo

# Function to print all collected host information
def PritingAllHostInfo (HostInfo):
    for key, value in HostInfo.items():
        print(f'{key}: {value}')
    print('Do you wish to go to main menu ? ')
    x=input('YES or NO ? : ')
    if x == 'YES':
        print('You will be returned to the main menu.')
        MainMenu()
    elif x == 'NO':
        print('Thank you and enjoy your day. The script is ending.')
        sys.exit()
    else:
        print('Invalid input')


# Function to print host information to a CSV file
def CsvPrint (information):
    with open('SystemInfo.csv',mode='w') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',')
        line_count = 0
        for key , value in information.items():
            csv_writer.writerow([key,value])
            line_count += 1
    print('Task done')
    print('Do you wish to go to main menu ? ')
    x = input('YES or NO ? : ')
    if x == 'YES':
        print('You will be returned to the main menu.')
        MainMenu()
    elif x == 'NO':
        print('Thank you and enjoy your day. The script is ending.')
        sys.exit()
    else:
        print('Invalid input')

# Function to display the main menu
def MainMenu ():
    #Main interface for the user
    print('Welcome in the script please choose the would you like to start')
    for i in range(4):
        x = input('Please Enter :Ping Test, Exit , All Information , CSV Report : ')
        if x == 'Ping Test':
            PingTest()
            print('Task done')

        elif x == 'All Information':
            holderr = PassingHostInfo()
            PritingAllHostInfo(holderr)
            print('Task done')

        elif x == 'Exit':
            print('Script is finneshed. Have nice rest of day')
            sys.exit()
        elif x == 'CSV Report':
            holder = PassingHostInfo()
            CsvPrint(holder)
            print('Task done')

        else :
            print(f'Invalid input, attempts {i}')
            print(f'Warning there 3 attempts available and now you have {3-i} ')


MainMenu()






