import tkinter as tk
from tkinter import filedialog as fd, ttk

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from RpReader import getGraf


class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("osu! replay grafs")
        self.geometry('800x400')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (HPbar, MapDataBar, ReplayDataBar, PlayerDataBar):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HPbar)

        def select_file():
            filetypes = (
                ('osu! replay files', '*.osr'),
                ('All files', '*.*')
            )

            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)
            do_plot(getGraf(filename)[0], getGraf(filename)[1])

        frame1 = tk.Frame(self.frames[HPbar])
        frame1.place(x=100, y=0, width=700, height=400)
        figure = plt.Figure(figsize=(5, 5), dpi=100)
        canvas = FigureCanvasTkAgg(figure, frame1)
        canvas.get_tk_widget().place(x=0, y=0, width=700, height=400)
        ax = figure.add_subplot(111)

        def do_plot(x, y):
           ax.clear()
           ax.plot(x, y)
           canvas.draw()

        # open button
        open_button = ttk.Button(
            master=self,
            text='Open a File',
            command=select_file
        )
        open_button.pack()
        open_button.place(x=0, y=0)

        buttonHP = ttk.Button(
            master=self,
            text='Hp Graf',
            command=lambda: self.show_frame(HPbar)
        )
        buttonHP.place(x=0, y=20)

        buttonReplayData = ttk.Button(
            master=self,
            text='Replay data',
            command=lambda: self.show_frame(ReplayDataBar)
        )
        buttonReplayData.place(x=0, y=40)

        buttonMapData = ttk.Button(
            master=self,
            text='Map Data',
            command=lambda: self.show_frame(MapDataBar)
        )
        buttonMapData.place(x=0, y=60)

        buttonPlayerData = ttk.Button(
            master=self,
            text='Player Data',
            command=lambda: self.show_frame(PlayerDataBar)
        )
        buttonPlayerData.place(x=0, y=80)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HPbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="start")



class MapDataBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 1")


class PlayerDataBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2")


class ReplayDataBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 3")


# buttonHP.pack()
# buttonHP.place(x=0,y=20)


app = tkinterApp()
app.mainloop()
