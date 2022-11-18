import sorting
#==============================Estrutura=Heroi=====================================
class Professor:
    def __init__(self):
        self.id = []
        self.nome = []
        self.sexo = []
        self.idade = []
        self.area = []
        self.telefone = []
        
    def setHeroi(self, id, nome, sexo, idade, area, telefone):
        self.id.append(id)
        self.nome.append(nome)
        self.sexo.append(sexo)
        self.idade.append(idade)
        self.area.append(area)
        self.telefone.append(telefone)
        self.n = self.n + 1

    def buscalinear(self,chave):
        for i in range(0,self.n,1):
            if self.id[i] == chave:
                return i 
        return -1 

    def getNome(self, n):
        return (self.nome[n])

    def getProfessor(self, n):
        return (self.id[n]+'|'+self.nome[n]+'|'+self.sobrenome[n]+'|'+self.apelido[n]+'|'+self.poder[n]+'|'+self.vulneravel[n]+'|'+self.origem[n]+'|'+self.profissao[n])
#==============================Tratammento-do-Arquivo==============================
Entrada = open("input1.txt",'r')
Entrada.seek(0,0)                                                                  #Cursor no inicio do arquivo

LinhaArquivo = (Entrada.readline()).replace('\n', '')  
if (LinhaArquivo == '' or LinhaArquivo == ' '):                                    #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Arquivo Vazio!')
  exit()
#==============================Tratammento-do-Cabecalho============================
CabecalhoArqSaida = LinhaArquivo
Cabecalho = LinhaArquivo.split()
VetCabecalho = []

for x in Cabecalho:
    Valor = x.split('=')
    VetCabecalho.append(Valor[1])
#==============================Tratammento-de-Registros============================
Registro = Professor()
VetorElementos = []     
for y in range(int(VetCabecalho[2])):
    LinhaArquivo = (Entrada.readline()).replace('\n', '') 
    if (LinhaArquivo == ''):                                                           #Verifica se o arquivo esta vazio
        print('ERRO -> Não há registro no arquivo')
        exit() 
    LinhaArquivo = LinhaArquivo.split('|')
    VetorElementos.append(LinhaArquivo[0])
    Registro.setHeroi(id=LinhaArquivo[0], nome=LinhaArquivo[1], sexo=LinhaArquivo[2], idade=LinhaArquivo[3], area=LinhaArquivo[4])  
#==============================Escrita-Ordenada-Saida==============================
Saida = open("Saida.txt",'w')
Saida.seek(0,0)                                                                    #Cursor no inicio do arquivo
Saida.write(CabecalhoArqSaida)

Entrada.close()
Saida.close()    
