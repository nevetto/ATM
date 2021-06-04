# ATM IF ELSE STATEMENT

# def reg():
#     print('                             WELCOME TO NEVETTO BANK FOR AFRICA')
# gui = input(' 1. Register\n 2. Perform Transaction\n 3. Quit')
# if(gui != "1" or gui != "2" or gui != "3"):
#     print('Enter correct value')

    

# print('                             WELCOME TO NEVETTO BANK FOR AFRICA')
# gui = input(' 1. Register\n 2. Perform Transaction\n 3. Quit')
# if(gui != "1" or gui != "2" or gui != "3"):
#     print('Enter correct value')
# if(gui == '1'):
#     reg = input('Enter your Firstname')
#     reg1 = input('Enter your Middle Name')
#     reg2 = input('Enter your Last Name')
#     reg3 = input('enter your Date of Birth')

#     c = input("do you wish to replace any word?\n if yes\n press 1 to modify>>>>\n press 2 to continue>>>>")
#     if(c=='1'):
#         d1= input("type the first value to modify>>>>")
#         d = input("enter the new word you want to replace it with>>>>")
#         abcd = reg.replace(d1,d)
#     else:
#         print()
 


#     reg4 = input('Fill Account Type:\n 1. Saving\n2. Current\n3. Domicilliary)')
#     if (reg4 == '1'):
#         a = "Savings"
#         print("You Have Opened  Savings Account")
#     if(reg4 == '2'):
#         b = "Current"
#         print("You Have Opened  Current Account")
#     elif(reg4 == '3'):        
#         c = "Domicilliary"
#         print("You Have Opened  Domicilliary Account")
#     else:
#         ('Select Account Type')

#     names = []
#     if(reg != '' and reg1 != '' and reg2 != '' and reg3 != '' and reg4 !=''):        
#         if True:
#             import random
#             user = (random.randrange(10,100000000))   
#             names.append(user)       
#             print((reg2.upper().strip()) + ' ' +  (reg.upper().strip()) + ' ' + (reg1.upper().strip()) + ' Your Account Number is ' +
#              str(names))        
#         pin = input('input Four Digits For Your Pin')
#         print('Your Pin Number is' + ' ' + str(pin.encode()) + ' ' + 'Note You Must Not Share Your Pin')
#         oper = input('Do you want to perform another operations\n 1. Yes\n 2. No')
#     if(oper == "1"):
#         oper1 = input('Enter your pin')            
#         if(oper1.strip() == pin):
#             oper2 = gui
#             print(gui)      
#         else:
#             print('Incorrect PIn')
#     elif(oper == '2'):
#         print('THANKS FOR BANKING WITH US')
# elif(gui == '2'):
#     d = input('Select The Transaction You Want to Perform\n 1. Withdraw\n 2. Transfer\n 3. Check Balance\n 4. TopUp\n 5. Loans\n 6. PayBills\n 7. AccountSetings')
     
#     if(d == '1' ):
#         e = input('Enter Your Pin') 
#         if(e != ''):
#             witd = input('Select Account Type\n 1. Savings\n 2. Current\n Domicilliary')
#             witda = input('Enter Amount')
#             print(witd)
#             print('Please wait.......Your Transaction is processing')
#             print()
#             print()
#             print('TAKE YOUR CASH')
#             witd2 = input('Do You Want To Perform Another Transaction\n 1. Yes\n 2. No')
#             if(witd2 == "1"):
#                 witd3 = d
#                 print(witd3)
            
#             else:
#                 print('THANKS FOR BANKING WITH US')
#     elif(d == "2"):
#         trans = input('Enter Your Pin')
#         if(trans != ''):
#             trans2 = input('Select Account Type\n 1. Savings\n 2. Current\n Domicilliary')
#             trans3 = input('Enter your Account Number')
#             trans4 = input('Enter Recipent Account Number') 





            #USING FUNCTIONS FOR ATM
            # def bank_details():
