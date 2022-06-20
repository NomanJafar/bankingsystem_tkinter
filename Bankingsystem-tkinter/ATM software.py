from  tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from random import randint
import tkinter.font as font
new=Tk()
new.iconbitmap('calculator.ico')
new.title("ATM")
new.geometry("1024x500")
new.configure(bg="pink")
myFont = font.Font(size=30)



# exxisting user , new user
def new_user():
    top=Toplevel()
    top.configure(bg="lightblue")
    # global first_name
    new_info=Label(top,text="Please enter your information to register yourself.",padx=10,pady=10,bg="lightblue").grid()

    # first name
    first_name=Label(top,text="Enter your first name",pady=10,bg="lightblue").grid()
    e1 = Entry(top, width=35, borderwidth=5)
    e1.grid()
# last name
    last_name=Label(top,text="Enter your Last name",pady=10,bg="lightblue").grid()
    e2 = Entry(top, width=35, borderwidth=5)
    e2.grid()
    # id card number
    id_card=Label(top,text="Enter your CNIC",pady=10,bg="lightblue").grid()
    e3 = Entry(top, width=35, borderwidth=5)
    e3.grid()
# address
    address=Label(top,text="Enter your permanent address",pady=10,bg="lightblue").grid()
    e4 = Entry(top, width=35, borderwidth=5)
    e4.grid()
    # phone number
    phone_number=Label(top,text="Enter your Phone Number\n(Remember:This number will be used for further verifications of your account)",pady=10,bg="lightblue").grid()
    
    e5 = Entry(top, width=35, borderwidth=5)
    e5.grid()
# profession
    profession=Label(top,text="Enter your profession",pady=10,bg="lightblue").grid()
    e6 = Entry(top, width=35, borderwidth=5)
    e6.grid()
    
   
    # save inforamtion
    def save():
        
        top=Toplevel()
        top.configure(bg="purple")
        # issue account number and password
        account_num=str(randint(1000000000,9999999999))
        pass_word=str(randint(1000,9999))

        issue_account=Label(top,text="your new account has been issued on basis of your information",bg="purple",fg="white").grid(padx=10,pady=10)
        new_account_number=Label(top,text="your new account number is  "+account_num,bg="purple", font = ('Comic Sans MS',10),fg="white").grid(padx=10,pady=10)
        password=Label(top,text="your default password is "+pass_word, font = ('Comic Sans MS',10),bg="purple",fg="white").grid(padx=10,pady=10)
        # save data to file
        global text
        text = "\n" + account_num+ "\t" +pass_word + "\t" + e1.get() + "\t" + e2.get() + "\t" +  e3.get() + "\t" + e4.get() + "\t" + e5.get() + "\t" +  e6.get() + "\t"  
        f=open("persons.txt", "a")
        f.write(text)
        f.close()



        def sent():
            Label(top,text="message sent").grid()
            send_info= Button(top,text="Send me Account Number and password on my phone",state=DISABLED,bg="black",fg="white",command=sent)
        send_info= Button(top,text="Send me Account Number and password on my phone",bg="black",fg="white",command=sent).grid(padx=10,pady=10)
        # yes=Button(top,text="YES",bg="black",fg="white").grid(padx=10,pady=10)
        # no=Button(top,text="NO",bg="black",fg="white").grid(padx=10,pady=10)   
    # save button to save information
    summit=Button(top,text="Save Information",pady=10,bg="black",fg="white",command=save).grid(pady=10)
# existing account
def existing_user():
    top1=Toplevel() 
    top1.configure(bg="skyblue")
    account_number=Label(top1,text="Enter your account number",bg="skyblue",padx=20,pady=20).grid()
    e1 = Entry(top1, width=35, borderwidth=5)
    e1.grid()
    password=Label(top1,text="Enter your password",bg="skyblue",padx=20,pady=20).grid()
    e2 = Entry(top1, width=35, borderwidth=5)
    e2.grid()
    # for further procedding press continue
    def operations():
        
        f=open('text.txt')
        rad=f.read().strip().split()

        # checking if password and account number is right
        
        if e1.get() in rad and e2.get() in rad : #string in present in the text file
            top=Toplevel()    
            top.configure(bg="skyblue")
        # serevices porvide by atm
            top.geometry("1024x500")
            cash_withdrawl=Button(top,text="Withdraw cash", font = ('Comic Sans MS',15),bg=10,padx=20,pady=10).grid(row=0,column=0,padx=100,pady=40)
            transfer_money=Button(top,text="Transfer money", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=1,column=0,padx=20,pady=40)
            pay_utilities=Button(top,text="Pay utilities", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=2,column=0,padx=20,pady=40)
            pay_incometax=Button(top,text="Pay income tax", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=3,column=0,padx=20,pady=40)
            empty=Label(top,text="                                                                                                                                                    ",bg="skyblue").grid(row=1,column=3)
            recharge_mobile=Button(top,text="Recharge your mobile", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=0,column=5,padx=20,pady=40)
            apply_loan=Button(top,text="Apply for Loan", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=1,column=5,padx=20,pady=40)
            balance_inquire=Button(top,text="Balance Inquire", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=2,column=5,padx=20,pady=40)
            others=Button(top,text="Others", font = ('Comic Sans MS',15),padx=20,pady=10).grid(row=3,column=5,padx=20,pady=40)
            
        else:
            wrong_password=Label(top1,text="account number or password may wrong", font = ('Comic Sans MS',10)).grid()
# continue button
    continu=Button(top1,text="Continue",padx=10,pady=10,bg="black",fg="white",command=operations).grid(padx=10,pady=10)
# for new customer
new_label=Label(new,text="If you are a new user. please register yourself first by clicking below", font = ('Comic Sans MS',15),padx=40,pady=20).grid(padx=370,pady=10)
new_input=Button(new,text="new user", font = ('Comic Sans MS',15),command=new_user,bg="black",fg="white")
new_input.grid()
# for existing customer
existing_label=Label(new,text="If you are a existing user. please click below to continue", font = ('Comic Sans MS',15),padx=40,pady=20).grid(padx=370,pady=10)
existing_input=Button(new,text="existing user", font = ('Comic Sans MS',15),command=existing_user,bg="black",fg="white")
existing_input.grid()











mainloop()