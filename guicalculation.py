import tkinter as tk
#from turtle import title
root  = tk.Tk()
root.title("Result 2.0")
root.geometry("1200x750+0+0")
root.config(bg="pink")

font=("monotype corwas",40,'bold')
bg='white'
fg='black'

sid=tk.StringVar()
F_Name=tk.StringVar()
degree=tk.StringVar()
stream=tk.StringVar()
email=tk.StringVar()
phone=tk.StringVar()

python=tk.IntVar()
ml=tk.IntVar()
sql=tk.IntVar()
total=tk.IntVar()
per=tk.IntVar()
grade=tk.StringVar()
    
#functions 

def close_window():
    ask = tk.messagebox.askyesno('WARNING','Do you really want to exit?')
    if ask:
        root.destroy()


def clear_window():
    sid.set('')
    F_Name.set('')
    degree.set('')
    stream.set('')
    email.set('')
    phone.set('')
    python.set('')
    ml.set('')
    sql.set('')
    total.set('')
    per.set('')
    grade.set('')
    
def calculation():
    sum = python.get()+ml.get()+sql.get()
    total.set(sum)
    perc = sum/3
    per.set(perc)
    if perc >= 90:
        grade.set('O')
    elif perc >= 80:
        grade.set('A')
    elif perc >= 70:
        grade.set('B')
    elif perc >= 60:
        grade.set('C')
    elif perc >= 50:
        grade.set('D')
    elif perc >=35:
        grade.set('E')
    else:
        grade.set('F')
        

#creating a frame:-
top_frame=tk.Frame(root, bg="white")
top_frame.place(x=5, y=5,width=1510,height=100)

left_frame=tk.Frame(root, bg="white")
left_frame.place(x=5, y=110,width=752,height=530)

right_frame=tk.Frame(root, bg="white")
right_frame.place(x=762, y=110,width=752,height=530)



bottom_frame=tk.Frame(root, bg="white")
bottom_frame.place(x=5, y=647,width=1510,height=100)

#lable for top frame
title=tk.Label(top_frame,text="Result 2.0",
               bg=bg,font=font,fg=fg )
title.pack(pady=30)

# create a lable for left frame
left_title=tk.Label(left_frame, text="S_info :-",
                    bg=bg,font=("monotype corwas",30,'bold'),fg=fg)
left_title.grid(row=0,column=0,padx=5,pady=5)

# create a lable for right frame
right_title=tk.Label(right_frame, text="M_info :-",
                    bg=bg,font=("monotype corwas",30,'bold'),fg=fg)
right_title.grid(row=0,column=0,padx=5,pady=5)

  

        
#create a lable and textbox for left frame
sid_lable=tk.Label(left_frame,text="Sid",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
sid_lable.grid(row=1,column=0,padx=5,pady=5)
sid_entry=tk.Entry(left_frame,textvariable=sid,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
sid_entry.grid(row=1,column=1,padx=5,pady=5)

fname_lable=tk.Label(left_frame,text="F_Name",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
fname_lable.grid(row=2,column=0,padx=5,pady=5)
fname_entry=tk.Entry(left_frame,textvariable=F_Name,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
fname_entry.grid(row=2,column=1,padx=5,pady=5)

stream_lable=tk.Label(left_frame,text="Stream",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
stream_lable.grid(row=4,column=0,padx=5,pady=5)
stream_entry=tk.Entry(left_frame,textvariable=stream,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
stream_entry.grid(row=4,column=1,padx=5,pady=5)

degree_lable=tk.Label(left_frame,text="Degree",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
degree_lable.grid(row=3,column=0,padx=5,pady=5)
degree_entry=tk.Entry(left_frame,textvariable=degree,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
degree_entry.grid(row=3,column=1,padx=5,pady=5)

email_lable=tk.Label(left_frame,text="Email",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
email_lable.grid(row=5,column=0,padx=5,pady=5)
email_entry=tk.Entry(left_frame,textvariable=email,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
email_entry.grid(row=5,column=1,padx=5,pady=5)

phone_lable=tk.Label(left_frame,text="Phone",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
phone_lable.grid(row=6,column=0,padx=5,pady=5)
phone_entry=tk.Entry(left_frame,textvariable=phone,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
phone_entry.grid(row=6,column=1,padx=5,pady=5)



#create a lable and textbox for right frame
python_lable=tk.Label(right_frame,text="Python",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
python_lable.grid(row=1,column=0,padx=5,pady=5)
python_entry=tk.Entry(right_frame,textvariable=python,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
python_entry.grid(row=1,column=1,padx=5,pady=5)

ml_lable=tk.Label(right_frame,text="ML",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
ml_lable.grid(row=2,column=0,padx=5,pady=5)
ml_entry=tk.Entry(right_frame,textvariable=ml,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
ml_entry.grid(row=2,column=1,padx=5,pady=5)

sql_lable=tk.Label(right_frame,text="SQL",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
sql_lable.grid(row=3,column=0,padx=5,pady=5)
sql_entry=tk.Entry(right_frame,textvariable=sql,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
sql_entry.grid(row=3,column=1,padx=5,pady=5)

total_lable=tk.Label(right_frame,text="Total",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
total_lable.grid(row=4,column=0,padx=5,pady=5)
total_entry=tk.Entry(right_frame,textvariable=total,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
total_entry.grid(row=4,column=1,padx=5,pady=5)

per_lable=tk.Label(right_frame,text="Percent",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
per_lable.grid(row=5,column=0,padx=5,pady=5)
per_entry=tk.Entry(right_frame,textvariable=per,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
per_entry.grid(row=5,column=1,padx=5,pady=5)

grade_lable=tk.Label(right_frame,text="Grade",
                    bg=bg,font=("monotype corwas",25,'bold'),fg=fg)
grade_lable.grid(row=6,column=0,padx=5,pady=5)
grade_entry=tk.Entry(right_frame,textvariable=grade,
                    bg="white",font=("monotype corwas",20,'bold'),fg="black")
grade_entry.grid(row=6,column=1,padx=5,pady=5)

#create buttons

close = tk.Button(bottom_frame,text='Quit',font=font,bg=bg,fg=fg,command=close_window)
close.pack(side=tk.RIGHT,padx=5,pady=5)

clear = tk.Button(bottom_frame,text='Clear',font=font,bg=bg,fg=fg,command=clear_window)
clear.pack(side=tk.RIGHT,padx=5,pady=5)

calculation = tk.Button(bottom_frame,text='Calculation',font=font,bg=bg,fg=fg,command=calculation)
calculation.pack(side=tk.RIGHT,padx=5,pady=5)


root.mainloop()