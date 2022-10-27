# Nome aluno, notas e condição para notas 

nome = input("Digite seu nome: ")
nota = float(input("Qual sua nota(0 a 10): "))


if (nota == 10):
  print(f"Parabéns {nome} você é o bichão mesmo")

elif (nota >= 6 and nota < 10):
  print(f"Ta bom, mas pode melhor né {nome}")

elif (nota > 10 ):
  print(f"Nem existe essa nota doidão")

else : 
  print(f"Burrão em {nome}")