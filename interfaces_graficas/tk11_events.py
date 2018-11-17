import tkinter as tk

def ev_mouse_esquerdo(event):
    print('Clique esq.: {}, {}'.format(event.x, event.y))

def ev_mouse_direito(event):
    tv.set('Clique dir.: {}, {}'.format(event.x, event.y))

def ev_mouse_movimento(event):
    # imprima dir(event) para saber as informações sobre as quais podemos ter acesso
    tv.set('Movimento sobre label2: {}, {}'.format(event.x, event.y))

def ev_mouse_esquerdo_label3(event):
    l3.focus_set() # atribui foco ao label3: necessário para eventos de teclado
    print('foco esta em label3')

def ev_tecla(event):
    tv.set('Tecla pressionada com foco em label3: {}'.format(event.char))

root = tk.Tk()

tv = tk.StringVar()
tv.set('Evento:')

l0 = tk.Label(root, text='Label0', bg='red')
l1 = tk.Label(root, text='Label1', bg='green')
l2 = tk.Label(root, text='Label2', bg='blue')
l3 = tk.Label(root, text='Label3', bg='yellow')
l4 = tk.Label(root, textvariable=tv)

l0.grid(row=0, column=0)
l1.grid(row=0, column=1)
l2.grid(row=1, column=0)
l3.grid(row=1, column=1)
l4.grid(row=2)

l0.bind('<Button-1>', ev_mouse_esquerdo)
l1.bind('<Button-3>', ev_mouse_direito)
l2.bind('<Motion>', ev_mouse_movimento)
l3.bind('<Button-1>', ev_mouse_esquerdo_label3)
l3.bind('<Key>', ev_tecla)

root.mainloop()