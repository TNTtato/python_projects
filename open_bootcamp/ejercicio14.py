from tkinter import Tk, StringVar, Radiobutton, Label, Button, W

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="Option 1", variable=opcion, 
            value='Value 1', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Option 2", variable=opcion, 
            value='Value 2', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Option 3", variable=opcion,   
            value='Value 3', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Option 4", variable=opcion,   
            value='Value 4', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()