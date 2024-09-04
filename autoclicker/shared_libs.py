# Contains imported libraries and functions
import pyautogui, threading, time, customtkinter, keyboard
from tkinter import * 
from pynput import mouse


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Auto Clicker 1.0')
        self.minsize(400,200)

        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Label "Click Interval"

        self.start_button = customtkinter.CTkButton(self, text='Start (Shift+C)', command=self.start_callback)
        self.start_button.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.stop_button = customtkinter.CTkButton(self, text='Stop (Shift+C)', command=self.stop_callback)
        self.stop_button.grid(row=0, column=1, padx=20, pady=20, sticky='ew')
        self.stop_button['state'] = 'disabled'

        keyboard.add_hotkey('shift+c', self.toggle_autoclicker)
        self.start = False


    def autoclick(self):
        while self.start:
            pyautogui.click(interval=0.00001)
            

    def start_callback(self):
        print(f'Autoclicker activated!')
        self.start_button.configure(state=DISABLED)
        self.stop_button.configure(state=NORMAL)
        self.start = True
        threading.Thread(target=self.autoclick, daemon=True).start()


    def stop_callback(self):
        print('Autoclicker turned off...')
        self.start_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)
        self.start = False


    def toggle_autoclicker(self):
        if not self.start:
            self.start_callback() 
        else:
            self.stop_callback()
            

if __name__ == '__main__':
    app = App()
    app.mainloop()

