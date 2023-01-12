from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# creating the window;
window = Tk()

#adding title to the window.
window.title("SIGN-UP Form")

#dimensions of the window.
window.geometry("800x400") # (width,Height)



entry_font = ("times",18,"bold" )

frame = Frame(window)

frame.pack()


# row 0: Labels and Entry boxes
l_fname = Label(frame, text = "First Name", font = entry_font )
l_fname.grid(row = 0, column = 0)
e_fname = Entry(frame,width = 10, font = entry_font, bd = 4)
e_fname.grid(row = 0, column = 1)
l_lname = Label(frame, text = "Last Name", font = entry_font )
l_lname.grid(row = 0, column = 2)
e_lname = Entry(frame,width = 10, font = entry_font, bd = 4)
e_lname.grid(row = 0, column = 3)

# row 1: Labels and Entry boxes

l_username = Label(frame, text = "User Name", font = entry_font )
l_username.grid(row = 1, column = 0)
e_username = Entry(frame,width = 20, font = entry_font, bd = 4)
e_username.grid(row = 1, column= 1)


# row 2 : Labels and entry boxes:

l_choose_password = Label(frame, text = "Choose Password:", font = entry_font )
l_choose_password.grid(row = 2, column = 0)
e_choose_password = Entry(frame,width = 20, font = entry_font, bd = 4, show = "*")
e_choose_password.grid(row = 2, column= 1)

# row 3 : Labels and entry boxes:

l_confirm_password = Label(frame, text = "Confirm Password:", font = entry_font )
l_confirm_password.grid(row = 3, column = 0)
e_confirm_password = Entry(frame,width = 20, font = entry_font, bd = 4, show = "*")
e_confirm_password.grid(row = 3, column= 1)

# row 4: Label and Combobox
l_dob = Label(frame, text = "Date of Birth:", font = entry_font )
l_dob.grid(row = 4, column = 0)

l_month = Label(frame, text = "Month", font = entry_font)
l_month.grid(row = 4, column = 1)


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
month_menu = ttk.Combobox(frame,values = months , width = 11, font = entry_font)
month_menu.grid(row= 4, column = 2)

# row 5: Label and Combobox

l_day = Label(frame, text = "Day", font = entry_font)
l_day.grid(row = 5, column = 1)

days= []
for i in range(1,32,1):
    days.append(i)
day_menu = ttk.Combobox(frame,values = days , width = 11, font = entry_font)
day_menu.grid(row= 5, column = 2)


# row 6: Label and Combobox
l_year = Label(frame, text = "Year", font = entry_font)
l_year.grid(row = 6, column = 1)

years= []
for i in range(1921,2021,1):
    years.append(i)
year_menu = ttk.Combobox(frame,values = years , width = 11, font = entry_font)
year_menu.grid(row= 6, column = 2)


#row 7: Button

def submit():
    # assigning all the userinputs to variables.
    first_name = e_fname.get()
    last_name = e_lname.get()
    user_name = e_username.get()
    choose_password = e_choose_password.get()
    confirm_password = e_confirm_password.get()
    dob = month_menu.get() + "-" + str(day_menu.get()) + "-" + str(year_menu.get())


    #if and else statements

    if choose_password == confirm_password:
        con = sqlite3.connect("student.db")
        cur = con.cursor()

        # create a table:
        cur.execute('''CREATE TABLE IF NOT EXISTS signup_info
                       (firstName text, lastName text, userName text, password text, dob text)''')
        insert_command = "INSERT INTO signup_info VALUES ('" + first_name + "','" + last_name + "', '"+user_name+"' ,'" + choose_password + "', '" + dob + "')"
        cur.execute(insert_command)

        con.commit()
        con.close()

        s_msg = messagebox.showinfo("Info", "Your account has been created successfully")

    else:
        e_msg = messagebox.showinfo("Error", "The confirm password and and choose password entries do not match")


mbfont = ("times",32,"bold", )
b_submit = Button(frame, text = "Submit", command = submit, font = mbfont, bd = 6)
b_submit.grid(row = 7, column = 1)


window.mainloop()