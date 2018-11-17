import tkinter as tk

root = tk.Tk()

l0 = tk.Label(root, text='Label 0', bg='red')
l1 = tk.Label(root, text='Label 1', bg='green')
l2 = tk.Label(root, text='Label 2', bg='blue')
l3 = tk.Label(root, text='Label 3', bg='gray')

# método grid: informa o geometry manager em qual linha/coluna do master deseja posicionar widget
# (master é dividido em uma matriz)

l0.grid(row=0, column=0) 
l1.grid(row=1, column=0)
l2.grid(row=0, column=1)
l3.grid(row=1, column=1)

root.mainloop()