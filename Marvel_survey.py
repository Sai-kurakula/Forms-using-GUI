from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

window = Tk()
font  = ('times', 18, 'bold')
frame = Frame(window, bg = 'Red' )
frame.pack()
window.title("Marvel Survey")

window.geometry("800x400")

window.configure(bg = 'red')
operator_selected = False

#row 0: Title

title = Label(frame, text = "MARVEL SURVEY", font = ("times", 22, 'bold'), bg = 'red', fg = 'white' )
title.grid(row = 0 , columnspan = 2)

#row 1: Lable: What is your favourite marvel movie?

Q1_l = Label(frame, text = "1) Enter the name of your favorite Marvel movie:", font = font, bg = 'red', fg = 'white'  )
Q1_l.grid( row= 1, column= 0)
Q1_Entry = Entry(frame, width = 25, font = font, bd = 4,foreground = 'red')

Q1_Entry.grid(row = 1, column = 1)

#row 2, 3,4,5: Label: select three favorite superheros:

Q2_l = Label(frame, text = "2) Please select your top three favorite superheros: ", font = font, bg = 'red', fg = 'white'
             )
Q2_l.grid(row =2, column = 0)

heros = [ "Spider-Man", "Iron Man", "Captain America", "the Hulk", "Thor", "Wolverine", "Ant-Man", "the Wasp", "Black Widow",
          "Hawkeye", "Captain Marvel", "Black Panther", "Doctor Strange", "the Scarlet Witch", "Quicksilver", "She-Hulk", "the Vision", "the Falcon", "the Winter Soldier", "Ghost Rider", "Blade", "Daredevil"," Ms. Marvel", "Miles Morales", "the Punisher", "Deadpool", "other"]



heros1_menu = ttk.Combobox(frame,values = heros , width = 11, font = font, foreground = "red")
heros1_menu.grid(row= 3, column = 0)


heros2_menu = ttk.Combobox(frame,values = heros , width = 11, font = font, foreground = "red")
heros2_menu.grid(row= 4, column = 0)


heros3_menu = ttk.Combobox(frame,values = heros , width = 11, font = font, foreground = "red")
heros3_menu.grid(row= 5, column = 0)

#row 6

Q_3 = Label(frame, text = "3) Is DC better than Marvel?", font = font, bg = 'red', fg = 'white')
Q_3.grid(row = 6, column = 0)

var = IntVar()
rb_yes =  Radiobutton(frame, text = "Yes", variable = var,value = 1, font = font, background= "red" )
rb_yes.grid(row = 6, column = 1)
rb_no =  Radiobutton(frame, text = "No", variable = var,value = 2, font = font, background= "red" )
rb_no.grid(row = 6, column = 2)


#row 7: Submit
def submit ():
    con = sqlite3.connect("Marvel.db")
    cur = con.cursor()
    Movie =  Q1_Entry.get()
    superhero_1 = heros1_menu.get()
    superhero_2 = heros2_menu.get()
    superhero_3 = heros3_menu.get()
    dc_marvel = var.get()
    list = ["none", "Dc", "Marvel"]
    universe = list[dc_marvel]






    # create a table:
    cur.execute('''CREATE TABLE IF NOT EXISTS signup_info
                           (Favourite_Movie text, superhero_1 text, superhero_2 text, superhero_3 text, Universe text)''')
    insert_command = "INSERT INTO signup_info VALUES ('" + Movie + "','" + superhero_1 + "', '" + superhero_2 + "' ,'" + superhero_3 + "','" + universe + "')"
    cur.execute(insert_command)

    con.commit()
    con.close()




b_submit = Button( frame, text = "Submit", command = submit, font = ("times", 22, 'bold'), bd = 6)
b_submit.grid(row = 8, columnspan = 3)




window.mainloop()

