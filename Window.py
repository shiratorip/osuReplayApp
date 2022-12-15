import tkinter as tk
from tkinter import filedialog as fd, ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from RpReader import getGraf
root = tk.Tk()
root.title("osu! replay grafs")
root.geometry('800x400')

def do_plot(x, y):
    ax.clear()
    ax.plot(x,y)
    canvas.draw()

frame1 = tk.Frame(root); frame1.place(x=100, y=0, width=500, height=400)
figure = plt.Figure(figsize=(5,5), dpi=100)
canvas = FigureCanvasTkAgg(figure, frame1)
canvas.get_tk_widget().place(x=0,y=0,width=500,height=400)
ax = figure.add_subplot(111)

def select_file():
    filetypes = (
        ('osu! replay files', '*.osr'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    do_plot(getGraf(filename)[0],getGraf(filename)[1])


# open button
open_button = ttk.Button(
    master = root,
    text='Open a File',
    command=select_file
)


def showHPGraph():
    pass
def showReplayData():
    pass
def showMapData():
    pass
def showPlayerData():
    pass

buttonHP=ttk.Button(
    master=root,
    command=showHPGraph()
)
buttonReplayData=ttk.Button(
    master=root,
    command=showReplayData()
)
buttonMapData=ttk.Button(
    master=root,
    command=showMapData()
)
buttonPlayerData=ttk.Button(
    master=root,
    command=showPlayerData()
)

open_button.pack()
open_button.place(x=0,y=0)

buttonHP.pack()
buttonHP.place(x=0,y=20)



root.mainloop()