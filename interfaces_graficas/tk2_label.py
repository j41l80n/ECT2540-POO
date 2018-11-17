import tkinter as tk

root = tk.Tk()
root.geometry("1024x500")
l = tk.Label(root, text='Ola TK!') # constroi widget do tipo label
l['fg'] = 'blue' # altera cor da fonte (fg = foreground)
l.config(bg='black') # altera cor do fundo (bg = background)
#l.bg por exemplo, não funciona
l.pack() # adiciona widget à sua janela pai

root.mainloop()