import datetime


def depositcash():
    deposit_amount = float(input('Please enter amount to be deposited:'))
    username = uname
    filename = username + '.txt'
    transactionfilename = username + '_transactionhistory.txt'
    transactionfile = open(transactionfilename, 'a')
    file = open(filename, 'a')
    balance = 0
    new_balance = 0
    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open(filename, 'w+') as file2:
        new_balance = balance + deposit_amount
        new_balance = str(new_balance)
        file2.write(new_balance)
        print('Your new balance is:', new_balance)
    with open(transactionfilename, 'a') as file3:
        balance = str(balance)
        deposit_amount = str(deposit_amount)
        file3.write(str(datetime.datetime.now()))
        file3.write('\nPrevious balance: ' + balance + '. Deposit amount is:' +
            deposit_amount + '. New balance:' + new_balance + '\n')

    file.close()


def withdrawcash():
    withdrawn_amount = float(input('Please enter amount to be withdrawn:'))
    username = uname
    filename = username + '.txt'
    transactionfilename = username + '_transactionhistory.txt'
    transactionfile = open(transactionfilename, 'a')
    file = open(filename, 'a')
    balance = 0
    new_balance = 0

    with open(filename, 'r') as file:
        for i in file:
            balance = float(i)
    with open(filename, 'r') as file2:
        if withdrawn_amount > balance:
            print('You have insufficient balance. Your balance is:', balance)


        else:
            with open(filename, 'w+') as file2:
                new_balance = balance - withdrawn_amount
                new_balance = str(new_balance)
                file2.write(new_balance)
                print('Your new balance is:', new_balance)
                with open(transactionfilename, 'a') as file3:
                    balance = str(balance)
                    withdrawn_amount = str(withdrawn_amount)
                    file3.write(str(datetime.datetime.now()))
                    file3.write('\nPrevious balance: ' + balance + '. Withdrawn amount is:' +
                        withdrawn_amount + '. New balance:' + new_balance + '\n')

            file.close()
    file.close()


def chkbalance():
    username = uname
    filename = username+'.txt'
    file = open(filename,'a')
    with open(filename,'r') as file:
        for i in file:
            balance = float(i)
        file.seek(0)
        if file.read(1):
            print('Your Balance is: ',balance)
        else:
            print('No Balance Left')
    file.close()


#################################################################################################

print(' \n                         Hello! Welcome to SBI Bank.                  ')
print('*'*100,'\n')
print('Please login to proceed.\n')



uname = input('Please Enter Username: ')
unamee = f'Username:{uname}'
pwd = input('Please Enter PWD: ')
pwdd = f'Password:{pwd}'
print('*' * 100, '\n')

if uname == '' and pwd == '':
    print('Enter The Value')
    uname = input('Please Enter Username: ')
    unamee = f'Username:{uname}'
    pwd = input('Please Enter PWD: ')
    pwdd = f'Password:{pwd}'
    print('*' * 100, '\n')

else:
    for line in open("cust_profile.txt", "r").readlines():
        login_info = line.split()

        if unamee == login_info[0] and pwdd == login_info[1]:
            print('                         Login Successful \n')
            print('                           Welcome',uname)
            print('*' * 100, '\n')
            opt = int(input('Do you want to continue? Enter 0 to continue, 1 to Logout: '))
            while True:
                if opt == 0:

                    print('What would you like to do ? '
                          '\n1. Deposit Money'
                          '\n2. Withdraw Money'
                          '\n3. Check Balance'
                          '\n4. Check Transaction History')

                    opt = int(input('Enter Your Choice: '))
                    while True:
                        if opt == 1:
                            depositcash()
                            break
                        elif opt == 2:
                            withdrawcash()
                            break
                        elif opt == 3:
                            chkbalance()
                            break
                        elif opt == 4:
                            transactionfilename = uname + '_transactionhistory.txt'
                            transactionfile = open(transactionfilename, 'a')
                            with open(transactionfilename,'r') as f:
                                f.seek(0)
                                if f.read(1):
                                    print(f.read())
                                    break
                                else:
                                    print('There is no transaction history.')
                                    break
                            file.close()

                        else:
                            print('Wrong Option')
                            break

                    opt = int(input('Do you want to continue? Select 0 to Continue, 1 to Logout: '))

                    continue

                elif opt == 1:
                    print('Good Bye')
                    break

                else:
                    print('Wrong option')
                    opt = int(input('Do you want to continue? Select 0 to Continue, 1 to Logout: '))


            break
    else:
        print('Incorrect Username or Password. Please try again later or contact our Customer Care Representative.')
