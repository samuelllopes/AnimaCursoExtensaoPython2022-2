# Projeto Python - Extensão 

# input()

nome = input("Digite seu nome: ")
idade = int(input("Qual sua idade: "))
sexo = input("Informe seu gênero: (SENDO M = MASCULINO E F = FEMININO) ")

print(f"Boa Noite, seu nome é {nome} e você tem {idade} anos.")

dobro = idade * 2
print(f"O dobro da sua idade é {dobro}.")

# Condicional 


if (idade >= 18 and sexo == "M"):
  print("Você é um Homem e tem mais de 18 anos, pode servir o serviço obrigatorio(caso não tenha servido)")
  
else :
   print("Você é Mulher ou tem menos de 18, não precisa servir o serviço obrigatorio")

