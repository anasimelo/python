from Div import div
from Mult import mult
from Soma import soma
from SUb import sub

def main():

    num1 = int (input("Digite seu primeiro número: "))
    num2 = int (input("Digite o segundo número: "))

    print("A soma de ", num1, "+", num2," = ", soma(num1, num2))
    print("A subtração de ", num1,  " = ", sub(num1, num2))
    print("A multiplicação de ", num1, "*", num2,"=", mult(num1, num2))
    print("A divisão de ", num1 " / ", num2, " = ", div(num1, num2))
  
    return 0
main()
