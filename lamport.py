import sys
number = int(input("Enter the number of Process :"))
processList = list()
logicalClock = {}
timestamp = {}
for i in range(number):
    processName = input(f"Enter the name of {i+1} process : ")
    while True:
        if processName not in processList:
            processList.append(processName)
            break
        else:
            print("Same Process detected!!")
            processName = input("Enter different Process name : ")
for i in processList:
    logicalClock[i] = 0

def addevent():
    while True:
        processName = input("\nEnter the name of the process in which event occured : ")
        if processName in processList:
            ename = input("Enter the name of the event : ")
            etype = input("Enter the type of event (normal/message) : ")
            if etype == 'normal':
                timestamp[ename] = logicalClock[processName]+1
                logicalClock[processName] += 1
            elif etype == 'message':
                while True:
                    ereceivername = input("Enter the name of the receiver event : ")
                    receiverprocessName = input("Enter the name of the receiver process : ")
                    if receiverprocessName in processList:
                        timestamp[ename] = logicalClock[processName]+1
                        timestamp[ereceivername] = timestamp[ename]+1
                        logicalClock[receiverprocessName] = timestamp[ereceivername]
                        break
                    else:
                        print("Enter valid process name!!")
            break
        else:
            print("Enter Valid process name!! ")

while True:
    print("\nEnter")
    print("1. Add Event\n2. Display Timestamp\n3. Exit")
    n = int(input())
    if n == 1:
        addevent()
    elif n == 2:
        print(timestamp)
    elif n == 3:
        sys.exit("Bye Bye User!!")
    else:
        print("Enter correct input.\n")
        n = int(input())