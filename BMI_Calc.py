from tkinter import *


root = Tk()
root.title('BMI Calculator')
root.configure(width=500,height=400,bg='black')


def calc():
	BMI = BMI_val(mass.get(),height.get())
	s_tat = get_status()
	stat.set(s_tat)
	bmi_val.set(format(BMI,'.2f'))


def BMI_val(mass,height):
	return mass/height**2



def get_height():
	return height

def clear():
	stat.set('')
	bmi_val.set('0.0')
	m_ass.delete(0,'end')
	h_eight.delete(0,'end')


def get_mass():
	return m_ass


def get_status():
	if bmi_val.get() > 40:
		return 'You are Obese class III.'
	elif bmi_val.get() > 35 and bmi_val.get() <= 40:
		return 'You are Obese class II.'
	elif bmi_val.get() > 30 and bmi_val.get() <= 35:
		return 'You are Obese class I.'
	elif bmi_val.get() > 25:
	 	return 'You are Overweight.'
	elif bmi_val.get() > 18.5 and bmi_val.get() <= 25:
		return 'You are Normal.'
	elif bmi_val.get() > 17 and bmi_val.get() <= 18.5:
		return 'You are Mildly Thin.'
	elif bmi_val.get() > 16 and bmi_val.get() <= 17:
		return 'You are Moderately Thin.'
	else: 
		return 'You are Severely Thin.'
	




height = DoubleVar()
height_label = Label(root,text='Height(meters)',fg='green',bg='black',font='Calibri 14 bold',
	                  pady=2,padx=8)
h_eight = Entry(root,textvariable=height)
height_label.grid(row=2)
h_eight.grid(row=2,column=1,columnspan=2,padx=5)

mass = DoubleVar()
mass_label = Label(root,text='Mass(kg)',fg='green',bg='black',font='Calibri 14 bold',
	                pady=10,padx=2)
m_ass = Entry(root,textvariable=mass)
mass_label.grid(row=4)
m_ass.grid(row=4,column=1)

bmi_val = DoubleVar()
stat = StringVar()
bmi = Label(root,text='BMI',fg='red',bg='black',font='Calibri 14 bold',
	         pady=2,padx=10,justify=LEFT)
status = Label(root,text='Status',fg='red',bg='black',font='Calibri 14 bold',
	            pady=10,padx=2)
status_msg = Label(root,textvariable=stat,fg='white',bg='black',font='Calibri 14 bold',
	                pady=10,padx=2)
BMI_total = Label(root,textvariable=bmi_val,fg='white',bg='black',font='Calibri 14 bold',
	              pady=10,padx=2)
bmi.grid(row=6)
status.grid(row=7)
BMI_total.grid(row=6,column=1)
status_msg.grid(row=7,column=1)

calculate = Button(root,text='Calculate',fg='white',bg='black',font='Calibri 12 bold',command=calc)
clear = Button(root,text='Reset',fg='white',bg='black',font='Calibri 14 bold',command=clear)
calculate.grid(row=8)
clear.grid(row=8,column=3)

root.mainloop()





