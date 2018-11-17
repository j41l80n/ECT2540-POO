import tkinter as tk

root = tk.Tk()

l0 = tk.Label(root, text='Nome:')
e0 = tk.Entry(root)
b0 = tk.Button(root, text='OK') # cria widget do tipo botão

l0.grid(row=0, column=0)
e0.grid(row=0, column=1)
b0.grid(row=1, columnspan=2, sticky=tk.E+tk.W) # sticky: cola a borda do widget na sua célula (quando esta é maior que o widget) 
                                               # (combinações de Norte-N, Sul-S, Leste-E, Oeste-W podem ser usadas)

root.mainloop()