import mysql.connector
mycon = mysql.connector.connect(host="localhost", user="root",password="",  database="atm_app")
mycursor = mycon.cursor()
# # mycursor.execute("CREATE DATABASE atm_app")


# mycursor = mycon.cursor()
# mycursor.execute("CREATE TABLE customersreg_info(id INT AUTO_INCREMENT PRIMARY KEY, First_Name VARCHAR(20), Last_Name VARCHAR(20), Sex VARCHAR(10), Address VARCHAR(50), Account_Type VARCHAR(15), Phone_Number VARCHAR(11), Account_No VARCHAR(15), Pin_Number VARCHAR(5), Account_Balance VARCHAR(50))")
 



from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import *
from math import *
from math import exp, expm1
import tkinter as tk
from PIL import Image, ImageTk
import random


class AtmGui:
    def __init__(self):
         
        self.container = Tk()
        self.container.geometry("700x550")
        # self.container.iconbitmap("ball.ico")
        self.container.title('Registration Form')
        self.main = Frame(self.container)
        self.main.pack()

       
        self.homeScreen()

        self.buttonFm = Frame(self.container)
        self.buttonFm.pack(side=BOTTOM)
        

        # Number buttons
        Button(self.buttonFm, text='1', width=5, command=lambda: self.getValues('1')).grid(row=0, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='2', width=5, command=lambda: self.getValues('2')).grid(row=0, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='3', width=5, command=lambda: self.getValues('3')).grid(row=0, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='cancel', width=8, bg='red', command=lambda: self.getValues('4')).grid(row=0, column=3, padx=5, pady=5)

        Button(self.buttonFm, text='4', width=5, command=lambda: self.getValues('5')).grid(row=1, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='5', width=5, command=lambda: self.getValues('6')).grid(row=1, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='6', width=5, command=lambda: self.getValues('7')).grid(row=1, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='correct', bg='yellow', width=8, command=lambda: self.getValues('8')).grid(row=1, column=3, padx=5, pady=5)

        Button(self.buttonFm, text='7', width=5, command=lambda: self.getValues('9')).grid(row=2, column=0, padx=5, pady=5)
        Button(self.buttonFm, text='8', width=5, command=lambda: self.getValues('7')).grid(row=2, column=1, padx=5, pady=5)
        Button(self.buttonFm, text='9', width=5, command=lambda: self.getValues('8')).grid(row=2, column=2, padx=5, pady=5)
        Button(self.buttonFm, text='', width=8, bg='grey', command=lambda: self.getValues('9')).grid(row=2, column=3, padx=5, pady=5)

        Button(self.buttonFm, text='.', width=5, command=lambda: self.getValues('9')).grid(row=3, column=0, padx=5, pady=10)
        Button(self.buttonFm, text='0', width=5, command=lambda: self.getValues('7')).grid(row=3, column=1, padx=5, pady=10)
        Button(self.buttonFm, text='00', width=5, command=lambda: self.getValues('8')).grid(row=3, column=2, padx=5, pady=10)
        Button(self.buttonFm, text='Enter', bg='green', width=8, command=lambda: self.getValues('9')).grid(row=3, column=3, padx=5, pady=10)
    
        self.container. mainloop()

    def homeScreen(self):
        self.main.destroy()
        self.main = Frame(self.container)
        self.main.pack()
        self.submain1 = Frame(self.main)
        self.submain1.grid(row=0, column=0, rowspan=10)
        
 #left side buttons in diff. frame

        # self.imgbtn = Image.open("image/Forward_64px.png")
        # self.imgbtn1 = ImageTk.PhotoImage(self.imgbtn)
    
        Label(self.submain1).pack(expand = YES, fill = BOTH, pady=27)
        Button(self.submain1, text='1', width=5, command=lambda: self.regist()).pack(expand = YES, fill = BOTH, pady=7, side =BOTTOM)
        Button(self.submain1, text='2', width=5, command=lambda: self.getValues( )).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)
        Button(self.submain1, text='3', width=5, command=lambda: self.transactionScreen()).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)
        Button(self.submain1, text='a', width=5, command=lambda: self.registrationScreen()).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)

        # the center frame
        self.submain2 = Frame(self.main)
        self.submain2.grid(row=0, column=1)
        self.submain2.configure(bg='blue')

        self.bankLabel=Label(self.submain2, text ='NEVETTO BANK FOR AFRICA\n WELCOME\n', fg='pink',font=('arial',15, 'bold'), background = 'blue', height=4 , padx=105, pady=25)
        self.bankLabel.pack(side =TOP, fill = BOTH )
         

        self.submain2b = Frame(self.submain2)
        self.submain2b.pack(side=LEFT)
        self.submain2b.configure(bg='blue')

        
        self.lb=Label(self.submain2b, text ='Register', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT)
        self.lb.grid(pady=8)
        Label(self.submain2b, text ='Transaction', fg='pink',font=('arial',12, 'bold'), background = 'blue').grid (pady=8)
        Label(self.submain2b, text ='Quit', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT ).grid(pady=8)
        Label(self.submain2b,background = 'blue').grid(pady=50)
         

        
        self.submain3 = Frame(self.main) 
        self.submain3.grid(row=0, column=2)
        
       
        # self.imgplay = Image.open("image/Circled Play.png")
        # self.imgstart = ImageTk.PhotoImage(self.imgplay)

        Label(self.submain3).pack(expand = YES, fill = BOTH, pady=27)
        Button(self.submain3, text='ghgj',  command=lambda: self.getValues('1')).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='dtfyh', command=lambda: self.getValues('2')).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='31223',  command=lambda: self.getValues('3')).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='bbbb',  command=lambda: self.getValues('3')).pack(expand = YES, fill = BOTH, pady=7)

        
        
    
    def registrationScreen(self): 
        self.main.destroy()
        self.main = Frame(self.container)
        self.main.pack()
        

        self.mycon = mysql.connector.connect(host="localhost", user="root",password="",  database="atm_app")
        self.mycursor = self.mycon.cursor()    
        
    
        self.submain1 = Frame(self.main)
        self.submain1.grid(row=0, column=0, rowspan=10)
         

    

        Label(self.submain1).pack(expand = YES, fill = BOTH, pady=25)
        Button(self.submain1, text='1', width=5, command=lambda: self.getValues('1')).pack(expand = YES, fill = BOTH, pady=7, side =BOTTOM)
        Button(self.submain1, text='2', width=5, command=lambda: self.home()).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)
        Button(self.submain1, text='3', width=5, command=lambda: self.getValues('3')).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)
        Button(self.submain1, text='a', width=5, command=lambda: self.getValues('3')).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)

        # the center frame
        self.submain2 = Frame(self.main)
        self.submain2.grid(row=0, column=1)
        self.submain2.configure(bg='blue')

        self.bankLabel=Label(self.submain2, text ='Please Fill The Form Below Correctly', fg='pink',font=('arial',10, 'bold'), background = 'blue', padx=125, pady=35)
        self.bankLabel.pack(side =TOP, fill = BOTH )

        self.submain2b = Frame(self.submain2)
        self.status = StringVar()
        self.acctStatus = StringVar()
        self.submain2b.pack()
        self.submain2b.configure(bg='blue')

        Label(self.submain2b, text ='First Name', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =0, column=0)
        self.fName =Entry(self.submain2b,  fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT)
        self.fName.grid(row=0, column=1,pady=2)

        Label(self.submain2b, text ='Last Name', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =1, column=0)
        self.lName =Entry(self.submain2b, text ='Enter Your Last Name', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT)
        self.lName.grid(row= 1, column=1,pady=2)

        Label(self.submain2b, text ='Gender', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =2, column=0)
        Radiobutton(self.submain2b, variable= self.status, text = 'Female', value= 'female', tristatevalue= 0, fg='pink',font=('arial',8, 'bold'), background = 'blue',justify=LEFT).grid(row= 2, column=1)
        Radiobutton(self.submain2b, variable= self.status, text = 'Male', value= 'male', tristatevalue= 0, fg='pink',font=('arial',8, 'bold'), background = 'blue',justify=LEFT).grid(row= 2, column=2)

        Label(self.submain2b, text ='Address', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =3, column=0, pady=2)
        self.address =Entry(self.submain2b, fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT)
        self.address.grid(pady=5, row= 3, column=1)

        
        Label(self.submain2b, text ='Account Type', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =6, column=0, pady=2)
        Radiobutton(self.submain2b, variable= self.acctStatus, text = 'Savings', value= 'Savings', tristatevalue= 0, fg='pink',font=('arial',8, 'bold'), background = 'blue',justify=LEFT).grid(row= 6, column=1, pady=2)
        Radiobutton(self.submain2b, variable= self.acctStatus, text = 'Current', value= 'Current', tristatevalue= 0, fg='pink',font=('arial',8, 'bold'), background = 'blue',justify=LEFT).grid(row= 6, column=2, pady=2)
        Radiobutton(self.submain2b, variable= self.acctStatus, text = 'Domicilliary', value= 'Domicilliary', tristatevalue= 0, fg='pink',font=('arial',8, 'bold'), background = 'blue',justify=LEFT).grid(row= 6, column=3, pady=2,  padx=10)

        Label(self.submain2b, text ='Phone Number', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =7, column=0, pady=2)
        self.phoneNo =Entry(self.submain2b, fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT, width=10)
        self.phoneNo.grid(pady=8,row= 7, column=1)

        Label(self.submain2b, text ='PinNumber', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =8, column=0, pady=2)
        self.pinNo =Entry(self.submain2b, show='*',fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT, width=10, insertwidth=4,)
        self.pinNo.grid(pady=5, row= 8, column=1 )
        Label(self.submain2b, text ='Back>>>', fg='pink',font=('arial',12, 'bold'), background = 'blue').grid (row =8, column=3, pady=8)

        self.accBalStatus = StringVar()
        Label(self.submain2b, text ='Enter Initial Amount', fg='pink',font=('arial',8, 'bold'), background = 'blue').grid (row =9, column=0, pady=2)
        self.accBal =Entry(self.submain2b, fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT, width=10)
        self.accBal.grid(pady=2,row= 9, column=1)
        Label(self.submain2b, text ='Submit>>>', fg='pink',font=('arial',12, 'bold'), background = 'blue', justify=RIGHT).grid (row =9, column=3, pady=8)


        self.accFeedback = Frame(self.submain2) 
        self.accFeedback.pack()
        self.accNoStatus = StringVar()

        self.accNo =Label(self.accFeedback, textvariable = self.accNoStatus, fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT)
        self.accNo.grid()
        
        # Label(self.submain2b, text ='Transaction', fg='pink',font=('arial',12, 'bold'), background = 'blue').grid (pady=5)
        # Label(self.submain2b, text ='Quit', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT ).grid(pady=5)
        Label(self.accFeedback,background = 'blue').grid(pady=45)
         
        self.submain3 = Frame(self.main) 
        self.submain3.grid(row=0, column=2)
        
       
        # self.imgplay = Image.open("image/Circled Play.png")
        # self.imgstart = ImageTk.PhotoImage(self.imgplay)

        Label(self.submain3).pack(expand = YES, fill = BOTH, pady=25)
        Button(self.submain3, text='ghgj',  command=lambda: self.getValues('1')).pack(expand = YES, fill = BOTH,  pady=7)
        Button(self.submain3, text='<<', command=lambda: self.getValues('2')).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='<<',  command=lambda: self.homeScreen()).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='<<',  command=lambda: self.SubmitFunction()).pack(expand = YES, fill = BOTH, pady=7)



        self.buttonFm = Frame(self.container)
        self.buttonFm.pack( )
        
        
    # def register(self):
    #     detail = ["fName", "lName", "sex", "address", "acct_type", "phone-number", "acct_pin"]
    #     request = ["First_Name", "Last_Name", "Sex", "Address","Account_Type", "Phone_Number", "Pin_Number"]
    #     for i in range(7):
    #         detail[i] = input("Enter your"+request[i]+">>>")
    #     acct_no = "11"+str(random.randint(00000000, 90000000))
    #     acct_bal = 0000
    #     myquery = """INSERT INTO customersreg_info (First_Name, Last_Name, Sex, Address,Account_Type, Phone_Number,
    #                 Account_No, Pin_Number, Account_Balance)VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #     val = (detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], acct_no, detail[6], acct_bal)
    #     self.mycursor.execute(myquery, val)
    #     self.mycon.commit()
    #     print(self.mycursor.rowcount, """registration is successful
    #             Your account number is """ +acct_no + ' and Your balance is ' + str(acct_bal))
    #     self.option()

    def SubmitFunction(self):
        self.firstName = self.fName.get()
        self.lastName = self.lName.get()        
        self.sex = self.status.get()
        self.address = self.address.get()
        self.acct_type = self.acctStatus.get()
        self.phone_nunber = self.phoneNo.get()
        self.acct_pin = self.pinNo.get() 
        self.acc_bal = self.accBal.get()
        self.acc_no = "11"+str(random.randint(00000000, 90000000))
        
        myquery = """INSERT INTO customersreg_info (First_Name, Last_Name, Sex, Address,Account_Type, Phone_Number,
                    Account_No, Pin_Number, Account_Balance)VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (self.firstName, self.lastName, self.sex, self.address, self.acct_type, self.phone_nunber, self.acc_no, self.acct_pin, self.acc_bal)
        self.mycursor.execute(myquery, val)
        self.mycon.commit()
        print(self.firstName, self.lastName, self.sex, self.address, self.acct_type, self.phone_nunber, self.acc_no, self.acct_pin, self.acc_bal)
        #         Your account number is """ +acct_no + ' and Your balance is ' + str(acct_bal))

        self.accNoStatus.set('Dear customer your account number is ' + self.acc_no + '\n and your  current balance is ' + self.acc_bal )
         
    
    def transactionScreen(self):
        self.main.destroy()
        self.main = Frame(self.container)
        self.main.pack()
        self.submain1 = Frame(self.main)
        self.submain1.grid(row=0, column=0, rowspan=10)
        
 #left side buttons in diff. frame

        # self.imgbtn = Image.open("image/Forward_64px.png")
        # self.imgbtn1 = ImageTk.PhotoImage(self.imgbtn)
    
        Label(self.submain1).pack(expand = YES, fill = BOTH, pady=27)
        Button(self.submain1, text='>>', width=5, command=lambda: self.regist()).pack(expand = YES, fill = BOTH, pady=7, side =BOTTOM)
        Button(self.submain1, text='2', width=5, command=lambda: self.getValues( )).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)
        Button(self.submain1, text='3', width=5, command=lambda: self.getValues( )).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)
        Button(self.submain1, text='>>', width=5, command=lambda: self.registrationScreen()).pack(expand = YES, fill = BOTH , pady=7, side =BOTTOM)

        # the center frame
        self.submain2 = Frame(self.main)
        self.submain2.grid(row=0, column=1)
        self.submain2.configure(bg='blue')

        self.bankLabel=Label(self.submain2, text ='NEVETTO BANK FOR AFRICA\n WELCOME\n', fg='pink',font=('arial',15, 'bold'), background = 'blue', height=4 , padx=105, pady=10)
        self.bankLabel.pack(side =TOP, fill = BOTH )
         

        self.submain2b = Frame(self.submain2)
        self.submain2b.pack(side=LEFT)
        self.submain2b.configure(bg='blue')

        
        self.lb=Label(self.submain2b, text ='<<Withdraw', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT)
        self.lb.grid(pady=8)
        Label(self.submain2b, text ='<<Deposit', fg='pink',font=('arial',12, 'bold'), background = 'blue').grid (pady=8)
        Label(self.submain2b, text ='<<Transfer', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=LEFT ).grid(pady=8)

        self.submain2c = Frame(self.submain2)
        self.submain2c.pack(side=RIGHT)
        self.submain2c.configure(bg='blue')

        Label(self.submain2c, text ='', fg='pink',font=('arial',12, 'bold'), background = 'blue', justify=RIGHT).grid (pady=30)
        Label(self.submain2c, text ='Check Balance>>', fg='pink',font=('arial',12, 'bold'), background = 'blue', justify=RIGHT).grid (pady=8)
        Label(self.submain2c, text ='Quit>>', fg='pink',font=('arial',12, 'bold'), background = 'blue',justify=RIGHT ).grid(pady=8)

        Label(self.submain2c,background = 'blue').grid(pady=100)
         

        
        self.submain3 = Frame(self.main) 
        self.submain3.grid(row=0, column=2)
        
       
        # self.imgplay = Image.open("image/Circled Play.png")
        # self.imgstart = ImageTk.PhotoImage(self.imgplay)

        Label(self.submain3).pack(expand = YES, fill = BOTH, pady=27)
        Button(self.submain3, text='ghgj',  command=lambda: self.getValues('1')).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='<<', command=lambda: self.homeScreen()).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='31223',  command=lambda: self.getValues('3')).pack(expand = YES, fill = BOTH, pady=7)
        Button(self.submain3, text='bbbb',  command=lambda: self.getValues('3')).pack(expand = YES, fill = BOTH, pady=7)


at = AtmGui()