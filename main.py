import tkinter as tk
from tkinter import ttk

HEADER1 = ("Arial", 24)
HEADER2 = ("Arial", 18)
PARAGRAPH = ("Arial", 12)

buttonBoard = []

def ClearWindow():
  global frm

  for widget in mainWindow.winfo_children(): # for each element in page
    widget.grid_remove()                     # destroy it
  
  frm = ttk.Frame(mainWindow, padding=10)
  frm.grid()

def OpenGameWindow():

  ClearWindow()         # removes all window elements

  for y in range(6):    # loop through eachh row
    row = []            # initalize row array
    for x in range(7):  # loop through each column
      row.append(tk.Button(frm, text=f"{x},{y}", command=mainWindow.destroy).grid(column=x, row=y)) # add a button in each slot

    buttonBoard.append(row) # add the row of buttons to the 2D button board array

def OpenPlayerSelect():
  tk.Label(frm, text="Connect 4", font=HEADER1).grid(column=1, row=1)

  tk.Button(frm, text="Play!", command=OpenGameWindow).grid(column=1, row=2)

  pass

mainWindow = tk.Tk()
mainWindow.title('Connect4')
mainWindow.geometry("920x540")

frm = ttk.Frame(mainWindow, padding=10)
frm.grid()

OpenPlayerSelect()

mainWindow.mainloop() # run window forever

