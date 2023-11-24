import tkinter as tk
from tkinter import Tk
import pyautogui as PAG
import random
from PIL import Image, ImageTk
from playsound import playsound
import threading


size = PAG.size()
running = True



# walktime = random.randint(1,4) # how long it takes to walk
# dirAngle = 45*random.randint(1,7) # 8 directions, 45deg angle per direction
# distance = random.randint(5,25) # how long the walk is

def create_transparent_overlay(width, height):
    # Create a fully transparent image
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    return ImageTk.PhotoImage(overlay)

def make_white_transparent(img):
    img = img.convert("RGBA")
    data = img.getdata()

    new_data = []
    for item in data:
        # If the pixel color is white, set alpha to 0 (transparent)
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    return img

def NuKörVi(): 
    global running
    

    window = tk.Tk()
    window.title('image viewer')
    x = 1000
    y = 800
    window.geometry('128x128+'+str(x)+'+'+str(y)) # second arg is the start pos x&y
    
    window.bind("<Escape>", lambda event: stop(event))
    window.bind("<Button-1>", lambda event: click(event))

    # Load images using Pillow
    pepe_run = [Image.open("../assets/pepe-running/pepe_r_0.png").convert("RGBA"),Image.open("../assets/pepe-running/pepe_r_1.png").convert("RGBA"),Image.open("../assets/pepe-running/pepe_r_2.png").convert("RGBA"),Image.open("../assets/pepe-running/pepe_r_3.png").convert("RGBA"),Image.open("../assets/pepe-running/pepe_r_4.png").convert("RGBA"),Image.open("../assets/pepe-running/pepe_r_5.png").convert("RGBA")]

    # target_color = (255, 255, 255)  # Adjust this to match the background color you want to make transparent

    # Create a Tkinter Canvas
    # canvas = tk.Canvas(window, width=128, height=128, highlightthickness=0)
    # canvas.pack()

    # Create a transparent overlay
    # overlay = create_transparent_overlay(128, 128)

    # Set transparent background for each image
    pepe_run = [make_white_transparent(img) for img in pepe_run]

    # Create a list of PhotoImage objects
    pepe_run_images = [ImageTk.PhotoImage(image) for image in pepe_run]

    def pepe_running(i):
        img.config(image=pepe_run_images[i])
        window.after(100, pepe_running, (i +1) % len(pepe_run_images))
    
    
    # img_path = "../assets/peepo.gif"
    img = tk.Label(window, image=pepe_run_images[0])
    img.pack()

    window.after(500, pepe_running, 1)

    
    # window.config(highlightbackground='blue')
    # label = tk.Label(window,bd=0,bg='blue')
    window.overrideredirect(True)
    window.attributes('-topmost', True)
   # window.wm_attributes('-transparentcolor',  'blue')
    
    walktime = 1 # how long it takes to walk
    dirAngle = 90 # 8 directions, 45deg angle per direction
    distance = 10 # how long the walk is
    move(window, walktime, dirAngle, distance)
    
    while running:
        window.update()
    window.destroy()
    
# stopevent 
def stop(event):
    global running
    running = False

# clickevent
def click(event):
    threading.Thread(target=playsound, args=('../assets/audio/huh.mp3',)).start()
   

# walking around logic

# get a new angle, a distance, and a walktime
def newMovement(window : Tk):
    # walktime = random.randint(1,4) # how long it takes to walk
    # dirAngle = 45*random.randint(1,7) # 8 directions, 45deg angle per direction
    # distance = random.randint(20,25) # how long the walk is
    walktime = 1 # how long it takes to walk
    dirAngle = 90 # 8 directions, 45deg angle per direction
    distance = 10 # how long the walk is
    window.after(100, move, window, walktime, dirAngle, distance) 
    
# fancy math, start a new movement
def move(window : Tk, walktime,  dir_angle, delta_distance, ):
    #delta_x = delta_distance * round(-1 * (walktime / 2) * 0.1 * round(10 * (1 if dir_angle < 180 else -1) * (1 - abs(((dir_angle + 180) % 360) - 180) / 180)))
    #delta_y = delta_distance * round(-1 * (walktime / 2) * 0.1 * round(10 * (1 if dir_angle < 180 else -1) * (1 - abs(((dir_angle + 90) % 360) - 90) / 90)))
    delta_x = delta_distance * round(-1 * (walktime / 2) * 0.1 * round(10 * (1 if dir_angle < 180 else -1) * (1 - abs(((dir_angle + 180) % 360) - 180) / 180)))
    delta_y = 0

    x = 1000
    y = 800
    window.geometry('128x128+' + str(x + delta_x) + "+"  + str(y + delta_y))
    
    # window.after(1000, move, window, walktime, dir_angle, delta_distance)
        

NuKörVi() 