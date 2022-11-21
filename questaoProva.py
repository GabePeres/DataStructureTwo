def Grep(Arquivo, Palavra):
    Contador = 0
    Final = 0
    Matriz = []
    Pos = 0

    Entrada = open("entrada.txt","r")
    Entrada.seek(0,0)                                           
    while Final == 0:
        Linha1 = (Entrada.readline())  
        if Linha1 != '':           
            Linha1 = Linha1.replace('\n', '') 
            LinhaSlipt = Linha1.split()
            Pos = Pos + 1    
            for Pal in LinhaSlipt:
                if(Pal == Palavra):
                    Contador = Contador + 1
                    Matriz.append('Linha: '+str(Pos)+' - '+Linha1)
        else:
            Final = 1 
            return Contador, Matriz
    Entrada.close()   

Arquivo = "entrada.txt"
Palavra = "know"
ContPalavra, LinhasPalavra = Grep(Arquivo,Palavra) 

print('A palavra "',Palavra,'" foi encontrada',ContPalavra,'veze(s)')
print('Palavra encontrada em:')
print('')
for x in LinhasPalavra:
    print(x)