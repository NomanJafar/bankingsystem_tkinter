import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import fileinput
from tkinter import filedialog
from random import randint
import tkinter.font as font

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,FourPage,FivePage,deposite,Current_balance):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
    
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="pink")
        label = tk.Label(self, text="Welcome to XYZ Banking Service", font=('Comic Sans MS',15,"bold"))
        label.grid(row=0,column=1,pady=10,padx=10)
        tk.Label(self,text="                                                                                                                                                         ",bg="pink").grid(row=0,column=0)
                

        button = tk.Button(self, text="New User",font=("Helvetica", 15, "bold italic"),
                            command=lambda: controller.show_frame(PageOne))
        button.grid(row=2,column=1,pady=10,padx=10)

        button2 = tk.Button(self, text="Existing User",font=("Helvetica", 15, "bold italic"),
                            command=lambda: controller.show_frame(FourPage))
        button2.grid(row=3,column=1,pady=10,padx=10)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="lightblue")
        label = tk.Label(self, text="                                        ",bg="lightblue", font=LARGE_FONT)
        label.grid(row=0,column=2,pady=10,padx=10)

        new_info=tk.Label(self,text="Please enter your information to register yourself.",font=(' MS Sans Serif',15,),padx=10,pady=10,bg="lightblue").grid(row=1,column=3,pady=3,padx=3)

        # first name
        first_name=tk.Label(self,text="Enter your first name",font=("Times", 13),pady=10,bg="lightblue").grid(row=2,column=3,pady=3,padx=3)
        global e1
        e1 = tk.Entry(self, width=35, borderwidth=5)
        e1.grid(row=3,column=3,pady=3,padx=3)
    # last name
        last_name=tk.Label(self,text="Enter your Last name",font=("Times", 13),pady=10,bg="lightblue").grid(row=4,column=3,pady=3,padx=3)
        global e2
        e2 = tk.Entry(self, width=35, borderwidth=5)
        e2.grid(row=5,column=3,pady=3,padx=3)
        # id card number
        id_card=tk.Label(self,text="Enter your CNIC",font=("Times", 13),pady=10,bg="lightblue").grid(row=6,column=3,pady=3,padx=3)
        global e3
        e3 = tk.Entry(self, width=35, borderwidth=5)
        e3.insert( 'end','00000-0000000-0')
        e3.grid(row=7,column=3,pady=3,padx=3)
    # address
        address=tk.Label(self,text="Enter your permanent address",font=("Times", 13),pady=10,bg="lightblue").grid(row=8,column=3,pady=3,padx=3)
        global e4
        e4 = tk.Entry(self, width=35, borderwidth=5)
        e4.grid(row=9,column=3,pady=3,padx=3)
        # phone number
        phone_number=tk.Label(self,text="Enter your Phone Number\n(Remember:This number will be used for further verifications of your account)",font=("Times", 13),pady=10,bg="lightblue").grid(row=10,column=3,pady=3,padx=3)
        global e5
        e5 = tk.Entry(self, width=35, borderwidth=5)
        e5.insert( 'end','+92')
        e5.grid(row=11,column=3,pady=3,padx=3)
    # profession
        profession=tk.Label(self,text="Enter your profession",font=("Times", 13),pady=10,bg="lightblue").grid(row=12,column=3,pady=3,padx=3)
        global e6
        e6 = tk.Entry(self, width=35, borderwidth=5)
        e6.grid(row=13,column=3,pady=3,padx=3)

        def clear():
            e1.delete(0,'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e3.insert( 'end','00000-0000000-0')
            e4.delete(0, 'end')
            e5.delete(0, 'end')
            e5.insert( 'end','+92')
            e6.delete(0, 'end')
            controller.show_frame(StartPage)

        button1 = tk.Button(self, text="Back to Home",bg="black",fg="white",font=("Helvetica", 15, "bold italic"),
                            command=clear)
        button1.grid(row=0,column=0,pady=3,padx=3)

        
        summit=tk.Button(self,text="Save Information",pady=10,bg="black",fg="white",font=("Helvetica", 15, "bold italic"),command=lambda: controller.show_frame(PageTwo)).grid(row=14,column=3,pady=3,padx=3)
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="purple")
        label = tk.Label(self, text="                                          ",bg="purple", font=LARGE_FONT)
        label.grid(row=0,column=1,padx=10,pady=10)

        
        account_num=str(randint(1000000000,9999999999))
        pass_word=str(randint(1000,9999))
        zero="0"
        tk.Label(self,text="                                              ",bg="purple").grid(row=0,column=2,padx=10,pady=10)
        issue_account=tk.Label(self,text="Your information has been saved successfully",font=("Helvetica", 15, "bold italic"),bg="purple",fg="white").grid(row=1,column=3,padx=10,pady=10)
        new_account_number=tk.Label(self,text="your new account number is  "+account_num,bg="purple", font = ('Comic Sans MS',15),fg="white").grid(row=2,column=3,padx=10,pady=10)
        password=tk.Label(self,text="your default password is "+pass_word, font = ('Comic Sans MS',15),bg="purple",fg="white").grid(row=3,column=3,padx=10,pady=10)

        def save():
            # open("text.txt","w+").close()
            global info
            info = "\n"+ account_num+ "\t" +pass_word + "\t" + e1.get() + "\t" + e2.get() + "\t" +  e3.get() + "\t" + e4.get() + "\t" + e5.get() + "\t" +  e6.get() + "\t"
            with open("text.txt", "a") as f:
                f.write(info)

            global pasay
            pasay=account_num+"   "+zero + "\n"
            with open("amount.txt", "a") as f:
                f.write(pasay)
                f.close()


            tk.Label(self,text="Account Number Registered",bg="purple",fg="white").grid(row=5,column=3,padx=10,pady=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        button1.grid(row=0,column=0,pady=3,padx=3)

        button2 = tk.Button(self, text="Register your Account Number",
                            command=save)
        button2.grid(row=4,column=3,padx=10,pady=10)
        
class FourPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="lightblue")
        label = tk.Label(self, text="                                                                           ",bg="lightblue", font=LARGE_FONT)
        label.grid(row=1,column=1,padx=10,pady=10)



        account_number=tk.Label(self,text="Enter your account number", font = ('Comic Sans MS',15),bg="lightblue",padx=20,pady=20).grid(row=3,column=3,padx=10,pady=10)
        global eA
        eA = tk.Entry(self, width=35, borderwidth=5)
        eA.grid(row=4,column=3,padx=10,pady=10)
        password=tk.Label(self,text="Enter your password",bg="lightblue" ,font = ('Comic Sans MS',15),padx=20,pady=20).grid(row=5,column=3,padx=10,pady=10)
        global eP
        eP = tk.Entry(self, width=35, borderwidth=5)
        eP.grid(row=6,column=3,padx=10,pady=10)
        
        def match():
            
            f=open('text.txt')
            rad=f.read().strip().split()


            if eA.get() in rad and eP.get() in rad :

                controller.show_frame(FivePage)
            else:
                tk.Label(self,text="Account number or Password may wrong" ,font = ('Comic Sans MS',15),bg="lightblue",padx=20,pady=20).grid(row=8,column=3,padx=10,pady=10)



        

        button = tk.Button(self, text="Login", font = ('Arial',15,"bold"),
                            command=match)
        button.grid(row=7,column=3,padx=10,pady=10)

        button2 = tk.Button(self, text="Home Page", font = ('Arial',15,"bold"),
                            command=lambda: controller.show_frame(StartPage))
        button2.grid(row=0,column=0,padx=10,pady=10)
class FivePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="purple")
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(pady=10,padx=10)


        
        
        cash_withdrawl=tk.Button(self,text="Withdraw cash", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=0,column=0,padx=100,pady=40)
        transfer_money=tk.Button(self,text="Transfer money", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=1,column=0,padx=20,pady=40)
        pay_utilities=tk.Button(self,text="Pay utilities", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=2,column=0,padx=20,pady=40)
        pay_incometax=tk.Button(self,text="Pay income tax", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=3,column=0,padx=20,pady=40)
        empty=tk.Label(self,text="                                                                                                                                                    ",bg="Purple").grid(row=1,column=3)
        recharge_mobile=tk.Button(self,text="Recharge your mobile", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=0,column=5,padx=20,pady=40)
        apply_loan=tk.Button(self,text="Apply for Loan", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=1,column=5,padx=20,pady=40)
        balance_inquire=tk.Button(self,text="Balance Inquire", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=2,column=5,padx=20,pady=40)
        others=tk.Button(self,text="Others", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=3,column=5,padx=20,pady=40)    
        money_deposit=tk.Button(self,text="Deposite Money", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10,command=lambda: controller.show_frame(deposite)).grid(row=4,column=0,padx=100,pady=40)
        Personal_Information=tk.Button(self,text="Personal Information", font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10).grid(row=4,column=5,padx=100,pady=40)

        # to clear the login page 
        def clear():
            eA.delete(0,'end')
            eP.delete(0,'end')
            controller.show_frame(FourPage)

        button2 = tk.Button(self, text="Log Out",bg="skyblue",
                            command=clear)
        button2.grid(row=4,column=3,padx=20,pady=10)

