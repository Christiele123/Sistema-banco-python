arquivo = open('arqText.txt','w')
arquivo.write("Curso Python \n")
arquivo.close()

def lernotas():
    n=float(input("Digite uma nota para o Aluno: "))
    return n

def resultado(n1,n2):
    media=(n1+n2)/2
    print("Nota 1:",n1)
    print("Nota 2:",n2)
    print("Media:",media,"\nResultado: ",end="")
    if media > 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lernotas()
b = lernotas()
resultado(a,b)



