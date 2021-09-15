import random
import scriptDeExecuçãoDeRede as ser
import math

class Ser():
    def __init__(self):
        pass

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

def retornarErros(rede, entradas, resultados):
	erro = 0
	for valor in range(0, len(entradas)):
		erro += somaDosErros(rede.processar(entradas[valor]), resultados[valor])
	return erro

class Knot():
	def __init__(self):
		pass
	def receberValor(self, novoValor):
		self.valor = novoValor
		return self
	def retornarValor(self):
		return self.valor

class Neuron():
	def processar(self, entrada):
		saida = 0
		for i in range(0, len(self.pesos)):
			saida += self.pesos[i] * entrada[i]
		saida += self.bias
		#if saida > 0:
		#	return 1
		#else:
		#	return 0
		return sigmoid(saida)
	def receber(self, pesos, bias):
		self.pesos = pesos
		self.bias = bias
		return self
	def gerar(self, pesos):
		self.pesos = []
		for i in range(pesos):
			self.pesos.append(random.randint(-1000, 1000) / 100) 
		self.bias = random.randint(-1000, 1000) / 100
		return self
	def taxa(self, taxa):
		for i in range(0, len(self.pesos)):
			self.pesos[i] +=  random.randint(-100, 100) / 10 * taxa
		self.bias += random.randint(-100, 100) / 10 * taxa
	def aleatoriar(self):
		for i in range(0, len(self.pesos)):
			self.pesos[i] = (random.randint(-1000, 1000) / 100)
			self.bias = (random.randint(-1000, 1000) / 100)





class Camada():
	def receber(self, neuronios):
		self.neuronios = neuronios
		return self
	def gerar(self, neuronios, entradas):
		self.neuronios = []
		for i in range(neuronios):	
			self.neuronios.append(Neuron().gerar(entradas))
		return self
	def processar(self, entrada):
		saidas = []
		for i in range(0, len(self.neuronios)):
			saidas.append(self.neuronios[i].processar(entrada))
		return saidas
	def taxa(self, taxa):
		for i in self.neuronios:
			i.taxa(taxa)
	def aleatoriar(self):
		for i in self.neuronios:
			i.aleatoriar()

class Rede():
	def receber(self, camadas):
		self.camadas = camadas
		return self
	def gerar(self, camadas, entrada):
		self.camadas = [Camada().gerar(camadas[0], entrada)]
		self.entrada = entrada
		for i in range(1, len(camadas)):
			self.camadas.append(Camada().gerar(camadas[i], camadas[i - 1]))
		return self
	def processar(self, entrada):
		saidas = self.camadas[0].processar(entrada)
		for i in range(1, len(self.camadas)):
			saidas = self.camadas[i].processar(saidas)
		return saidas
	def taxa(self, taxa):
		for i in self.camadas:
			i.taxa(taxa)
	def aleatoriar(self):
		for i in self.camadas:
			i.aleatoriar()
	def retornarErros(self, entradas, resultados):
		erro = 0
		for i in range(len(entradas)):
			erro += somaDosErros(self.processar(entradas[i]), resultados[i])
		return erro



class RedeNeuralRecorrente():
	def receberRede(self, rede, saidas):
		self.rede = rede
		self.saidas = saidas
		self.entradas = len(self.rede.camadas[0].neuronios[0].pesos)
		return self
	def gerar(self, camadas, entradas, saidas):
		self.rede = Rede().gerar(camadas + [saidas], entradas + saidas)
		self.saidas = saidas
		self.memoria = [0] * self.saidas
		self.entradas = entradas
		return self
	def processar(self, valores):
		memoria = [0] * self.saidas
		for i in valores:
			saida = self.rede.processar(i + memoria)
			memoria = saida
		return saida
	def treinar(self, entradas, resultados):
		self.rede = ser.treinar(self.rede, entradas, resultados)
	def zerar(self):
		self.memoria = [0] * self.saidas
	def retornarRede(self):
		return self.rede
	def taxa(self):
		self.rede.taxa(1)
	def aleatoriar(self):
		self.rede.aleatoriar()


def sumLista(lista):
	valores = []	
	for valor in lista:
		valores.append(valor)
	return valores

def positivo(x):
	if x < 0:
		x= -x
	return x

def somaDosErros(saidas, resultados):
	erro = 0
	for i in range(0, len(resultados)):
		erro += positivo(saidas[i] - resultados[i])
	return erro




