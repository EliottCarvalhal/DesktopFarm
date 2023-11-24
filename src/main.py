import tkinter as tk
import pyautogui as PAG


def test(): 
    window = tk.Tk()
    window.title('image viewer')

    img_path = "../assets/peepo.gif"
    img = tk.PhotoImage(file=img_path)
    
    label = tk.Label(window, image=img)
    label.pack() 
    
    window.config(highlightbackground='black')
    label = tk.Label(window,bd=0,bg='black')
    window.overrideredirect(True)
    window.attributes('-topmost', True)
    window.wm_attributes('-alpha')
    
    window.mainloop()

test()