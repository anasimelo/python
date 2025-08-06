def main():
    inicio = int (input("Digite seu inicio do intervalo: "))
    fim = int (input("Digite o fim do intervalo: "))

    primos = "" 


    if inicio < fim:
      while inicio <= fim:
        i = 2

        while inicio > i:
           if inicio % i == 0:
            break
           i += 1

        if inicio == i and inicio > 1:
           primos += "\n" + str(inicio)

        inicio += 1
    elif inicio > fim:
        while inicio >= fim:
           
           i = 2

           while inicio != i and inicio > 1:
              if inicio % i == 0:
                 break
              i += 1

        if inicio == i and inicio > 1:
                primos += "\n" + str (inicio)
        inicio -= 1
    else:
        i = 2

        while inicio != i and inicio > 1:
           if inicio % i == 0:
              break
        i += 1
              
    if inicio == i and inicio > 1:
           primos += "\n" + str (inicio)
    if primos == "":
            primos += "intervalo sem primo"

    print("Primos: ", primos)
    return 0
main()