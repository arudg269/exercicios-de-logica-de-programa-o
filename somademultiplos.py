soma = 0
for n in range(1, 501):
    if n % 2 == 0 and n % 3 == 0:
        soma += n
print("A soma dos múltiplos de 2 e 3 entre 1 e 500 é:", soma)