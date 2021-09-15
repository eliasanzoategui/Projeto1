import math
import os
import ClassesDeRede



def procurar(nome, valores):
    for i in valores:
        if i.nome == nome:
            return i

def decodificarValores(texto):
    valores = []
    nome = ''
    nomeFinal = ''
    valor = ''
    add = False
    for i in texto:
        if i == ']':
            add = False
            valores.append(ValorNoArquivo(nomeFinal, valor))
            nome = ''
            valor = ''
            nomeFinal = ''
            valor = ''
        elif i == '[':
            add = True
            nomeFinal = nome
            nome = ''
        else:
            if add:
                valor += i
            else:
                nome += i

    return valores

def codificarValores(valores):
    cod = ''
    try:
        for i in valores:
            cod += i.codificar()
    except:
        cod = ''
    return cod

class ValorNoArquivo():
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    def codificar(self):
        return str(self.nome) + '[' + str(self.valor) + ']'
    def mudarValor(self, novoValor):
        self.valor = novoValor


def decodificarRedeNeural(texto):
    rede = []
    camada = []
    neuronio = []
    pesos = []
    bias = 0
    seletor = 'peso'
    valor = ''
    for caractere in texto:
        if caractere == 'p':
            seletor = 'peso'
        elif caractere == 'B':
            tipo = 'bolean'
        elif caractere == 'S':
            tipo = 'soma'
        elif caractere == 'r':
            red = ClassesDeRede.Rede()
            red.receber(camada)
            rede.append(red)
            camada = []
        elif caractere == 'c':
            cam = ClassesDeRede.Camada()
            cam.receber(neuronio)
            camada.append(cam)
            neuronio = []
        elif caractere == 'w':
            pesos.append(float(valor))
            valor = ''
        elif caractere == 'z':
            bias = float(valor)
            valor = ''
        elif caractere == 'b':
            seletor = 'bias'
        elif caractere == 'n':
            neu = ClassesDeRede.Neuron()
            neu.receber(pesos, bias)
            neuronio.append(neu)
            pesos = []
            bias = 0 
        else:
            if seletor == 'peso':
                valor += caractere
            if seletor == 'bias':
                valor += caractere
    return rede


def codificarNeuronio(neuronio):
    saida = 'p'
    for peso in neuronio.pesos:
        saida += str(peso) + 'w'
    saida += 'b' + str(neuronio.bias) + 'zn'
    return saida

def codificarCamada(camada):
    saida = ''
    for neuronio in camada.neuronios:
        saida += codificarNeuronio(neuronio)
    saida += 'c'
    return saida

def codificarRede(rede):
    saida = ''
    for camada in rede.camadas:
        saida += codificarCamada(camada)
    saida += 'r'
    return saida

def codificarRedes(redes):
    saida = ''
    for i in redes:
        saida += codificarRede(i)
    return saida

def seExisteValor(arquivos, nome):
    if procurar(nome, arquivos) != None:
        return True
    else:
        return False

class UnidadeDeSaveELoad():
    def __init__(self, caminho, numero):
        self.caminho = caminho
        self.numero = numero
    def criar(self):
        arq = open(self.gerarBanco(), 'w')
        arq.write('')
        arq.close()
    def salvarValores(self, valores):
        arquivo = open(self.gerarBanco(), 'w')
        arquivo.write(codificarValores(valores))
        arquivo.close()
    def retornarValor(self, nome):
        nome = str(nome)
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if seExisteValor(arquivos, nome):
            return procurar(nome, arquivos).valor
    def gerarBanco(self):
        return self.caminho + '\\banco_' + str(self.numero) + '.txt'
    def carregar(self):
        return decodificarValores(open(self.gerarBanco()).read())
    def salvarValor(self, nome, valor):
        nome = str(nome)
        valor = str(valor)
        arquivos = self.carregar()
        if arquivos == None:
            arquivos = []
        if seExisteValor(arquivos, nome):
            arquivo = procurar(nome, arquivos)
            arquivo.mudarValor(valor)
        else:
            arquivo = ValorNoArquivo(nome, valor)
            arquivos.append(arquivo)
        self.salvarValores(arquivos)
        


