from abc import ABC , abstractmethod
import tkinter
from tkinter import *
import matplotlib.pyplot as plt
from PIL import ImageTk, Image 
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime as dt
import math
import smtplib
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,  NavigationToolbar2Tk
import os
import mysql.connector as connector


#defining customer,admin and furniture classes

class User(ABC):
    def __init__(self , name , phonenumber , address , loginid , password):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber
        self.__loginid = loginid
        self.__password = password
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getPhoneNumber(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

class Customer(User):
    def __init__(self, name , phonenumber , address , loginid , password , amountdue , numberoforders):
        super().__init__(name , phonenumber , address , loginid , password)
        self.__amountdue = amountdue
        self.__numberoforders = numberoforders
        pass

    def getAddress(self):
        return self.address
    
    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phonenumber


class Admin(User):

    profit = 0
    investment = 0

    def __init__(self, name , phonenumber , address , loginid , password):
        super().__init__(name , phonenumber , address , loginid , password)
        pass

    def getAddress(self):
        return self.address
    
    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phonenumber

class Furniture:
    def __init__(self , id , name , company , price , feedback , description , type , rented , photo , interestrate , timeframe ,userid = 0):
        self.__id = id
        self.__name = name
        self.__company = company
        self.__price = price
        self.__feedback = feedback
        self.__description = description
        self.__type = type
        self.__rented = rented
        self.__photo = photo
        self.__interestrate = interestrate
        self.__timeframe = timeframe
        pass
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getCompany(self):
        return self.__company

    def getPrice(self):
        return self.__price

    def getFeedback(self):
        return self.__feedback

    def getDescription(self):
        return self.__description

    def getType(self):
        return self.__type

    def getUserId(self):
        return self.__id

    def isRented(self):
        return self.__rented

    def getPhoto(self):
        return self.__photo

    def getInterestRate(self):
        return self.__interestrate

    def getTimeFrame(self):
        return self.__timeframe

global user_id , pass_word , is_admin

# page opens up after login as a Customer
def CustomerPage(self) :
    self.destroy()
    customer = Tk()
    customer.geometry("1000x600")
    customer.title("CUSTOMER PAGE")
    leftBg = "cyan"
    rightBg = "violet"
    


    def buynowonloan():
        loan = Tk()
        loan.geometry("500x500")
        loan.title("BUY VIA LOAN")
        bgCol = "cyan"
        loan.config(bg=bgCol)
        l1 = Label(loan , text = "Enter the id of the furniture", bg=bgCol, font=("Italic", 12))
        l1.grid(row = 0 , column = 0, padx=10, pady=10)
        e1 = Entry(loan)
        e1.grid(row = 0 , column = 1)
        l2 = Label(loan , text = "Enter the days to loan", bg=bgCol, font=("Italic", 12))
        e2 = Entry(loan)
        l2.grid(row = 1, column = 0, padx=10, pady=10)
        e2.grid(row = 1 , column = 1)
        ex = "SELECT COUNT(username) FROM past_orders WHERE username = %s"
        va = (user_id , )
        my_cursor.execute(ex , va)
        count = my_cursor.fetchall()[0][0]
        l3 = Label(loan , text = "Your past orders : " + str(count), bg=bgCol, font=("Comic Sans MS", 13, "italic"))
        l3.grid(row = 2 , column = 0 , columnspan = 2, pady=10)
        

        def checkprice():
            fur_id = e1.get()
            num_days = e2.get()
            ex = "SELECT interest_rate FROM furnitures WHERE id = %s"
            va = (fur_id , )
            my_cursor.execute(ex , va)
            interest_rate = my_cursor.fetchall()
            new_interest = float(interest_rate[0][0])*(2**(-count))
            l4 = Label(loan , text = "Interest Rate on your experience with us : " + str(new_interest), bg = bgCol ,font=("Centaur", 10, "italic"))
            l4.grid(row = 3 , column = 0 , columnspan = 2, padx=10, pady=10)
            ex = "SELECT price FROM furnitures WHERE id = %s"
            va = (fur_id , )
            my_cursor.execute(ex , va)
            old_price = my_cursor.fetchall()
            
            global new_price
            new_price = float(old_price[0][0])*(1+new_interest*int(num_days)/100)
            l5 = Label(loan , text = "Total price on your experience with us : " + str(new_price), bg = bgCol ,font=("Centaur", 10, "italic"))
            l5.grid(row = 4 , column = 0 , columnspan = 2, padx=10, pady=10)
            pass

        def buynow():
            fur_id = e1.get()
            num_days = int(e2.get())
            ex = "UPDATE furnitures SET rented = %s , days_rented = days_rented + %s WHERE id = %s"
            va = (2 , num_days , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "INSERT INTO past_orders (username , furniture_id) VALUES (%s , %s)"
            va = (user_id , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "UPDATE customers SET amountdue = %s WHERE username = %s"
            messagebox.showinfo("Information", "Furniture Purchased !")
            va = (new_price , user_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            CustomerPage(customer)
            pass

        b1 = Button(loan , text = "Buy Now" , command = buynow, bg="maroon", font=("Arial", 13, "bold"), fg="white")
        b1.grid(row = 7 , column = 0, padx=10, pady=10, columnspan=2)
        b2 = Button(loan , text = "Check Price" , command = checkprice, bg="violet red", font=("Arial", 13, "bold"), fg="white")
        b2.grid(row = 6 , column = 0, padx=10, pady=10, columnspan=2)
        pass

    def buynowonrent():
        rent = Tk()
        rent.geometry("500x500")
        bgCol = "dark green"
        rent.config(bg=bgCol)
        rent.title("BUY ON RENT")
        l1 = Label(rent , text = "Enter the id of the furniture", bg=bgCol, font=("Italic", 12))
        l1.grid(row = 0 , column = 0, padx=10, pady=10)
        e1 = Entry(rent)
        e1.grid(row = 0 , column = 1)
        l2 = Label(rent , text = "Enter the days to rent ", bg=bgCol, font=("Italic", 12))
        e2 = Entry(rent)
        l2.grid(row = 1, column = 0 , padx=10, pady=10)
        e2.grid(row = 1 , column = 1)

        def checkprice():
            fur_id = e1.get()
            num_days = e2.get()
            ex = "SELECT price FROM furnitures WHERE id = %s"
            va = (fur_id , )
            my_cursor.execute(ex , va)
            old_price = my_cursor.fetchall()
            global ne_price
            ne_price = old_price[0][0]*math.ceil(int(num_days)/10)
            l5 = Label(rent , text = "Total price on your experience with us : " + str(ne_price),bg = bgCol, font=("Centaur", 10, "italic"))
            l5.grid(row = 4 , column = 0 , columnspan = 2)
            pass

        def buynow():
            fur_id = e1.get()
            num_days = int(e2.get())
            ex = "UPDATE furnitures SET rented = %s , days_rented = days_rented + %s WHERE id = %s"
            va = (1 , num_days , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "INSERT INTO past_orders (username , furniture_id) VALUES (%s , %s)"
            va = (user_id , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "SELECT profit FROM admins LIMIT 1"
            my_cursor.execute(ex)
            res = my_cursor.fetchall()
            ex = "SELECT username FROM admins LIMIT 1"
            my_cursor.execute(ex)
            re = my_cursor.fetchall()
            ex ="UPDATE admins SET profit = %s WHERE username = %s"
            va = (ne_price + res[0][0] , re[0][0])
            my_cursor.execute(ex , va)
            mydb.commit()
            exe = "SELECT profit FROM graph WHERE id = (SELECT max(id) FROM graph)"
            my_cursor.execute(exe)
            oldprofit = my_cursor.fetchall()
            exe = "SELECT investment FROM graph WHERE id = (SELECT max(id) FROM graph)"
            my_cursor.execute(exe)
            oldinvestment = my_cursor.fetchall()
            exe = "INSERT INTO graph (profit , investment) VALUES (%s , %s)"
            va = (float(oldprofit[0][0])+float(ne_price), float(oldinvestment[0][0]))
            my_cursor.execute(exe , va)
            mydb.commit()
            messagebox.showinfo("Information", "Furniture Purchased !")
            CustomerPage(customer)
            pass

        b2 = Button(rent , text = "Check Price" , command = checkprice, font=("Arial", 13, "bold"), fg="white", bg="#002366")
        b2.grid(row = 5 , column = 0, padx=10, pady=10, columnspan=2)

        b1 = Button(rent , text = "Buy Now" , command = buynow, font=("Arial", 13, "bold"), fg="white", bg="#991229")
        b1.grid(row = 6 , column = 0, padx=10, pady=10, columnspan=2)
        pass

    def returnitem():
        item = Tk()
        item.geometry("500x500")
        item.title("RETURN ITEM")
        bgCol = "cyan"
        item.config(bg=bgCol)
        l6 = Label(item , text = "Enter the id of the furniture : ", bg=bgCol, font=("Times new roman", 14))
        l6.grid(row = 0 , column = 0, padx=10, pady=10)
        e6 = Entry(item, relief=FLAT)
        e6.grid(row = 0 , column = 1)

        def addreturn():
            temp = e6.get()
            if temp:
                ex = "INSERT INTO current_returns (username , furniture_id) VALUES (%s , %s)"
                va = (user_id , int(e6.get()))
                my_cursor.execute(ex , va)
                mydb.commit()
                messagebox.showinfo("Information", "Return Process Initiated, you will be notified soon !")
               # testreturnadded(e6.get())
            else:
                messagebox.showwarning("Warning", "Enter the ID !")
            pass

        b6 = Button(item , text = "Add to return" , command = addreturn, bg="lime green", font=("Arial", 12, "bold"), fg="white")
        b6.grid(row = 1 , column = 1, padx=10, pady=10)
        pass

    def checkamountdue():
        amount = Tk()
        amount.geometry("500x500")
        amount.title("DETAILS OF THE AMOUNT")
        cbg="red"
        amount.config(bg=cbg)
        ex = "SELECT amountdue FROM customers WHERE username = %s"
        va = (user_id , )
        my_cursor.execute(ex , va)
        res = my_cursor.fetchall()[0][0]
        l1 = Label(amount , text = "Your amount due : " + str(res), bg=cbg, font=("Comic sans ms", 13))
        l1.grid(row=0, column=0,padx=10, pady=10, columnspan=2)
       
        l2 = Label(amount , text = "Enter amount to be paid", bg=cbg, font=("Comic sans ms", 13))
        l2.grid(row=1, column=0, padx=10, pady=10)
        e2 = Entry(amount, relief=FLAT)
        e2.grid(row=1, column=1)

        def paynow():
            
            money = (e2.get())
            if money:
                money = float(money)
                ex = "SELECT profit FROM admins LIMIT 1"
                my_cursor.execute(ex)
                r = my_cursor.fetchall()
                new_profit = r[0][0] + money
                ex = "SELECT username FROM admins LIMIT 1"
                my_cursor.execute(ex)
                re = my_cursor.fetchall()
                ex ="UPDATE admins SET profit = %s WHERE username = %s"
                va = (new_profit , re[0][0])
                my_cursor.execute(ex , va)
                mydb.commit()
                ex = "UPDATE customers SET amountdue = %s WHERE username = %s"
                va = (max(res-money , 0) , user_id)
                my_cursor.execute(ex , va)
                mydb.commit()
               
                messagebox.showinfo( "Amount Paid !")
                exe = "SELECT profit FROM graph WHERE id = (SELECT max(id) FROM graph)"
                my_cursor.execute(exe)
                oldprofit = my_cursor.fetchall()
                exe = "SELECT investment FROM graph WHERE id = (SELECT max(id) FROM graph)"
                my_cursor.execute(exe)
                oldinvestment = my_cursor.fetchall()
                exe = "INSERT INTO graph (profit , investment) VALUES (%s , %s)"
                va = (float(oldprofit[0][0])+float(money), float(oldinvestment[0][0]))
                my_cursor.execute(exe , va)
                mydb.commit()
            else:
                messagebox.showwarning("Warning", "No money added !")
            pass

        b1 = Button(amount , text = "Pay amount due !" , command = paynow, bg="#60e84e", font=("Arial", 13, "bold"))
        b1.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        pass

    def pastorder():
        past = Tk()
        past.geometry("500x500")
        past.title("PREVIOUS ORDER HISTORY")
        ex = "SELECT * FROM past_orders WHERE username = %s"
        va = (user_id , )
        my_cursor.execute(ex , va)
        res = my_cursor.fetchall()
        text_scroll = Scrollbar(past)
        text_scroll.pack(side = RIGHT , fill = Y)
        my_text = Text(past , width = 100 , height = 120 , font = ('Comic sans ms' , 10) , yscrollcommand = text_scroll.set, spacing1=8)
        my_text.pack(pady = 10 , padx = 10)
        text_scroll.config(command = my_text.yview)
        for furniture in res:
            my_text.insert(END , "          Furniture id = " + str(furniture[2]) + "\n")
        pass

    def giveFeedback():
        give = Tk()
        give.geometry("800x500")
        give.title("GIVE FEEDBACK")
        gbg = "yellow"
        give.config(bg = gbg)
        lab2 = Label(give , text = "Enter the name of the furniture", bg=gbg, font=("Courier New", 12, "bold"))
        lab2.grid(row = 0 ,column = 0, padx=10, pady=10)
        ent2 = Entry(give, relief=FLAT, width=70)
        ent2.grid(row = 0 , column = 1)
        lab1 = Label(give , text = "Give Feedback", bg=gbg, font=("Courier New", 12, "bold"))
        lab1.grid(row = 1,column = 0, padx=10, pady=10)
        ent1 = Entry(give, relief=FLAT, width=70)
        ent1.grid(row = 1 , column = 1)
        
        def submitFeedback():
            typ = ent2.get()
            feed = ent1.get()
            if typ and feed:
                ex = "INSERT INTO feedbacks (type , review) VALUES (%s , %s)"
                va = (typ , feed)
                my_cursor.execute(ex , va)
                mydb.commit()
                #testfeedbackinsert(typ, feed)
                messagebox.showinfo("Information", "Feedback Submitted !")
            else:
                messagebox.showwarning("Warning", "All fields must be filled !")
            
            pass

        but1 = Button(give , text = "Submit feedback" , command = submitFeedback, bg="midnight blue", font=("Arial", 13, "bold"))
        but1.grid(row = 2 , column = 0 , columnspan = 2, padx=10, pady=10)

        pass

    def searchFurniture():
        search = Tk()
        search.geometry("800x500")
        search.title("SEARCH FOR THE FURNITURE")
        lbg = "purple"
        rbg = "snow2"
        frame1 = Frame(search , background = lbg)
        frame1.grid(row = 0 , column = 0 , sticky = "nsew")
        frame2 = Frame(search , background = rbg)
        frame2.grid(row = 0 , column = 1 , sticky = "nsew")
        search.grid_columnconfigure(0 , weight = 2)
        search.grid_columnconfigure(1 , weight = 3)
        search.grid_rowconfigure(0 , weight = 1)
        frame1.grid_propagate(False)
        frame2.grid_propagate(False)
        frame1.pack_propagate(False)
        frame2.pack_propagate(False)
        la1 = Label(frame1 , text = "Enter the name :", font=("Times new roman", 14), bg=lbg)
        la1.grid(row = 0 , column = 0, padx=10, pady=10)
        ent1 = Entry(frame1, relief=FLAT, font=("Comic sans ms", 9))
        ent1.grid(row = 0 , column = 1)
        text_scroll2 = Scrollbar(frame2)
        text_scroll2.pack(side = RIGHT , fill = Y)
        my_text2 = Text(frame2 , width = 100 , height = 120 , font = ('Comic sans ms' , 10) , yscrollcommand = text_scroll2.set, spacing1=8)
        my_text2.pack(pady = 10 , padx = 10)
        text_scroll2.config(command = my_text2.yview)
        global my_imag
        global imag
        imag = []
        def searchNow():
            my_text2.delete("1.0" , END)
            typ = ent1.get()
            exe = "SELECT * FROM furnitures WHERE rented = 0"
            my_cursor.execute(exe)
            relu = my_cursor.fetchall()
            for furniture in relu:
                if typ in furniture[5]:
                   
                    my_text2.insert(END , '\n')
                    
                    my_text2.insert(END , "         Id : " + str(furniture[0]) + '\n')
                    my_text2.insert(END , "         Name : " + furniture[5] + '\n')
                    my_text2.insert(END , "         Company : " + furniture[2] + '\n')
                    my_text2.insert(END , "         Price : " + str(furniture[3]) + '\n')
                    my_text2.insert(END , "         Description : " + furniture[4] + '\n')
                    my_text2.insert(END , "         Interest Rate : " + str(furniture[8]) + '\n')
                    ex = "SELECT review FROM feedbacks WHERE type = %s"
                    va = (furniture[5],)
                    my_cursor.execute(ex , va)
                    rel = my_cursor.fetchall()
                    my_text2.insert(END , "         Reviews :\n")
                    for feedback in rel:
                        my_text2.insert(END , "         "+ feedback[0] + "\n")
                        pass
                    my_text2.insert(END , "\n\n")
            pass
        

        bu1 = Button(frame1 , text = "Search Now" , command = searchNow, bg="navy", fg="green yellow", font=("Centaur", 14, "bold"))
        bu1.grid(row = 1 , column = 0 , columnspan = 2, padx=10, pady=10)
        pass

    def logOut():
        Login(customer)
        pass
    
    BtnBg = "tomato"
    searchbutton = Button(customer , text = "Search furniture" , width = 30,command = searchFurniture, bg=BtnBg, font=("Tahoma", 15))
    searchbutton.pack(padx=10, pady=10)
    buy_now_on_loan = Button(customer , text = "Buy Now On Loan" , width = 30 , command = buynowonloan, bg=BtnBg, font=("Tahoma", 15))
    buy_now_on_loan.pack(padx=10, pady=(10))
    buy_now_on_rent = Button(customer , text = "Buy Now On Rent" , width = 30 , command = buynowonrent, bg=BtnBg, font=("Tahoma", 15))
    buy_now_on_rent.pack(padx=10, pady=10)
    amountdue = Button(customer , text = "Amount Due" , width = 30 , command = checkamountdue, bg=BtnBg, font=("Tahoma", 15))
    amountdue.pack(padx=10, pady=10)
    returnbutton = Button(customer , text = "Return" , width = 30 , command = returnitem, bg=BtnBg, font=("Tahoma", 15))
    returnbutton.pack(padx=10, pady=10)
    Pastorder = Button(customer , text = "Past Order History" , width = 30 , command = pastorder, bg=BtnBg, font=("Tahoma", 15))
    Pastorder.pack(padx=10, pady=10)
    feedback = Button(customer , text = "Give Feedback" , command = giveFeedback, bg=BtnBg, font=("Tahoma", 15), width=30)
    feedback.pack(padx=10, pady=10)
    
    logout = Button(customer , text = "Log Out" , width = 30 , command = logOut, bg=BtnBg, font=("Tahoma", 15))
    logout.pack(padx=10, pady=10)


 
# page opens up after login as a admin


def AdminPage(self):
    self.destroy()
    admin = Tk()
    admin.geometry("900x550")
    admin.title("ADMIN PAGE")
    leftBg = "khaki"
    rightBg = "gold"
    


    # The rental price of each item is decreased by 10% after its use by a customer for each year.
    


    exe = "SELECT id FROM furnitures WHERE days_rented >= %s"
    va = (365,)
    my_cursor.execute(exe, va)
    res = my_cursor.fetchall()

    if(len(res) > 0):
        for id in res[0]:
            ex = "UPDATE furnitures SET days_rented = days_rented - %s , price = price * %s WHERE id = %s"
            va = (365, 0.9, id)
            my_cursor.execute(ex, va)


    mydb.commit()


# The admin creates a customer account from the signup portal

    def createCustomer():
        Signup()
        pass


# For deleting a customer we first check if the entered username exists or not and then we check if the customer has any amount due
# if no amout due then we delete the customer from the database

    def deleteCustomer():
        cusdelete = Tk()
        cusdelete.geometry("650x200")
        cusdelete.title("DELETE THE CUSTOMER ACCOUNT")
        cusdelete.config(bg="indian red")
        Label(cusdelete , text = "Enter Username of the Customer : ", bg="lime green", font=("Georgia", 15)).grid(row = 0 , column = 1, padx=10, pady=10)
        entry = Entry(cusdelete, relief=FLAT)
        entry.grid(row = 0 , column = 2)

        def confirmDelete():
            user = entry.get()
            exe = "SELECT * FROM customers WHERE username = %s"
            val = (user , )
            my_cursor.execute(exe , val)
            res = my_cursor.fetchall()
            if len(res) == 0:
                messagebox.showwarning("ALERT !" , "NO such user found !")
            elif res[0][5] != 0:
                messagebox.showwarning("Warning","User Cannot be Deleted !")
               
            else:
                exe = "DELETE FROM customers WHERE username = %s"
                my_cursor.execute(exe , val)
                mydb.commit()
                messagebox.showinfo("ALERT !" , "USER DELETED !")
              
            pass

        b = Button(cusdelete , text = "Delete !" , command = confirmDelete, bg="navy", fg="bisque", font=("Arial", 13, "bold"))
        b.grid(row = 1 , column = 0 , columnspan = 2)
        pass

# If the number of any item present in the inventory falls below 6 items then a message is sent to the admin for its need

    def seeNotifications():
        seenoti=Tk()
        seenoti.geometry("500x500")
        seenoti.title("NOTIFICATIONS")
        text_scroll = Scrollbar(seenoti)
        text_scroll.pack(side = RIGHT , fill = Y)
        my_text = Text(seenoti , width = 100 , height = 120 , font = ('Comic sans ms' , 10) , yscrollcommand = text_scroll.set, spacing1=8)
        my_text.pack(pady = 10 , padx = 10)
        text_scroll.config(command = my_text.yview)
        exe = "SELECT DISTINCT type FROM furnitures"
        my_cursor.execute(exe)
        res = my_cursor.fetchall()
       
        for t in res:
            ex = "SELECT COUNT(type) FROM furnitures WHERE rented = %s AND type = %s"
            
            v = (0 , t[0])
            my_cursor.execute(ex , v)
            r = my_cursor.fetchall()
            
            if r[0][0]<6:
                my_text.insert(END , "          " + t[0] + " type of furniture is low !\n")
            pass
        pass

# Admin should also be able to see the total investment and profit on his dashboard

    def checkInvestmentAndProfit():
       ''' inv = Tk()
        inv.geometry("1360x678")
        leftBg = "slate blue"
        rightBg = "yellow green"
        fram1 = Frame(inv , background = leftBg)
        fram2 = Frame(inv , background = rightBg)
        fram1.grid(row = 0 , column = 0 , sticky = "nsew")
        fram2.grid(row = 0 , column = 1 , sticky = "nsew")
        inv.grid_columnconfigure(0 , weight = 3)
        inv.grid_columnconfigure(1 , weight = 4)
        inv.grid_rowconfigure(0 , weight = 1)
        fram1.grid_propagate(False)
        fram2.grid_propagate(False)
        
        exe = "SELECT SUM(investment) FROM admins"
        my_cursor.execute(exe)
        investment = my_cursor.fetchall()
        
        l4 = Label(fram1 , text = "INVESTMENT = " + str(investment[0][0]), bg=leftBg, font=("Century gothic", 13, "bold"))
        l4.grid(row=0, column=0, pady=200, padx=25)
        
        exe = "SELECT SUM(profit) FROM admins"
        my_cursor.execute(exe)
        pro = my_cursor.fetchall()
       
        l5 = Label(fram1 , text = "Profit = " + str(pro[0][0]), bg=leftBg, font=("Century gothic", 13, "bold"))
        
        l5.grid(row=1, column=0, padx=25)
        exe = "SELECT profit , investment FROM graph"
        my_cursor.execute(exe)
        rel = my_cursor.fetchall()
        x = []
        y = []
        for tup in rel:
            x.append(tup[1])
            y.append(tup[0])
        fig = Figure(figsize = (8,6),dpi = 100)
        canvas = FigureCanvasTkAgg(fig, master = fram2)
        plot1 = fig.add_subplot(111)
        plot1.plot(x,y)
        plot1.set_xlabel("investment")
        plot1.set_ylabel("profit")
        canvas.draw()
        canvas.get_tk_widget().pack(pady = 30 , padx = 8)'''
    pass

# For changing the price of a product we first check the product's existance and if exists we update its price in the database 
    def changePrice():
        change = Tk()
        change.geometry("600x400")
        change.title("CHANGE THE PRICE")
        changeBg = "gold"
        change.config(bg=changeBg)

        Label(change, text = "Enter the type of the furniture for changing price: ", font=("Times New Roman", 15), bg=changeBg).grid(row = 0 , column = 0, padx=10, pady=10)
        e2 = Entry(change, relief=FLAT)
        e2.grid(row = 0 , column = 1)
        Label(change , text = "Enter the new price :", font=("Times New Roman", 15), bg=changeBg).grid(row = 1 , column = 0, padx=10, pady=10)
        e3 = Entry(change, relief=FLAT)
        e3.grid(row = 1 , column = 1)

        def confirmPriceChange():
            typ = e2.get()
            np = e3.get()
            ex = "SELECT * FROM furnitures WHERE type = %s"
            va = (typ,)
            my_cursor.execute(ex , va)
            res = my_cursor.fetchall()
            if len(res) == 0:
                messagebox.showerror("Error", "No furniture of this type found !")
                return
            exe = "UPDATE furnitures SET price = %s WHERE type = %s"
            va = (np , typ)
            my_cursor.execute(exe , va)
            mydb.commit()
            
            messagebox.showinfo("Information", "Price Changed")
            pass

        Button(change , command = confirmPriceChange , text = "Alter", bg="red", font=("Arial", 16, "bold"), fg="white").grid(row = 2 , column = 1, pady=10)
        
        pass

# Readd the product to inventory 
    def reAddition():
        readd = Tk()
        readd.geometry("1000x500")
        readd.title("CHECKING RETURNED FURNITURE")
        rightBg = "lime green"
        leftBg = "indian red"
        rightFrame1 = Frame(readd , width = 50 , height= 100 , background = rightBg)
        leftFrame1 = Frame(readd , width = 50 , height = 100 , background = leftBg)
        leftFrame1.grid(row = 0 , column = 0 , sticky = "nsew")
        rightFrame1.grid(row = 0 , column = 1 , sticky = "nsew")
        readd.grid_columnconfigure(0 , weight = 2)
        readd.grid_columnconfigure(1 , weight = 3)
        readd.grid_rowconfigure(0 , weight = 1)
        leftFrame1.grid_propagate(False)
        leftFrame1.pack_propagate(False)
        rightFrame1.grid_propagate(False)
        rightFrame1.pack_propagate(False)

        text_scroll1 = Scrollbar(rightFrame1)
        text_scroll1.pack(side = RIGHT , fill = Y)
        my_text1 = Text(rightFrame1 , width = 100 , height = 120 , font = ('Comic sans ms' , 10) , yscrollcommand = text_scroll1.set, spacing1=8)
        my_text1.pack(pady = 10 , padx = 10)
        text_scroll1.config(command = my_text1.yview)

        ex = "SELECT * FROM current_returns"
        my_cursor.execute(ex)
        result = my_cursor.fetchall()
        for query in result:
            my_text1.insert(END , "         Furniture id = " + str(query[2]) + " Username = " + str(query[1]) + "\n")

        l1 = Label(leftFrame1 , text = "Enter the furniture id : ", font=("Eras Demi ITC", 12), bg=leftBg)
        e1 = Entry(leftFrame1)
        l1.grid(row = 0 , column = 0, padx=10, pady=10)
        e1.grid(row = 0 , column = 1)
        l2 = Label(leftFrame1 , text = "Enter the username : ", font=("Eras Demi ITC", 12), bg=leftBg)
        e2 = Entry(leftFrame1)
        l2.grid(row = 1 , column = 0, padx=10, pady=10)
        e2.grid(row = 1 , column = 1)
        v1 = StringVar(leftFrame1 , "1")
        R1 = Radiobutton(leftFrame1 , text = "Damaged" , variable = v1 , value = "1", bg=leftBg)
        R2 = Radiobutton(leftFrame1 , text = "Not Damaged" , variable = v1 , value ="2", bg=leftBg)
        R1.grid(row = 2 , column = 0, padx=10, pady=10)
        R2.grid(row = 2 , column = 1, padx=10, pady=10)


        def completereturn():
            fur_id = e1.get()
            user = e2.get()
            if v1.get() == "1" :
                ex = "SELECT price FROM furnitures WHERE id = %s"
                va = (fur_id,)
                my_cursor.execute(ex , va)
                price = my_cursor.fetchall()
                ex = "SELECT amountdue FROM customers WHERE username = %s"
                va = (user,)
                my_cursor.execute(ex , va)
                oldamount = my_cursor.fetchall()
                ex = "UPDATE customers SET amountdue = %s WHERE username = %s"
                va = (oldamount[0][0] + price[0][0] , user)
                my_cursor.execute(ex , va)
                mydb.commit()
                ex = "DELETE FROM furnitures WHERE id = %s"
                va = (fur_id , )
                my_cursor.execute(ex , va)
                mydb.commit()
                messagebox.showinfo("Information", "Furniture Deleted !")
               
                pass
            else:
                ex = "UPDATE furnitures SET rented = %s WHERE id = %s"
                va = (0 , fur_id )
                my_cursor.execute(ex , va)
                mydb.commit()
                messagebox.showinfo("Information", "Furniture Added to the Inventory !")
               
                pass
            ex = "DELETE FROM current_returns WHERE username = %s AND furniture_id = %s"
            va = (user , fur_id)
            my_cursor.execute(ex , va)
            mydb.commit()
            ex = "SELECT * FROM current_returns"
            my_cursor.execute(ex)
            result = my_cursor.fetchall()
            my_text1.delete("1.0",END)
            for query in result:
                my_text1.insert(END , "Furniture id = " + str(query[2]) + " Username = " + str(query[1]) + "\n")
            pass

        b1 = Button(leftFrame1 , text = "Complete the return !" , command = completereturn, bg="sandy brown", font=("Arial", 13, "bold"), fg="white")
        b1.grid(row = 3 , column = 0 , columnspan = 2)
        pass
    
    btnBg = "yellow"
    Button(admin , text = "Create a customer account" , width = 30 , command = createCustomer, bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=(50,10))
    Button(admin , text = "Delete a customer account" , width = 30 , command = deleteCustomer, bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=10)
    Button(admin , text = "See the notifications" , width = 30 , command = seeNotifications, bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=10)
    Button(admin , text = "Investment and profit" , width = 30 , command = checkInvestmentAndProfit, bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=10)
    Button(admin , text = "Change price" , width = 30 , command = changePrice, bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=10)
    Button(admin , text = "Check returns" , width = 30 , command = reAddition, bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=10)
    
    def adminlogoutcommand():
        Login(admin)

    
   
    def addingnewproducts():
        adnew=Tk()
        Label(adnew , text = "Add new funiture", bg=rightBg, relief=FLAT, font=("Verdana", 14), fg="red").grid(row=0, column=0, columnspan=2, padx=25)
        Label(adnew , text = "Name", bg=rightBg, relief=FLAT, font=("Verdana", 14)).grid(row = 1 , column = 0, padx=25, pady=10)
        Label(adnew , text = "Type", bg=rightBg, relief=FLAT, font=("Verdana", 14)).grid(row = 2 , column = 0, padx=25, pady=10)
        Label(adnew , text = "Price", bg=rightBg, relief=FLAT, font=("Verdana", 14)).grid(row = 3 , column = 0, padx=25, pady=10)
        Label(adnew , text = "Interest Rate", bg=rightBg, relief=FLAT, font=("Verdana", 14)).grid(row = 4 , column = 0, padx=25, pady=10)
        Label(adnew , text = "Description", bg=rightBg, relief=FLAT, font=("Verdana", 14)).grid(row = 5 , column = 0, padx=25, pady=10)
        Label(adnew , text = "Company", bg=rightBg, relief=FLAT, font=("Verdana", 14)).grid(row = 6 , column = 0, padx=35, pady=10)

        nameentry =  Entry(adnew, relief=FLAT)
        nameentry.grid(row = 1 , column = 1)
        name_type = Entry(adnew, relief=FLAT)
        name_type.grid(row = 2 , column = 1)
        enter_price = Entry(adnew , relief=FLAT)
        enter_price.grid(row = 3 , column = 1)
        enter_Interest_rate = Entry(adnew, relief=FLAT)
        enter_Interest_rate.grid(row = 4 , column = 1)
        enter_description = Entry(adnew, relief=FLAT)
        enter_description.grid(row = 5 , column = 1)
        enter_company = Entry(adnew, relief=FLAT)
        enter_company.grid(row = 6 , column = 1)
        
        global filepath
        filepath = ""
        
        def openImage():
            adnew.filename= filedialog.askopenfilename(initialdir = os.path.join(os.getcwd() , "images") , title = 'select an image' , filetypes = (("jpg files" , "*.jpg"),))
            global filepath
            filepath = adnew.filename

        def addNewFurniture():
            Name = nameentry.get()
            Description = enter_description.get()
            company = enter_company.get()
            type = name_type.get()
            Interestrate = (enter_Interest_rate.get())
            cost = (enter_price.get())
            date = dt.today().strftime('%Y-%m-%d')
            # print(filepath , date)
            if Name and cost and Description and type and Interestrate and filepath:
                Interestrate = float(Interestrate)
                cost = float(cost)
                exe = 'INSERT INTO furnitures (name , company , price , description , type , rented , photo , interest_rate , date_started) VALUES (%s , %s , %s , %s , %s , %s , %s , %s ,%s)'
                values = (Name , company , cost , Description , type , 0 , filepath , Interestrate , date)
                my_cursor.execute(exe , values)
                mydb.commit()
                
                exe = "UPDATE admins SET investment = investment + %s WHERE username = %s"
                va = (cost , user_id)
                my_cursor.execute(exe , va)
                mydb.commit()
                
                messagebox.showinfo("Information", "Furniture Added !")
                nameentry.delete(0,END)
                enter_price.delete(0,END)
                enter_description.delete(0,END)
                enter_company.delete(0,END)
                name_type.delete(0,END)
                enter_Interest_rate.delete(0,END)
                #testaddfuniture(type, filepath)
            else:
                messagebox.showwarning( "Fill all the fields")
            pass

        Button(adnew , text = "Choose Image" , command = openImage , width = 20, bg="violet", font=("Arial", 13, "bold")).grid(row = 7 , column = 0, padx=30, pady=10, columnspan=2)
        Button(adnew , text = "Add Furniture" , width = 30 , command = addNewFurniture, bg="lime green", font=("Arial", 13, "bold")).grid(row = 8 , column = 0, padx=30, pady=10, columnspan=2)
    
    Button(admin , text = "Add New Product" , width = 25 , command = addingnewproducts,  bg=btnBg,fg="black",font=("Century gothic", 13)).pack(pady=10)  
    Button(admin , text = "LOG OUT" , width = 25 , command = adminlogoutcommand, bg=btnBg,fg="purple",font=("Futura", 15)).pack(pady=10)




def Login(self):
    self.destroy()
    login = Tk()
    login.title("Log In to FRSS")
    loginBg = "ivory2"

    notif = Label(login, text=" Enter the login details !", font=("Comic sans ms", 15), fg="blue violet", bg=loginBg).grid(row=0, column=0, columnspan=2, padx=(70,0), pady=15)
    login.geometry("600x500")
    login.config(bg=loginBg)
    
    v1 = StringVar(login , "1")
    adminradiobutton = Radiobutton(login , text = "Admin" , variable = v1 , value = "1", font=("Arial", 12), bg=loginBg)
    customerradiobutton = Radiobutton(login , text = "Customer" , variable = v1 , value ="2", font=("Arial", 12), bg=loginBg)
    usernamel = Label(login , text = "Username", bg=loginBg,font=("Century gothic", 13))
    usernamel.grid(row = 1 , column = 0, padx=80, pady=10)
    passwdl = Label(login , text = "Password", bg=loginBg,font=("Century gothic", 13))
    passwdl.grid(row = 2 , column = 0, padx=(80,80), pady=10)
    adminradiobutton.grid(row = 3 , column = 0, padx=(80,80), pady=10)
    customerradiobutton.grid(row = 3 , column = 1, pady=10)

    def adduser():
        username = usernameentry.get()
        password = passwordentry.get()

        if username and password:
            if v1.get() == "2":
                exe =  f'SELECT username , password FROM customers WHERE username = "{username}" AND password = "{password}"'
                
                my_cursor.execute(exe)
                result  = my_cursor.fetchall()
                if len(result) == 0 :
                    messagebox.showerror("Error", "Invalid Username or Password !")
                    return 
                global user_id , pass_word , is_admin
                user_id = result[0][0]
                pass_word = result[0][1]
               
                is_admin = False
                CustomerPage(login)
            else :
                exe =  f'SELECT username , password FROM admins WHERE username = "{username}" AND password = "{password}"'
                
                my_cursor.execute(exe)
                result  = my_cursor.fetchall()
                if len(result) == 0 :
                    messagebox.showerror("Error", "Invalid Username or Password !")
                    return
                user_id = result[0][0]
                pass_word = result[0][1]
              
                is_admin = True
                AdminPage(login)

        else:
            messagebox.showwarning("ALERT !" , "All fields should be filled !")

    usernameentry = Entry(login, relief=FLAT)
    usernameentry.grid(row = 1 , column = 1)
    passwordentry = Entry(login , show ='*', relief=FLAT)
    passwordentry.grid(row = 2 , column = 1)
    
    completelogin = Button(login ,text="Proceed", command = lambda:adduser())
    completelogin.grid(row = 5,column=0 )
    

#clicking the signup option

def Signup():
    
    
    signup = Toplevel(bg="SkyBlue2")
    signup.geometry("650x700")
    signup.title("SIGN UP") 

    
    notif = Label(signup, text="Fill in the details!", font=("Comic sans ms", 13), fg="red", bg="#ffdc73")
    notif.grid(row=0, column=0, columnspan=2)
    Label(signup,  text="Name",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=1,column=0, padx=(50, 0), pady=(20, 10))
    Label(signup,  text="Username:",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=2,column=0, padx=(50, 0), pady=(20, 10))
    Label(signup,  text="Enter Password",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=3,column=0, padx=(50, 0), pady=(20, 10))
    Label(signup,  text="Confirm Password",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=4,column=0, padx=(50, 0), pady=(20, 10))
    Label(signup,  text="Address",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=5,column=0, padx=(50, 0), pady=(20, 10))
    Label(signup,  text="Phone No.",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=6,column=0, padx=(50, 0), pady=(20, 10))
    Label(signup,  text="Email Id",bg="SkyBlue2",fg="Black" , font=("Helvetica", 15)).grid(row=7,column=0, padx=(50, 0), pady=(20, 10))
    

#Buttons
    sendmailbtn = Button(signup, text="Verify details and send email", font = ("Arial", 10, "bold"),cursor="hand2", bg="green2", fg="maroon1", pady=1)
    sendmailbtn.grid(row=9, padx=40, pady=10, column=0, columnspan=2)
    verifymailbtn = Button(signup, text="Verify OTP!", font = ("Arial", 10), state=DISABLED,bg="green2", fg="maroon1" )
    verifymailbtn.grid(row=13, padx=10, pady=10, column=1)

#entry widgets
    nameentry = Entry(signup , width = 50, relief=FLAT)
    nameentry.grid(row = 1 , column = 1, padx=10, pady=10)
    usernameentry = Entry(signup , width = 50, relief=FLAT)
    usernameentry.grid(row = 2 , column = 1, padx=10, pady=10)
    passwordentry = Entry(signup , width = 50  , show ='*', relief=FLAT)
    passwordentry.grid(row = 3 , column = 1, padx=10, pady=10)
    confirmpasswordentry = Entry(signup , width = 50  , show = '*', relief=FLAT)
    confirmpasswordentry.grid(row = 4 , column = 1, padx=10, pady=10)
    addressentry = Entry(signup , width = 50, relief=FLAT )
    addressentry.grid(row = 5 , column = 1, padx=10, pady=10)
    phonenumberentry = Entry(signup , width = 50, relief=FLAT)
    phonenumberentry.grid(row = 6 , column = 1, padx=10, pady=10)
    emailentry = Entry(signup, width = 50, relief=FLAT)
    emailentry.grid(row=7, column=1, padx=10, pady=10)
    otpEntry = Entry(signup, width=50, relief=FLAT)
    otpEntry.grid(row=10, column=1, padx=10, pady=10)

# Using RadioButtons
    
    v1 = StringVar(signup , "1")
    adminradiobutton = Radiobutton(signup , text = "Admin" , variable = v1 , value = "1", bg="SkyBlue2", font=("Arial", 12))
    adminradiobutton.grid(row = 8 , column = 0, padx=10, pady=10)
    customerradiobutton = Radiobutton(signup , text = "Customer" , variable = v1 , value ="2", bg="SkyBlue2", font=("Arial", 12))
    customerradiobutton.grid(row = 8, column = 1, padx=10, pady=10)

    def verifyNSend():                                      
        name = nameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        cpassword = confirmpasswordentry.get()
        address = addressentry.get()
        phonenumber = phonenumberentry.get()
        emailid = emailentry.get()

        global starttime 
        starttime = time.time()
        global otp
        otp = ""

        if v1.get() == "2":
            if name and username and password and cpassword and address and phonenumber and emailid:        
                my_cursor.execute("SELECT username from customers")
                total = my_cursor.fetchall()
                if len(total) > 0 and username in total[0]:
                    messagebox.showwarning("ALERT !" , "User name already registered")
                    usernameentry.delete(0 , END)
                elif password != cpassword:
                    messagebox.showerror("ALERT !" , "Passwords do not match")
                    passwordentry.delete(0 , END)
                    confirmpasswordentry.delete(0 , END)
                else:
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()       
                        server.login("frssassignment@gmail.com", "frss@123") 
                        dig = "0123456789"
                        for _ in range(4):
                            otp += random.choice(dig)
                        finalMessage = "OTP for login verification to our Furniture rental store system is " + otp
                        to = emailentry.get()
                        server.sendmail("frssassignment@gmail.com", to, finalMessage)      
                        notif.config(text = "Success! Email has been sent. Enter OTP sent to email id in 2 minutes", fg = "green")
                        verifymailbtn.config(state=ACTIVE, bg="#4169e1", fg="white")
                    except:
                        messagebox.showerror("Invalid email!" , "Error! Please check the email id entered")
            else:
                messagebox.showwarning("ALERT !" , "Fill all the fields")
                
        else:
            if name and username and password and cpassword and address and phonenumber:
                my_cursor.execute("SELECT username from admins")
                total = my_cursor.fetchall()
                
                if len(total) > 0 and username in total[0]:
                    messagebox.showwarning("ALERT !" , "User name already registered")
                    usernameentry.delete(0 , END)
                    
                elif password != cpassword:
                    messagebox.showwarning("ALERT !" , "Passwords do not match")
                    passwordentry.delete(0 , END)
                    confirmpasswordentry.delete(0 , END)
                else:
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()       
                        server.login("frssassignment@gmail.com", "frss@123") 
                        dig = "0123456789"
                        for _ in range(4):
                            otp += random.choice(dig)
                        finalMessage = "OTP for login verification to our Furniture rental store system is " + otp
                        to = emailentry.get()
                        server.sendmail("frssassignment@gmail.com", to, finalMessage)      
                        notif.config(text = "Success! Email has been sent. Enter OTP sent to email id in 2 minutes", fg = "green")
                        verifymailbtn.config(state=ACTIVE, bg="#4169e1", fg="white")
                    except:
                        messagebox.showwarning("Invalid email!" , "Error! Please check the email id entered")
            else:
                messagebox.showwarning("ALERT !" , "Fill all the fields")
                

    def verifyOTP():
        end = time.time()
        t = format(end-starttime)
        if float(t) >= 180:
            messagebox.showinfo("Timed out", "Session expired! Please regenerate OTP")
        else:
            enteredOTP = otpEntry.get()
            if enteredOTP == otp:
                notif.config(text = "Successfully verified OTP! Please click on Sign Up button to add your account!", fg = "green")
                addbutton.config(state=ACTIVE)
            else:
                messagebox.showerror("Invalid OTP", "Please enter a valid OTP!")

    def adduser():
        name = nameentry.get()
        username = usernameentry.get()
        password = passwordentry.get()
        address = addressentry.get()
        phonenumber = phonenumberentry.get()

        if v1.get() == "1":
            exe = 'INSERT INTO admins (name , username , password , address , phonenumber) VALUES (%s , %s , %s , %s , %s)'
            values = (name , username , password , address , phonenumber)
            my_cursor.execute(exe , values)
            mydb.commit()
            notif.config(text="Successfully added to database!")
           
            

        else:
            exe = 'INSERT INTO customers (name , username , password , address , phonenumber) VALUES (%s , %s , %s , %s , %s)'
            values = (name , username , password , address , phonenumber)
            my_cursor.execute(exe , values)
            mydb.commit()
            notif.config(text="Successfully added to database!")
            
            
  
    
    
    addbutton = Button(signup, text="signup",command = lambda: adduser())
    addbutton.grid(row=14 , column=1, pady=3)   
    sendmailbtn.config(command=verifyNSend)
    verifymailbtn.config(command=verifyOTP)





if __name__ == '__main__':
    root = Tk()


#creating database and tables

    mydb = connector.connect(host = "localhost",
								user = "root",
								password = "",
                                database = "frss")

    global my_cursor
    my_cursor = mydb.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS frss")
    

    my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255) NOT NULL,username VARCHAR(255) PRIMARY KEY,password VARCHAR(255) NOT NULL,address VARCHAR(255) NOT NULL, phonenumber VARCHAR(255) NOT NULL,amountdue DECIMAL(8,2) DEFAULT 0,numberoforders INT(10))")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS admins (name VARCHAR(255) NOT NULL,username VARCHAR(255) PRIMARY KEY,password VARCHAR(255) NOT NULL,address VARCHAR(255) NOT NULL, phonenumber VARCHAR(255) NOT NULL,profit DECIMAL(8,2) DEFAULT 0,investment DECIMAL(8,2) DEFAULT 0)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS furnitures (id INT auto_increment primary key, name VARCHAR(255) NOT NULL , company VARCHAR(255) NOT NULL , price DECIMAL(8,2) , description VARCHAR(255) NOT NULL , type VARCHAR(255) NOT NULL , rented INT , photo VARCHAR(255) NOT NULL , interest_rate DECIMAL(4,2) , date_started DATE , date_ended DATE , username VARCHAR(255) , FOREIGN KEY (username) REFERENCES customers(username) , days_rented INT DEFAULT 0)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS past_orders (id INT auto_increment primary key , username VARCHAR(255) , furniture_id INT)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS feedbacks (id INT auto_increment primary key , type VARCHAR(255), review VARCHAR(255))")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS current_returns (id INT auto_increment primary key , username VARCHAR(255), furniture_id INT)")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS graph (id INT auto_increment primary key , profit DECIMAL(8,2) DEFAULT 0 , investment DECIMAL(8,2) DEFAULT 0)")


bg_color = "LightCyan"
fg_color = "#383a39"
root.configure(background= bg_color)
root.title("Welcome")
photo = ImageTk.PhotoImage(Image.open("frssimage.jpg"))
Label(root, image=photo).grid(rowspan = 3, columnspan = 5, row =0,column = 0)
Button(root, text="Login",borderwidth=3, relief='ridge', fg=fg_color, bg="green2", width = 20, command =lambda : Login(root)).grid(row = 6,column=1,  padx=(50, 0), pady=(20, 10))
Button(root, text="SignUp",borderwidth=3, relief='ridge', fg=fg_color, bg="green2", width = 20, command = Signup).grid(row = 6,column=2,  padx=(50, 0), pady=(20, 10))
root.mainloop()