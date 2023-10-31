vropt = input("""Selecione uma operação: \n
              + Soma
              - Subtração
              * Multiplicação
              / Divisão
              x Sair
              \n""")

print("Você escolheu: ",vropt)

v1 = int(input("\nEntre com o primeiro valor: "))
v2 = int(input("\nEntre com o segundo valor : "))

match vropt:
    case "+":
        print(v1," + ",v2," = ", v1+v2)
    case "-":
        print(v1," - ",v2," = ", v1-v2)
    case "*":
        print(v1," * ",v2," = ", v1*v2)
    case "/":
        print(v1," / ",v2," = ", v1/v2)    