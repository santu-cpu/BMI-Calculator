from tkinter import *


root = Tk()
root.title('BMI Calculator')
root.configure(width=500,height=400,bg='black')


height = DoubleVar()
height_label = Label(root,text='Height',fg='green',bg='black',font='Calibri 14 bold',
	                  pady=2,padx=8)
h_eight = Entry(root,textvariable=height)
height_label.grid(row=2)
h_eight.grid(row=2,column=1,columnspan=2,padx=5)

mass = DoubleVar()
mass_label = Label(root,text='Mass',fg='green',bg='black',font='Calibri 14 bold',
	                pady=10,padx=2)
m_ass = Entry(root,textvariable=mass)
mass_label.grid(row=4)
m_ass.grid(row=4,column=1)

bmi_val = DoubleVar()
stat = StringVar()
bmi = Label(root,text='BMI',fg='blue',bg='black',font='Calibri 14 bold',
	         pady=2,padx=10,justify=LEFT)
status = Label(root,text='Status',fg='blue',bg='black',font='Calibri 14 bold',
	            pady=10,padx=2)
status_msg = Label(root,textvariable=stat,fg='white',bg='black',font='Calibri 14 bold',
	                pady=10,padx=2)
BMI_total = Label(root,text=bmi_val,fg='white',bg='black',font='Calibri 14 bold',
	              pady=10,padx=2)
bmi.grid(row=6)
status.grid(row=7)
BMI_total.grid(row=6,column=1)
status_msg.grid(row=7,column=1)





mainloop()