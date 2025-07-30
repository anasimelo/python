def main():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade:"))
    peso = float(input("digite o seu peso:"))
    isEmpregado = input("vc possui um emprego? ")

    print("O", nome, "tem", idade, "anos de idade,pesa",peso)

    if isEmpregado:
        print("ele possui um emprego")
    else :
        print("ele não possui emprego")  

    return 0
main()