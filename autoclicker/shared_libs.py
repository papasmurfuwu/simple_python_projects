# Contains imported libraries and functions

import pyautogui, threading, time, tkinter
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