qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    #Entrada de Valores
    valor = float(input("Digite um valor"))

#Caso digite um valor negativo o laço se encerra
media = soma / qtd
print("\n Total da Soma:", soma)
print("\n Quantidade  de valores  digitados:", qtd)
print("\n Média de valores:", media)
