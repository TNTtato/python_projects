from random import sample, randint
import tkinter

colors = ['blue', 'red', 'yellow', 'purple', 'green']

win1 = tkinter.Tk()
for x in range(0, 1000):
  color1, color2 = sample(colors, 2)
  lbl = tkinter.Label(win1,
        text='label!',
        bg=color1,
        fg=color2
  )
  lbl.place(x=randint(0,150),
        y=randint(0, 180)
  )

win1.mainloop()