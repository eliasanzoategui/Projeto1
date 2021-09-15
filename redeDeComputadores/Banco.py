import scriptDeSaveELoad as ssl
import os

class UnidadeDeSaveELoad():
    def __init__(self, caminho, numero):
        self.caminho = caminho
        self.numero = numero
        if not ('banco_' + str(self.numero) + '.txt') in os.listdir(self.caminho):
            self.criar()
    def criar(self):
        arq = open(self.gerarBanco(), 'w')
        arq.write('')
        arq.close()
    def salvarValores(self, valores):
        arquivo = open(self.gerarBanco(), 'w')
        arquivo.write(ssl.codificarValores(valores))
        arquivo.close()
    def retornarValor(self, nome):
        nome = str(nome)
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            return ssl.procurar(nome, arquivos).valor
    def gerarBanco(self):
        return self.caminho + '\\banco_' + str(self.numero) + '.txt'
    def carregar(self):
        return ssl.decodificarValores(open(self.gerarBanco()).read())
    def salvarValor(self, nome, valor):
        nome = str(nome)
        valor = str(valor)
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if ssl.seExisteValor(arquivos, nome):
            arquivo = ssl.procurar(nome, arquivos)
            arquivo.mudarValor(valor)
        else:
            arquivo = ssl.ValorNoArquivo(nome, valor)
            arquivos.append(arquivo)
        self.salvarValores(arquivos)
        





