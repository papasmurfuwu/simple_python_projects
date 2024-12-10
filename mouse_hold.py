import pyautogui
import keyboard

# Variable to track the mouse button state
mouse_down = False

def toggle_mouse():
    global mouse_down
    if mouse_down:
        pyautogui.mouseUp()  # Release the mouse button
        print("Mouse released")
    else:
        pyautogui.mouseDown()  # Hold the mouse button down
        print("Mouse held down")
    mouse_down = not mouse_down  # Toggle the state

# Set up a hotkey for Ctrl + C
keyboard.add_hotkey('shift+c', toggle_mouse)

print("Press Shift + C to toggle mouse hold. Press ESC to exit.")
keyboard.wait('esc')  # Wait until the ESC key is pressed