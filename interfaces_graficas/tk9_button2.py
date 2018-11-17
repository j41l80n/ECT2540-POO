import tkinter as tk

def imprime_ok():
    print('OK pressionado')

root = tk.Tk()

l0 = tk.Label(root, text='Nome:')
e0 = tk.Entry(root)
b0 = tk.Button(root, text='OK', command=imprime_ok) # adiciona callback: função/método a ser chamado quando evento ocorre

l0.grid(row=0, column=0)
e0.grid(row=0, column=1)
b0.grid(row=1, columnspan=2, sticky=tk.E+tk.W)

root.mainloop()