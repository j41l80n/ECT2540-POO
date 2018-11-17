import tkinter as tk

def atualiza_entrada():
    entrada0.set('Texto digitado: {}'.format(e0.get())) # Importante: entrada0 e e0 podem ser acessadas pois são variáveis globais

root = tk.Tk()

entrada0 = tk.StringVar() # StringVar: variável string do TK
entrada0.set('Texto digitado: ') # atribuição do valor

l0 = tk.Label(root, text='Nome:')
e0 = tk.Entry(root)
b0 = tk.Button(root, text='OK', command=atualiza_entrada)
l1 = tk.Label(root, textvariable=entrada0) # textvariable deve ser utilizado ao invés de texto

l0.grid(row=0, column=0)
e0.grid(row=0, column=1)
b0.grid(row=1, columnspan=2, sticky=tk.E+tk.W)
l1.grid(row=2, columnspan=2, sticky=tk.E+tk.W)

root.mainloop()