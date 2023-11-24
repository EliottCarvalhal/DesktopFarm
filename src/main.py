import tkinter as tk
from win32api import GetMonitorInfo, MonitorFromPoint
from random import randint
import playsound
import threading

running = True


class Ket:
    def click(self, event):
        threading.Thread(target=playsound.playsound, args=('../assets/audio/huh.mp3',)).start()

    def stop(self, event):
        global running
        running = False
        self.window.destroy()

    def __init__(self):
        global running  # Declare running as a global variable
        running = True
        self.window = tk.Tk()

        self.idle = [tk.PhotoImage(file='../assets/pepe-running/pepe_r_0.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_1.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_3.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_4.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_5.png')]
        self.x = 1400
        self.y = 770

        self.i_frame = 0
        self.state = 1
        self.event_number = 1

        self.frame = self.idle[0]

        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window, bd=0, bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'black')

        self.window.bind("<Escape>", lambda event: self.stop(event))
        self.window.bind("<Button-1>", lambda event: self.click(event))

        self.label.pack()

        self.window.after(1, self.update)
        self.window.mainloop()

    def event(self):
        if running:
            self.window.after(100, self.update)

    def update(self):
        if running:
            self.frame = self.idle[self.i_frame]
            self.i_frame = self.animate(self.idle)

            self.window.geometry('128x128+' + str(self.x) + '+' + str(self.y))
            self.label.configure(image=self.frame)
            self.window.after(1, self.event)

    def animate(self, array):
        if self.i_frame < len(array) - 1:
            self.i_frame += 1
        else:
            self.i_frame = 0
        return self.i_frame


ket = Ket()