#     print('                             WELCOME TO NEVETTO BANK FOR AFRICA')
#     gui = input(' 1. Register\n 2. Perform Transaction\n 3. Quit')
# #ACCOUNT REGISTRATION    
#     def process(g,reg):
#         if (gui == "1"):
#             import random
#             accno = (random.randrange(100000000))
#             userno = (random.randrange(10000))
#             print(reg["name"] + ' you have sucessfully registered, your account number is ' + "11" +(str(accno)) + 'and your user number is ' + "14" + str(userno))
#             pin = input('enter four digits number four your pin')
#             anothertransac = input('Do you want to perform another Transaction?\n 1. Yes\n 2. No')
#             if(anothertransac == '1'):
#                 print(bank_details())
#             else:
#                 print('Thank you for banking with us')
#      # TO PERFORM TRANSACTIONS           
#     def processingTransac(g):
#         if (gui == "2"):
#             login = input('Enter Account Number')
#             pinNo = input('Enter pin number')
#             if (login and pinNo != ''):
#                 trans = input(' 1.Transfer\n 2.Withdraw\n 3.Check Balance\n 4.Topup\n 5.Back')
#             else:
#                 print('enter a valid pin')
#     # TRANFER PROCESSING
#             def transProcess(tran,p):
#                 if (tran == "1"):
#                     beneficiaryName = input('Enter beneficiary first name and last name')
#                     request = input('Enter Beneficiary Account Number')
#                     transfer = input('Enter ammount you want to transfer')
#                     print('You are Trying To Transfer ' + "N" + str(transfer) + ' to ' + beneficiaryName)
#                     proceed = input('Do you want to Proceed?\n 1. Proceed\n 2.Back')
#                     if(proceed == '1'):
#                         reenterPin = input('Enter your pin')
#                         if (reenterPin == pinNo):
#                             print('You have successfully transfered ' + str(transfer) + ' to ' + beneficiaryName)
#                         else:
#                             print("invalid pin")
#                             print(transProcess(tran,p))
#                         performOtherTransac= input('Do you want to perfom another transaction or logout\n 1. Perform Transaction\n 2. Logout')
#                         if(performOtherTransac== '1'):
#                             print(processingTransac(g))
#                         else:
#                             print('THANK YOU FOR BANKING WITH US')
#             #CHECK BALANCE
#             def checkBalance(tra,p,acc):
#                 if (tra == "3"):
#                     pinToCheckBalance = input('Enter your pin')
#                     if (pinNo == pinToCheckBalance):
#                         print('Your balance is N'acc)
                    
#                         # return acc - transfer
#                         # print ('Your balance is N' + str(checkBalance(transfer)) )
#                     else:
#                         print('invalid pin')
#                         print(checkBalance(tra,p,acc))

#             checkBalance(trans,pinNo,50000)
#             transProcess(trans,pinNo)
#     processingTransac(gui)
        
#     process(gui, {"name":input('please enter your first name and last name'), "email":input('Enter you valid email address')})
# bank_details()






#ATM OOP FUNCTION 
        
import mysql.connector
mycon = mysql.connector.connect(host="localhost", user="root",password="",  database="bankApp_db")
# mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE bankApp_db")


# mycursor = mycon.cursor()
# mycursor.execute("CREATE TABLE customersreg_info(id INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(20), Last_Name VARCHAR(20), Sex VARCHAR(10), Address VARCHAR(50), Account_Type VARCHAR(15), Phone_Number VARCHAR(11), Account_No VARCHAR(15), Pin_Number VARCHAR(5), Account_Balance VARCHAR(50))")
 
  

