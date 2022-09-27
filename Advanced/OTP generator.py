'''In this tutorial are going to make a real-time GUI to Send OTP Using Python. For this project, we are going to use four modules namely Tkinter, Requests, Random, and JSON.
Tkinter will be used for creating the UI.
Requests will be used to send a GET request to the site.
JSON will be used for setting the parameters and the random module will be used for generating the OTP.
Also, you need to create an account on fast2sms. Creating an account is very simple. Go to http://www.fast2sms.com and create an account for free. As a new user, you will receive 50 rupees balance in your wallet.
Now Goto Dev API and generate your API. Copy your unique API and paste in the JSON part of the code.'''

from tkinter import *
import tkinter.messagebox as tsmg
import requests
import random
import json

root=Tk()

rand=random.randint(1,999999)

msg=f"Your One Time Password(OTP) is {rand}"

def sms_send(a,msg):
    url="https://www.fast2sms.com/dev/bulk"
    params={
        "authorization":"ZctzPjmw1mzJXKcdpPXRJR3c",#paste your api here by going to devapi and login to generate an api
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":a
    }
    rs=requests.get(url,params=params)


def send():
    a=num.get()
    if(a==""):
        tsmg.showerror("Error","Enter Your Mobile Number")
    elif (len(a)<10):
        tsmg.showerror("Error","Invalid Mobile Number")
        num.set("")
    else:
        b=tsmg.askyesno("Info",f"Your Number is {a}")
        if(b==True):
            sms_send(a,msg)
        else:
            num.set("")

def check():
    c=otp.get()
    if(c==""):
        tsmg.showerror("Error","Enter OTP")
    else:
        if(str(rand)==c):
            tsmg.showinfo("Info","Successful")
        else:
            tsmg.showerror("Error","Invalid OTP")
            num.set("")
            otp.set("")


root.geometry("500x500")
root.title("OTP-Checker")

num=StringVar()
otp=StringVar()

f1=Frame(root)
Label(f1,text="Check Your OTP",font="SegoeUI 30 bold",fg="purple").pack(padx=5,pady=10)
f1.pack(fill=BOTH)

f2=Frame(root)
Label(f2,text="Enter Your Number",font="SegoeUI 20 bold",fg="teal").pack(padx=5,pady=5)
e1=Entry(f2,textvariable=num,font="SegoeUI 14 bold",fg="black",bg="white",relief=SUNKEN,borderwidth=4,justify="center").pack(ipady=5)
f2.pack(fill=BOTH,padx=5,pady=10)

f3=Frame(root)
Label(f3,text="Enter OTP",font="SegoeUI 20 bold",fg="teal").pack(padx=5,pady=5)
e2=Entry(f3,textvariable=otp,font="SegoeUI 14 bold",fg="black",bg="white",relief=SUNKEN,borderwidth=5,justify="center").pack(ipady=5)
f3.pack(fill=BOTH,padx=5,pady=10)

f4=Frame(root)
Button(f4,text="Send OTP",command=send,font="SegoeUI 10 bold",fg="purple").pack(padx=20,pady=10,side=LEFT)
Button(f4,text="Check OTP",command=check,font="SegoeUI 10 bold",fg="purple").pack(padx=40,pady=10,side=LEFT)
f4.pack()


root.mainloop()