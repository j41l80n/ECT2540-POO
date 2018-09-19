num = [2, 5, 9, 1]
num.append(7)

# reverso 
# num.sort(reverse=True)

# indice ~ valor
num.insert(2, 0)

num.sort()

# elimina o ultimo elemento ~ pode-se passar o valor do indice a ser removido
# num.pop()

# procura a primeira ocorrencia do valor e remove
# num.remove(2)

if 5 in num:
	num.remove(5)
else:
	print('não achei o numero 5')

print(num)
print(f'essa lista tem {len(num)} elementos.')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
	print(f'na posicao {c} encontrei o valor {v}.')


a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'lista a: {a}')
print(f'lista b: {b}')

pessoas = list()
