from tkinter import *

expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set("error")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

def backspace():
	global expression
	if len(expression) > 0:
		expression = expression[:-1]
		equation.set(expression)

def percentage():
	global expression
	try:
		expression = str(eval(expression) / 100)
		equation.set(expression)
	except:
		equation.set("error")
		expression = ""

def square():
	global expression
	try:
		expression = str(eval(expression) ** 2)
		equation.set(expression)
	except:
		equation.set("error")
		expression = ""

cal = Tk()
cal.configure(background="grey")
cal.title("Calculator")
cal.geometry("270x150")
equation = StringVar()
expression_field = Entry(cal, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

button1 = Button(cal, text=' 1 ', fg='white', bg='black',
					command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(cal, text=' 2 ', fg='white', bg='black',
					command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(cal, text=' 3 ', fg='white', bg='black',
					command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(cal, text=' 4 ', fg='white', bg='black',
					command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(cal, text=' 5 ', fg='white', bg='black',
					command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(cal, text=' 6 ', fg='white', bg='black',
					command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(cal, text=' 7 ', fg='white', bg='black',
					command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(cal, text=' 8 ', fg='white', bg='black',
					command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(cal, text=' 9 ', fg='white', bg='black',
					command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(cal, text=' 0 ', fg='white', bg='black',
					command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)

plus = Button(cal, text=' + ', fg='white', bg='black',
				command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(cal, text=' - ', fg='white', bg='black',
				command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(cal, text=' * ', fg='white', bg='black',
					command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(cal, text=' / ', fg='white', bg='black',
					command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

backspace_button = Button(cal, text='←', fg='white', bg='black',
                          command=backspace, height=1, width=7)
backspace_button.grid(row=1, column=3)

percentage_button = Button(cal, text=' % ', fg='white', bg='black',
						   command=percentage, height=1, width=7)
percentage_button.grid(row=1, column=0)

square_button = Button(cal, text=' x² ', fg='white', bg='black',
					   command=square, height=1, width=7)
square_button.grid(row=1, column=1)

equal = Button(cal, text=' = ', fg='white', bg='red',
				command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear_button = Button(cal, text='Clear', fg='white', bg='black',
					  command=clear, height=1, width=7)
clear_button.grid(row=1, column=2)

Decimal = Button(cal, text='.', fg='white', bg='black',
					command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=5, column=1)

cal.mainloop()
