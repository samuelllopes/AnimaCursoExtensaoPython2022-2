## Aula 3 - Laços

contador = 1

while(contador <= 1):
  print(contador)
  contador = contador +1

#criação de funções

preco = 2380.98

#Calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 1
print(imposto)

preco2 = 60
imposto2 = preco2 * 2
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
  
preco = 299
imposto = calcular_imposto(preco)
print(imposto)
