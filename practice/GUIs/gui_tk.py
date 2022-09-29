import tkinter as tk
from tkinter import ttk
import tkinter


#containers: frames y ventanas

win = tk.Tk() #window

# geometrias: pack, grid and place

#labels:
lbl_saludo = tk.Label(win,
      text='hola!', #text
      bg='yellow', # background
      fg='blue' # foreground
)

lbl_adios = tk.Label(win,
      text='adios',
      bg='green',
      fg='red'
)

lbl_side_r = tk.Label(win,
      text='Rigth side',
      bg='blue',
      fg='orange'
)
# con pack: ubicar elementos debajo o al lado de otros
lbl_saludo.pack(ipadx=50,
      ipady=50,
      fill='both',
      expand=True
) #inner paddig
lbl_side_r.pack(ipadx=50,
      ipady=130,
      fill='both',
      expand=True,
      side='right'
)
lbl_adios.pack(ipadx=50,
      ipady=80,
      fill='both',
      expand=True
)

#win.mainloop() #loop hasta cerrar

#geometria grid

win2 = tk.Tk()
win2.columnconfigure(0, weight=1)
win2.columnconfigure(1, weight=3)

username_lbl = ttk.Label(win2,
      text='Username: '
)
username_entry = ttk.Entry(win2)
username_lbl.grid(column=0,
      row=0,
      sticky=tk.W, 
      padx=5,
      pady=5
)
username_entry.grid(column=1,
      row=0,
      sticky=tk.E,
      padx=5,
      pady=5
)

password_lbl = ttk.Label(win2,
      text='Password: '
)
password_entry = ttk.Entry(win2,
      show='*'
)
password_lbl.grid(column=0,
      row=1,
      sticky=tk.W, 
      padx=5,
      pady=5
)
password_entry.grid(column=1,
      row=1,
      sticky=tk.E,
      padx=5,
      pady=5
)

logging_btn = ttk.Button(win2, 
      text='Log In')
logging_btn.grid(column=1,
      row=3,
      sticky=tk.E,
      padx=5,
      pady=5
)
#win2.mainloop()

#place: pos exacto abs o rela

win3 = tk.Tk()

lbl1 = tk.Label(win3,
      text='Pos Abs',
      bg='blue',
      fg='white'
)
lbl1.place(x=10, y=50)

lbl2 = tk.Label(win3,
      text='Pos Rela',
      bg='red',
      fg='white'
)
lbl2.place(relx=0.10,
      rely=0.150,
      anchor='ne'
)
win3.mainloop()