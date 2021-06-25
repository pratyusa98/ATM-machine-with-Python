import string
import random

cust_profile = open("cust_profile.txt","a+")

cnt = 1

def randompwd():
    chars = string.ascii_uppercase+ string.ascii_lowercase+string.digits
    size = random.randint(8,12)
    return ''.join(random.choice(chars) for x in range (size))

print(' \n                         Hello! Welcome to SBI Bank.                  ')
print('                             This is Admin account. \n')
print('*'*100,'\n')

choice = int(input('Enter 0 to proceed, 1 to terminate: '))

while True:
    if choice == 0:
        print('                What would you like to do today? '
              '\n1. Create Customer profile'
              '\n2. View customer transaction history'
              '\n3. Search customer profile\n')

        choice = int(input('Enter your choice:'))
        if choice == 1:
            fullname = input('Enter Customer Name: ')
            address = input('Enter Address: ')
            uname = fullname[0:2]+'020'
            username_integer = uname + str(cnt)
            with open('cust_profile.txt','r') as f:
                data = f.read()
                if (uname not in data):
                    temp = uname
                    temp2 = randompwd()
                    cust_profile.write('Username:' + uname + '\t'
                                       + 'Password:' + temp2 + '\t' + 'First Name:' + fullname
                                       + '\t'  + 'Address:' + address + "\n")

                    print("\nCreated username is:", temp, 'and password is', temp2, '\n')

                else:
                    cnt = cnt+1
                    temp = username_integer
                    temp2 = randompwd()
                    cust_profile.write('Username:' + username_integer
                                       + '\t' + 'Password:' + temp2 + '\t' + 'First Name:'
                                       + fullname + '\t' + 'Address:' + address + "\n")

                    print("\nCreated username is:", temp, 'and password is', temp2, '\n')

        elif choice == 2:
            username = input('Enter username that you would like to view:')
            transactionfilename = username + '_transactionhistory.txt'
            transactionfile = open(transactionfilename, 'a')
            with open(transactionfilename,'r') as f:
                f.seek(0)
                if f.read(1):
                    print(f.read())
                    break
                else:
                    print('No Transaction History For This Customer')
                    break

        elif choice == 3:
            data = input('Please enter customer detail to search:')
            file = open('cust_profile.txt')
            for line in file:
                line= line.rstrip()
                if data in line:
                    print(line)

            break

        else:
            print('Wrong Option')
            choice = int(input('Enter 0 to proceed, 1 to terminate:'))



    elif choice == 1:
        print('Terminate Good Bye')
        break
    else:
        print('Wrong option')
        choice = int(input('Enter 0 to proceed, 1 to terminate: '))

cust_profile.close()