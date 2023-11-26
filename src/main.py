import tkinter as tk
from random import randint
import playsound
import threading
import pyautogui as PAG
import time

size = PAG.size()
running = True
delta_x_accumulated = 0

class Ket:
    def click(self, event):
        threading.Thread(target=playsound.playsound, args=('../assets/audio/huh.mp3',)).start()

    def stop(self, event):
        global running
        running = False
        self.window.destroy()

    def __init__(self):
        global running  # Declare running as a global variable
        global delta_x_accumulated
        running = True
        self.window = tk.Tk()

        self.idle = [tk.PhotoImage(file='../assets/pepe-running/pepe_r_0.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_1.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_3.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_4.png'),
                     tk.PhotoImage(file='../assets/pepe-running/pepe_r_5.png')]

        self.x = round(size.width /2)
        self.y = round(size.height /2)
        self.window.geometry('128x128+{}+{}'.format(self.x, self.y))

        self.i_frame = 0
        self.state = 1
        self.event_number = 1

        self.frame = self.idle[0]

        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window, bd=0, bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparent', True)

        self.window.bind("<Escape>", lambda event: self.stop(event))
        self.window.bind("<Button-1>", lambda event: self.click(event))

        self.label.pack()
        
        walktime = 1 # how long it takes to walk
        dirAngle = 90 # 8 directions, 45deg angle per direction
        distance = 10 # how long the walk is
        self.move(walktime, dirAngle, distance)

        self.window.after(1, self.update)
        self.window.mainloop()
        

    def event(self):
        if running:
            self.window.after(100, self.update)

    def update(self):
        if running:
            self.frame = self.idle[self.i_frame]
            self.i_frame = self.animate(self.idle)

            self.label.configure(image=self.frame)
            self.window.after(1, self.event)

    def animate(self, array):
        if self.i_frame < len(array) - 1:
            self.i_frame += 1
        else:
            self.i_frame = 0
        return self.i_frame
    
    def move(self, walktime, dirAngle, deltaDistance):
        global delta_x_accumulated
        
        delta_x = self.calculate_delta_x(walktime, dirAngle, deltaDistance)
        delta_y = 0
        delta_x_accumulated += delta_x
             
        x = round((size.width / 2) + delta_x_accumulated)
        y = round((size.height / 2) + delta_y)

        self.window.geometry('128x128+{}+{}'.format(x, y))
                
        self.window.after(100, self.move, walktime, dirAngle, deltaDistance)

    def calculate_delta_x(self, walktime, dirAngle, deltaDistance):
        current_time = time.time()
        delta_x = deltaDistance * (
            (walktime / 2)
            * 0.1
            * round(
                10 * (1 if dirAngle < 180 else -1)
                * (1 - abs(((dirAngle + 180) % 360) - 180) / 180)
            )
            * (current_time % 10)
        )
        return delta_x

ket = Ket()
