def main():
   tam = int (input("Digite a quantidade de alunos: "))
   notas = [0.0] * tam
   nomes = [""] * tam
   i = 0
   while i < tam:
      nomes[i] = input("Digite o nome do aluno: ")

      notas[i] = float (input( "Digite a nota do aluno: "))

      i += 1
      print("\n")

   i = 0 
    
   for i in range (len (nomes)):
        print("O aluno ", nomes[i], " tirou ",notas[i])

   return 0
main()