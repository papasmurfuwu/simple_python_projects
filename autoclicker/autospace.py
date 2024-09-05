import pyautogui, threading, customtkinter, keyboard, time
from tkinter import * 
from pynput import mouse


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.pause = pyautogui.PAUSE = 1

        self.title('Auto Clicker 1.0')
        self.minsize(400,200)

        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)

        label_font = ('Calibri', 12)
        self.vcmd = self.register(self.validate_input)
        

        # First row: User click interval input 
        self.input1 = customtkinter.CTkEntry(self, placeholder_text="0", justify="right", width=50, corner_radius=0, font=label_font, validate="key", validatecommand=(self.vcmd, '%P'))
        self.input1.grid(row=0, column=0, padx=(5, 0), pady=5)
        self.label1 = customtkinter.CTkLabel(self, text="Hours", font=label_font)
        self.label1.grid(row=0, column=1, padx=(5, 5), pady=5)

        self.input2 = customtkinter.CTkEntry(self, placeholder_text="0", justify="right", width=50, corner_radius=0, font=label_font, validate="key", validatecommand=(self.vcmd, '%P'))
        self.input2.grid(row=0, column=2, padx=(10, 0), pady=5)
        self.label2 = customtkinter.CTkLabel(self, text="Minutes", font=label_font)
        self.label2.grid(row=0, column=3, padx=(5, 5), pady=5)

        self.input3 = customtkinter.CTkEntry(self, placeholder_text="0", justify="right", width=50, corner_radius=0, font=label_font, validate="key", validatecommand=(self.vcmd, '%P'))
        self.input3.grid(row=0, column=4, padx=(10, 0), pady=5)
        self.label3 = customtkinter.CTkLabel(self, text="Seconds", font=label_font)
        self.label3.grid(row=0, column=5, padx=(5, 5), pady=5)

        self.input4 = customtkinter.CTkEntry(self, placeholder_text="0", justify="right", width=50, corner_radius=0, font=label_font, validate="key", validatecommand=(self.vcmd, '%P'))
        self.input4.grid(row=0, column=6, padx=(10, 0), pady=5)
        self.label4 = customtkinter.CTkLabel(self, text="Milliseconds", font=label_font)
        self.label4.grid(row=0, column=7, padx=(5, 5), pady=5)
        

        # Second row: Start & End buttons
        self.start_button = customtkinter.CTkButton(self, text='Start (Shift+C)', command=self.start_callback)
        self.start_button.grid(row=2, column=0, columnspan=4, padx=20, pady=20, sticky='ew')

        self.stop_button = customtkinter.CTkButton(self, text='Stop (Shift+C)', command=self.stop_callback)
        self.stop_button.grid(row=2, column=4, columnspan=4, padx=20, pady=20, sticky='ew')
        self.stop_button['state'] = 'disabled'

        keyboard.add_hotkey('shift+c', self.toggle_autoclicker) # Adding hotkey enables global detection 
        self.start = False

        
    def validate_input(self, P):
        if P == '' or (P.isdigit() and len(P) <= 6):
            return True
        return False
    

    def find_pause(self):
        # Get input values and convert to float, treating empty inputs as 0
        h = float(self.input1.get()) if self.input1.get() else 0.0
        m = float(self.input2.get()) if self.input2.get() else 0.0
        s = float(self.input3.get()) if self.input3.get() else 0.0
        ms = float(self.input4.get()) / 1000 if self.input4.get() else 0.0

        # Calculate total pause in seconds
        pause = (h * 3600) + (m * 60) + s + ms
        return pause


    def autoclick(self):
        while self.start:
            pyautogui.click() 
            

    def start_callback(self):
        self.pause = self.find_pause()
        pyautogui.PAUSE = self.pause
        
        print(f'Pause set to: {self.pause} seconds')
        print(f'Autoclicker activated!')

        self.start_time = time.time()
        
        self.start_button.configure(state=DISABLED)
        self.stop_button.configure(state=NORMAL)
        self.start = True
        threading.Thread(target=self.autoclick, daemon=True).start()


    def stop_callback(self):
        if self.start_time is not None:
            print(f'Elapsed time: {round(time.time() - self.start_time, 2)} seconds')

        print('Autoclicker turned off...')
        self.start_button.configure(state=NORMAL)
        self.stop_button.configure(state=DISABLED)
        self.start = False
        self.start_time = None  # Reset start_time when stopping


    def toggle_autoclicker(self):
        if not self.start:
            self.start_callback() 
        else:
            self.stop_callback()
            

if __name__ == '__main__':
    app = App()
    app.mainloop()

