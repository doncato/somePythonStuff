#! /usr/bin/env python
# name: Doncato
# date: 05-09-20
# description: calculator
# calc.py
# I know it's not the best way to design a Calculator

import random
import time
from tkinter import *
from tkinter import messagebox

# Generate Window
root = Tk()
root.title('Calculator')
root.resizable(False, False)
# Insert Line
e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Variables
state = 'none'

# Functions
def numberset(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def numberadd():
    global Num1
    global state
    frstNum = e.get()
    Num1 = int(frstNum)
    e.delete(0, END)
    state = 'add'
def numbersub():
    global Num1
    global state
    frstNum = e.get()
    Num1 = int(frstNum)
    e.delete(0, END)
    state = 'sub'
def numbermul():
    global Num1
    global state
    frstNum = e.get()
    Num1 = int(frstNum)
    e.delete(0, END)
    state = 'mul'
def numberdiv():
    global Num1
    global state
    frstNum = e.get()
    Num1 = int(frstNum)
    e.delete(0, END)
    state = 'div'
def numbersolve():
    scndNum = e.get()
    e.delete(0, END)
    if state == 'add':
        e.insert(0, Num1 + int(scndNum))
    if state == 'sub':
        e.insert(0, Num1 - int(scndNum))
    if state == 'mul':
        e.insert(0, Num1 * int(scndNum))
    if state == 'div':
        div = Num1 / int(scndNum)
        e.insert(0, int(div))
def clear():
    e.delete(0, END)
# Buttons
button1 = Button(root, text='1', padx=30, pady=10, command=lambda: numberset(1))
button2 = Button(root, text='2', padx=30, pady=10, command=lambda: numberset(2))
button3 = Button(root, text='3', padx=30, pady=10, command=lambda: numberset(3))
button4 = Button(root, text='4', padx=30, pady=10, command=lambda: numberset(4))
button5 = Button(root, text='5', padx=30, pady=10, command=lambda: numberset(5))
button6 = Button(root, text='6', padx=30, pady=10, command=lambda: numberset(6))
button7 = Button(root, text='7', padx=30, pady=10, command=lambda: numberset(7))
button8 = Button(root, text='8', padx=30, pady=10, command=lambda: numberset(8))
button9 = Button(root, text='9', padx=30, pady=10, command=lambda: numberset(9))
button10 = Button(root, text='0', padx=30, pady=10, command=lambda: numberset(0))

button11 = Button(root, text='+', padx=31, pady=10, command=numberadd)
button12 = Button(root, text='-', padx=32, pady=10, command=numbersub)
button13 = Button(root, text='*', padx=31, pady=10, command=numbermul)
button14 = Button(root, text='/', padx=33, pady=10, command=numberdiv)
button15 = Button(root, text='!', padx=32, pady=10, command=numbersolve)
button16 = Button(root, text='X', padx=30, pady=10, command=clear)

# Place Buttons

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button10.grid(row=4, column=0)

button11.grid(row=1, column=3)
button12.grid(row=2, column=3)
button13.grid(row=3, column=3)
button14.grid(row=4, column=3)
button15.grid(row=4, column=1)
button16.grid(row=4, column=2)


# End
print ('Running...')
root.mainloop()
