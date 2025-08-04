def main():
    numero = int (input("digite um número:  "))


    i = 2

    while numero != i and numero != 1:
        if numero % i ==0:
            break
        i += 1

    if numero == i:
            print("O número", numero, "é primo")
    elif numero == 1:
            print("O número 1 não é primo")
    else:
          print("O número", numero,"não primo porque é divisivel por", i)


    return 0
main()