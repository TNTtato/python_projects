from cgi import print_arguments
from curses import window
import tkinter

def saludar(event):
  print('clico saludar')

def saludarDoble(event):
  print('Saluda doble'*2)

win = tkinter.Tk()

btn = tkinter.Button(win,
      text='Haz click'
)
btn.bind('<Button-1>', saludar)
btn.bind('<Double-1>', saludarDoble)
btn.pack()

win.mainloop()