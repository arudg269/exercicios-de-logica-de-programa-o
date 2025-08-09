ladoA = input("Digite o lado A do triângulo: ")
ladoB = input("Digite o lado B do triângulo: ")
ladoC = input("Digite o lado C do triângulo: ")
if ladoA == ladoB and ladoB == ladoC:
    print("O triângulo é equilátero")
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
num = int(input("Digite um número: "))

#regra para ser cada triangulo se os 3 numeros forem iguais é equilátero
#se dois forem iguais é isósceles
#se nenhum for igual é escaleno