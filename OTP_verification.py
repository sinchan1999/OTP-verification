from tkinter import *
from tkinter import messagebox
import smtplib
import random
import math

# Graphical Interface
root = Tk()
root.title("Send OTP Via Email")
root.geometry("600x250")
email_label = Label(root, text="Enter Receiver's Email: ",
                    font=("arial 15 bold"), relief=FLAT)
email_label.grid(row=0, column=0, padx=10, pady=60)
email_entry = Entry(root, font=("arial 15 bold"),
                    width=25, relief=GROOVE, bd=4)
email_entry.grid(row=0, column=1, padx=10, pady=60)
email_entry.focus()

# digits contains the all the possible OTP digits from which our program will select randomly.
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]

# SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon


def send():
    try:
        s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
        s.starttls()
        # Check how to generate app password if you dont know!
        s.login("<Sender email ID>", "<Sender App password>")
        otp = OTP
        otp = str(otp)

        s.sendmail("sender_email", email_entry.get(), otp)
        messagebox.showinfo("Send OTP via Email",
                            f"OTP sent to {email_entry.get()}")
        s.quit()

# Giving error message if User enters Invalid email address OR his/her interner connection is too poor!
    except:
        messagebox.showinfo("Send OTP via Email",
                            "Please enter the valid email address OR check an internet connection")


# Setting button properties
send_button = Button(root, text="Send OTP", font=(
    "arial 15 bold"), bg="black", fg="#03e8fc", bd=5, command=send)
send_button.place(x=230, y=150)

# Run a loop which inturn gives the user 5 chances to enter correct opt , after that the OTP expires.
root.mainloop()
print("OTP verification Process :")
tryCounts = 1
while(tryCounts <= 5):
    response = input("Enter Your OTP >>: ")
    if response == OTP:
        print("OTP Verification is Sucessfully !!!\n------WELCOME USER------")
        break
    elif (5-tryCounts) == 0:
        print("Sorry, you exceded the limits & this OTP has expired. Please try after sometime\n------THANK YOU------")
    else:
        print("Please Check your OTP again ! \n")
        print("No.of try left: ", (5-tryCounts))
    tryCounts = tryCounts+1