import sys
import random
class ATMClass:
    def __init__(self):
        self.connection()
        self.option()
    
    def connection(self):
        self.mycon = mysql.connector.connect(host="localhost", user="root",password="",  database="bankApp_db")
        self.mycursor = self.mycon.cursor()

        
    def option(self):
        print("""WELCOME TO NEVETTO BANK FOR AFRICA
                1. Register
                2. Transaction
                3. Quit""")
        self.userInput = input("Enter your option to continue>>>")
        if self.userInput == "1":
            self.register()
        elif self.userInput == "2":
            self.transaction()
        elif self.userInput == "3":
            self.quit()
        else:
            print("invalid input")
            self.option()
    
    def register(self):
        detail = ["fName", "lName", "sex", "address", "acct_type", "phone-number", "acct_pin"]
        request = ["First_Name", "Last_Name", "Sex", "Address","Account_Type", "Phone_Number", "Pin_Number"]
        for i in range(7):
            detail[i] = input("Enter your"+request[i]+">>>")
        acct_no = "11"+str(random.randint(00000000, 90000000))
        acct_bal = 0000
        myquery = """INSERT INTO customersreg_info (First_Name, Last_Name, Sex, Address,Account_Type, Phone_Number,
                    Account_No, Pin_Number, Account_Balance)VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], acct_no, detail[6], acct_bal)
        self.mycursor.execute(myquery, val)
        self.mycon.commit()
        print(self.mycursor.rowcount, """registration is successful
                Your account number is """ +acct_no + ' and Your balance is ' + str(acct_bal))
        self.option()

    def transaction(self):
        transact = ["1. withdraw", "2. Deposit", "3. Transfer", "4. Check Balance", "5. Cancel"]
       
        self.acct_no = input("Enter your account number>>>")
        self.acct_pin = input("Enter your account pin>>>")
        query = "SELECT* FROM customersreg_info WHERE Account_no=%s AND Pin_Number=%s"
        val = (self.acct_no, self.acct_pin)
        self.mycursor.execute(query, val)
        self.record = self.mycursor.fetchall() 
        if self.record: 
            print("You are welcome dear"+self.record[0][1]+" "+self.record[0][2])
            for val in transact:
                print(val)
            
            self.userInput = input("Enter an option to continue")
            if self.userInput == "1":
                self.withdraw()
            elif self.userInput == "2":
                self.deposit()
            elif self.userInput == "3":
                self.transfer()
            elif self.userInput == "4":
                self.checkBalance()
            elif self.userInput == "5":
                self.option()
            else:
                print("invalid input")
                self.option()
        else:
            print("Invalid account details. Please go and register first to continue")
            self.option()

    def withdraw(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000}
        for key, val in amount.items():
            print(key, val)
        self.userInput = input("Enter amount to withdraw>>>")
        # self.userInput = input("Enter your deposit amount>>>")
        query = "SELECT Account_Balance FROM customersreg_info WHERE Account_no=%s"
        account = (self.acct_no,)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone()
        print(self.balance)
        print(self.userInput)
        print(amount[self.userInput])
        if int(self.balance[0]) < amount[self.userInput]:
            print("Insufficient Fund")
            self.option()
        else:
            newBalance = int(self.balance[0]) - amount[self.userInput]
            query = "UPDATE customersreg_info SET Account_Balance= %s WHERE Account_no=%s"
            account = (newBalance, self.acct_no)
            self.mycursor.execute(query, account)
            self.mycon.commit()
            print("Please take your cash of" +str(amount[self.userInput]))


    def deposit(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000}
        for key, val in amount.items():
            print(key, val)
        self.userInput = input("Enter your deposit amount>>>")
        query = "SELECT Account_Balance FROM customersreg_info WHERE Account_no=%s"
        account = (self.acct_no,)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone() 
        newBalance = amount[self.userInput] + int(self.balance[0])
        query = "UPDATE customersreg_info SET Account_Balance= %s WHERE Account_no=%s"
        account = (newBalance, self.acct_no)
        self.mycursor.execute(query, account)
        self.mycon.commit()
        print(amount[self.userInput], "deposit is successful")
        self.option()

    
    def transfer(self):
        amount = {"1":1000, "2":2000, "3":5000, "4":10000, "5":20000, "6":50000}
        for key, val in amount.items():
            print(key, val)
        self.user_amount = input("Enter your transfer amount>>>")
        self.recipient = input("Enter your recipient account number>>>")
        
        query = "SELECT Account_Balance FROM customersreg_info WHERE Account_no=%s"
        accNo = (self.recipient,)
        self.mycursor.execute(query, accNo)
        # self.mycursor.execute(query2, (self.recipient,))
        recipient_balance = self.mycursor.fetchone() 
        print(recipient_balance)

        self.userAcc = input('Enter Your Account Number>>>')
        query2 = "SELECT Account_Balance FROM customersreg_info WHERE Account_no=%s"
        self.acct_no = (self.userAcc,)

        self.mycursor.execute(query2, self.acct_no)
        user_balance = self.mycursor.fetchone()
        print(user_balance)

        if recipient_balance and int(user_balance[0]) > amount[self.user_amount]:
            newBalance = int(recipient_balance[0]) + amount[self.user_amount]
            new_user_balance = int(user_balance[0]) - amount[self.user_amount]
            query = "UPDATE customersreg_info SET Account_Balance= %s WHERE Account_no=%s"
            myUpdate = (new_user_balance,  self.userAcc)
            self.mycursor.execute(query, myUpdate)
            self.mycon.commit
            # self.mycursor.execute(query, (new_user_balance, self.acct_no))
            query2 = "UPDATE customersreg_info SET Account_Balance= %s WHERE Account_no=%s"
            recipientUpdate = (newBalance, self.recipient)
            self.mycursor.execute(query2, recipientUpdate)
            self.mycon.commit
            #query = "SELECT First_Name, Last_Name FROM customersreg_info WHERE Account_no=%s"
            print(str(amount[self.user_amount]) +" transfered successfully to" + recipient_balance[0] +" "+ recipient_balance[0])
            self.option()

    def checkBalance(self):
        query = "SELECT Account_Balance FROM customersreg_info WHERE Account_no=%s"
        account = (self.acct_no,)
        self.mycursor.execute(query, account)
        self.balance = self.mycursor.fetchone() 
        print("Your balance is" +str(self.balance[0]))
        self.option()

    # def quit(self):
    #     self.mycon.close
    #     sys.exit()

atm = ATMClass()        






