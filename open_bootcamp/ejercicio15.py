from textwrap import fill
import tkinter as tk

def add():
  win_list.insert(tk.END, lang.get())

win = tk.Tk()
win.geometry("700x600+0+0")
win.title("Elementos seleccionables")
lbl_title = tk.Label(win,
      text='Lenguajes de programacion',
      bg='black',
      fg='white'
)
list_elements = tk.Variable(value=['Ruby', 'Python', 'JavaScript', 'C++', 'Java'])
win_list = tk.Listbox(win,
      bg='blue',
      fg='white',
      selectbackground='purple',
      listvariable=list_elements,
      height=3,
      selectmode=tk.EXTENDED
)
lbl_add_lang = tk.Label(win,
      text='Agrega un lenguaje: ',
      bg='gray',
      fg='black'
)
lang = tk.StringVar()
inp_lang = tk.Entry(win,
      fg='gray',
      textvariable=lang
)
btn_add_lang = tk.Button(win,
      text='Add',
      padx=5,
      pady=5,
      command=add
)
lbl_title.pack()
win_list.pack()
lbl_add_lang.pack()
inp_lang.pack()
btn_add_lang.pack()
win.mainloop()