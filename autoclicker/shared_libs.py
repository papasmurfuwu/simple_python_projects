# Contains imported libraries and functions
import pyautogui, threading, time, customtkinter
from tkinter import * 
from pynput import mouse


running = True 
pyautogui.PAUSE = 0.01 # Lower this for less delay (faster clicks)

def on_click(x, y, button, pressed):
    global running                                                                                                                                                                                 
    if pressed and (button == mouse.Button.left): # Check for pressed left click                                                                                    
        if on_click.last_click_time and (time.time() - on_click.last_click_time) < 0.25:     
            print("Double click detected! Terminating script.")
            running = False
        on_click.last_click_time = time.time()

def autospace(): 
    # Initialize last click time
    on_click.last_click_time = None             

    # Start listening to mouse events
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Main script loop
    # pyautogui.moveTo(1920, 720)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    while running:
        pyautogui.press(' ') # press spacebar 
            
    listener.stop()
    print("Script terminated.")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Auto Clicker 1.0')
        self.minsize(400,200)

        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Label "Click Interval"

        self.start_button = customtkinter.CTkButton(self, text='Start', command=self.autoclick_callback)
        self.start_button.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.stop_button = customtkinter.CTkButton(self, text='Stop', command=self.stop_callback)
        self.stop_button.grid(row=0, column=1, padx=20, pady=20, sticky='ew')
        
        self.bind('<C>', self.shift_c_pressed)
        self.start = False

    def autoclick_callback(self):
        print(f'Autoclicker activated!')
        self.start_button.configure(state=DISABLED)
        self.stop_button.configure(state=NORMAL)
        self.start = True

    def stop_callback(self):
        print('Autoclicker turned off...')
        self.start_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)
        self.start = False

    def shift_c_pressed(self, event):
        if not self.start:
            self.autoclick_callback()
            
        else:
            self.stop_callback()
            



    
    
   


if __name__ == '__main__':
    app = App()
    app.mainloop()

