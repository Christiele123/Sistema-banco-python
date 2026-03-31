notaA= float(input("Digite a primeira nota: "))
notaB= float(input("Digite a segunda nota: "))

#CALCULAR MEDIA
mediafinal=(notaA + notaB)/ 2
#verificação
if mediafinal >= 7.0:
    print("A Média: %.1f - Aprovado" % mediafinal)
else:
    print("A Média: %.1f - Reprovado" % mediafinal)
