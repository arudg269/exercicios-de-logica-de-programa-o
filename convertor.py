num = int(input("Enter a number: "))
print ("escolha a base para conversão:")
print ("1 - Binário")
print ("2 - Octal")
print ("3 - Hexadecimal")
opçao = int(input("Digite a opção: "))
if opçao == 1:
    print ("O número {} em Binário é: {}".format(num, bin(num)[2:]))
elif opçao == 2:
    print ("O número {} em Octal é: {}".format(num, oct(num)[2:]))
elif opçao == 3:
    print ("O número {} em Hexadecimal é: {}".format(num, hex(num)[2:]))
else:
    print ("Opção inválida")
    