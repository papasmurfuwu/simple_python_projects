from shared_libs import autospace
from shared_libs import * 

root = tkinter.Tk()
root.minsize(300, 200)
root.eval('tk::PlaceWindow . center')

h1 = Label(root, text="Spacebar Autoclicker 1.0")
button = Button(text='Start',
                command=autospace)

h1.pack()
button.pack()
root.mainloop() 
                                                                                                               
pyautogui.PAUSE = 0.01 # Lower this for lower delay (faster clicks) 
# Flag to control the running state of the script
running = True



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              