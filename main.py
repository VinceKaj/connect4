import tkinter as tk
from tkinter import font as tkfont 

from matplotlib.pyplot import gray

HEADER1 = ("Arial", 24)
HEADER2 = ("Arial", 18)
PARAGRAPH = ("Arial", 12)

buttonBoard = []
board = []

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)                              # initialize the main frame of the window
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)                # configure rows
        container.grid_columnconfigure(0, weight=1)             # configure columns

        self.frames = {}                                        # this list contains all frames
        for F in (PlayerSelect, GameWindow, WinWindow):         # foreach frame:
            page_name = F.__name__                              # store the name of the frame as a STRING
            frame = F(parent=container, controller=self)        # create a frame where container is the parent frame
            self.frames[page_name] = frame                      # add the frame to the frame list

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PlayerSelect") # load the first frame: the player selector

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class PlayerSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Connect 4", font=HEADER1).grid(column=2, row=1)
        tk.Label(self, text="Player select", font=HEADER2, fg="gray").grid(column=2, row=2)

        tk.Label(self, text="Gamemode", font=HEADER2).grid(column=1, row=3)

        # isPVP.get() = is PvP?
        isPVP = tk.IntVar(self, 1)
        tk.Radiobutton(self, text="Player vs Player", variable=isPVP, value=1).grid(column=1, row=4)
        tk.Radiobutton(self, text="Player vs Computer", variable=isPVP, value=0).grid(column=1, row=5)

        tk.Label(self, text="Player names", font=HEADER2).grid(column=3, row=3)

        tk.Button(self, text="Play!", command=lambda: controller.show_frame("GameWindow")).grid(column=2, row=4)


class GameWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        for y in range(6):    # loop through eachh row
          row = []            # initalize row array
          invisRow = []

          for x in range(7):  # loop through each column
            row.append(tk.Button(self, text=f"{x},{y}").grid(column=x, row=y)) # add a button in each slot
            invisRow.append(' ')

          buttonBoard.append(row) # add the row of buttons to the 2D button board array
          board.append(invisRow)


class WinWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This page is empty.", font=HEADER1).grid(column=1, row=1)
        button = tk.Button(self, text="Player Select", command=lambda: controller.show_frame("PlayerSelect"), font=HEADER1).grid(column=1, row=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
