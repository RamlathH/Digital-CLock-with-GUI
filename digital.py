from tkinter import *
import datetime

def date_time():
    time =datetime.datetime.now()
    hr = time.strftime('%I')#Gives the hours %I
    min = time.strftime('%M')#Gives the surf time in  minutes %M
    sec = time.strftime('%S')#Gives the surf time sec %S
    am = time.strftime('%p')#Gives the surf time am /pm %p

    date = time.strftime("%d")#date
    month= time.strftime("%m")#month
    year = time.strftime("%y")#year
    day = time.strftime("%a")#day

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_hr.after(200,date_time)#change graphics data everytime 

    lab_date.config(text=date)
    lab_month.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)#change graphics data everytime 

clock = Tk()#class
clock.title("       Digital Clock       ")
clock.geometry('1000x500')#size of the window
clock.config(bg ="Pink")#background color

# hour
lab_hr = Label(clock,text = "00" , font = ("Times New Roman",60,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_hr.place(x=120,y=50,height = 110, width = 100)
lab_hr_txt = Label(clock,text = "Hour" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_hr_txt.place(x=120,y=190,height =40, width = 100)

# minute
lab_min = Label(clock,text = "00" , font = ("Times New Roman",60,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_min.place(x=340,y=50,height = 110, width = 100)
lab_min_txt = Label(clock,text = "Min" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_min_txt.place(x=340,y=190,height =40, width = 100)

# Second
lab_sec = Label(clock,text = "00" , font = ("Times New Roman",60,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_sec.place(x=560,y=50,height = 110, width = 100)
lab_sec_txt = Label(clock,text = "Sec" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_sec_txt.place(x=560,y=190,height =40, width = 100)

# AM/PM
lab_am = Label(clock,text = "00" , font = ("Times New Roman",50,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_am.place(x=780,y=50,height = 110, width = 100)
lab_am_txt = Label(clock,text = "AM/PM" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_am_txt.place(x=780,y=190,height=40, width = 100)

#date
lab_date = Label(clock,text = "00" , font = ("Times New Roman",60,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_date.place(x=120,y=270,height = 110, width = 100)
lab_date_txt = Label(clock,text = "Date" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_date_txt.place(x=120,y=410,height =40, width = 100)

#month
lab_month= Label(clock,text = "00" , font = ("Times New Roman",60,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_month.place(x=340,y=270,height = 110, width = 100)
lab_month_txt = Label(clock,text = "Month" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_month_txt.place(x=340,y=410,height =40, width = 100)

#Year
lab_year = Label(clock,text = "00" , font = ("Times New Roman",60,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_year.place(x=560,y=270,height = 110, width = 100)
lab_year_txt = Label(clock,text = "Year" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_year_txt.place(x=560,y=410,height =40, width = 100)

#day

lab_day = Label(clock,text = "00" , font = ("Times New Roman",40,"italic"),
 bg = "black" ,fg ="white")#label gives the color font
lab_day.place(x=780,y=270,height = 110, width = 100)
lab_day_txt = Label(clock,text = "Day" , font = ("Times New Roman",20,"italic"),
 bg = "black" ,fg ="white")
lab_day_txt.place(x=780,y=410,height=40, width = 100)

date_time()

clock.mainloop()#mainloop graphics on 