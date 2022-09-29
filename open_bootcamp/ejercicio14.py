from select import select
import tkinter

win = tkinter.Tk()
selection = tkinter.StringVar()

def createList():
  global selection, win
  frame = tkinter.Frame(win)

  r1 = tkinter.Radiobutton(frame,
      text='option 1',
      activeforeground='blue',
      value='value 1',
      variable=selection
  )
  r1.pack()
  r2 = tkinter.Radiobutton(frame,
      text='option 2',
      activeforeground='blue',
      value='value 2',
      variable=selection
  )
  r2.pack()
  r3 = tkinter.Radiobutton(frame,
      text='option 3',
      activeforeground='blue',
      value='value 3',
      variable=selection
  )
  r3.pack()
  r4 = tkinter.Radiobutton(frame,
      text='option 4',
      activeforeground='blue',
      value='value 4',
      variable=selection
  )
  r4.pack()
  return frame

def reboot():
  global win
  win.destroy()
  createList()

frame = createList()
btn_reboot = tkinter.Button(win,
      text='Reboot',
      command=reboot
)
btn_reboot.pack()
win.mainloop()