class deposite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="purple")
        label = tk.Label(self, text="Enter the amount you want to deposite",font = ('Comic Sans MS',20),bg="purple",fg="white")
        label.grid(row=2,column=3,pady=10,padx=10)
        tk.Label(self,text="                                                                                                               \n                                                                                                      \n                                                                                           \n                                                                                 ",bg="purple").grid(row=1,column=2)
        edeposite = tk.Entry(self, width=50, borderwidth=5)
        edeposite.grid(row=3,column=3,padx=5,pady=5)



        def deposite_amount():
            if edeposite.get().isdigit():
                f=open('amount.txt','r')
                written=f.read().strip().split()
                global sum
                sum=int(written[1]) + int(edeposite.get())
                f.close()
    

                with open('amount.txt') as myFile:
                   
                    for num, line in enumerate(myFile,0):
                        if eA.get() in line:
                            
                    
                            num1 =num
                            tk.Label(self,text=line+"  line number"+str(num),bg="white",fg="black").grid(row=5,column=1)


                myFile.close()

                a_file = open("amount.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[num1] = eA.get()+"     "+str(sum)



                a_file = open("amount.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()







                myFile=open('amount.txt','w')
                myFile.writelines(list_of_lines)             
                myFile.close()
                
                tk.Label(self,text="Amount Deposited successfully",padx=30).grid(padx=15,row=4,column=3)
                
            else:
                notallowed=tk.Label(self,text="Only Integer entries allowed").grid(row=4,column=3)
                
                


        button = tk.Button(self, text="Deposite",font = ('Comic Sans MS',15),bg="skyblue",padx=10,pady=5,command=deposite_amount).grid(row=3,column=4,padx=10,pady=5)


        button1 = tk.Button(self, text="Back",font = ('Comic Sans MS',15),bg="skyblue",padx=10,pady=5,
                            command=lambda: controller.show_frame(FivePage))
        button1.grid(row=0,column=0,padx=10,pady=5)

        tk.Label(self,text="      \n        \n       \n               \n      \n   \n    \n       \n            \n         \n        \n     \n           \n        ",bg="purple").grid(row=5,column=4)

        button2 = tk.Button(self, text="Current Balance",font = ('Comic Sans MS',15),bg="skyblue",padx=20,pady=10,
                            command=lambda: controller.show_frame(Current_balance))
        button2.grid(row=6,column=4,padx=40,pady=20)

class Current_balance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="purple")
        tk.Label(self,text="                                                                                                               \n                                                                                                      \n                                                                                           \n                                                                                 ",bg="purple").grid(row=0,column=1)

        f=open('amount.txt')
        written=f.read().strip().split()

        label = tk.Label(self, text="Your current balance is "+str(written[0]),font = ('Comic Sans MS',15))
        f.close()
        label.grid(row=3,column=3,pady=10,padx=10)
        label1 = tk.Label(self, text="Your transaction limit is $1000 ",font = ('Comic Sans MS',15))
        label1.grid(row=4,column=3,pady=10,padx=10)
        button1 = tk.Button(self, text="Back",font=('',10),padx=15,
                        command=lambda: controller.show_frame(deposite))
        button1.grid(padx=15,row=0,column=0)

        




app = SeaofBTCapp()
app.mainloop()