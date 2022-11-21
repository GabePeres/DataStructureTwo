class Game:
  def __init__(self, Titulo=None, Produtora=None, Genero=None, Plataforma=None, Ano=None, Classificacao=None, Preco=None, Midia=None, Tamanho=None):
    self.Titulo = Titulo
    self.Produtora = Produtora
    self.Genero = Genero
    self.Plataforma = Plataforma
    self.Ano = Ano
    self.Classificacao = Classificacao
    self.Preco = Preco
    self.Midia = Midia
    self.Tamanho = Tamanho

  def setNome(self,Titulo):
    self.Titulo=Titulo

  def getNome(self):
    return (self.nome)

Entrada = open("Games.txt", 'r')
Saida   = open("GamesSaida.txt",'w')
aux = [Entrada.split('|')]
print(aux)
Saida.write(Entrada)
