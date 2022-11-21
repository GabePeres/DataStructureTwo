def pesquisa(arq,str):
  index=0
  lista=[]
  for linha in arq:
    txt = arq.readline()
    nopipe = txt.split('|')
    #print(nopipe)
    index = index + 1
    if str.upper() in txt.upper():
      #print(index,': ',txt)
      lista.append((index,nopipe))
  return lista

arquivo = open("Games.txt","r")
print('Digite a pesquisa:')
entrada = input()
print(pesquisa(arquivo, entrada))
arquivo.close()