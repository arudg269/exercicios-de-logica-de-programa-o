peso = float(input("Digite qual o seu peso: "))
altura = float(input("Digite qual a sua altura: "))
imc = peso / (altura ** 2)

if imc < 0:
    print("Valor inválido")
elif imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")