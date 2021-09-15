import scriptDeExecuçãoDeRede as ser
import ClassesDeRede as cr
import scriptDeSaveELoadDeRede as sslr

class Data():
	def __init__(self, entrada, resultado):
		self.entrada = entrada
		self.resultado = resultado
	def retornarEntrada(self):
		return self.entrada
	def retornarResultado(self):
		return self.resultado

def retornarDados(dados):
    entradas = []
    resultados = []
    for num in range(len(dados)):
        entradas.append(dados[num].retornarEntrada())
        resultados.append(dados[num].retornarResultado())
    return [entradas, resultados]

class RedeRecorrente():
	def __init__(self, caminho, numero):
		self.unidade1 = sslr.UnidadeDeSaveELoad(caminho, numero)
	def carregar(self):
		self.entradas = int(self.unidade1.retornarValor('entradas:'))
		self.saidas = int(self.unidade1.retornarValor('saidas:'))
		self.rede = cr.RedeNeuralRecorrente().receberRede(sslr.decodificarRedeNeural(self.unidade1.retornarValor(0))[0], self.saidas)
	def criarRede(self, camadas, entradas, saidas):
		self.rede = cr.RedeNeuralRecorrente().gerar(camadas, entradas, saidas)
		self.saidas = saidas
		self.entradas = entradas
		self.salvar()
	def processar(self, entrada):
		self.carregar()
		return self.rede.processar(entrada)
	def salvar(self):
		self.unidade1.salvarValor(0, sslr.codificarRede(self.rede.retornarRede()))
		self.unidade1.salvarValor('entradas:', self.rede.entradas)
		self.unidade1.salvarValor('saidas:', self.rede.saidas)
	def zerar(self):
		self.carregar()
		self.rede.zerar()
	def treinar(self,dados):
		self.carregar()
		entradas, resultados = retornarDados(dados) 
		r1 = self.rede.retornarRede()
		r3 = r1
		erro1 = r1.retornarErros(entradas, resultados)
		menorErro = erro1
		print(menorErro)
		while erro1 > 0:
			r2 = r1
			r2.taxa(1)
			erro2 = r2.retornarErros(entradas, resultados)

			erro3 = r3.retornarErros(entradas, resultados)

			if erro2 <= erro1:
				erro1 = erro2
				r1 = r2
			if erro3 <= erro1:
				erro1 = erro3
				r1 = r3
			if erro1 < menorErro:
				menorErro = erro1
				print(menorErro)
				self.rede.receberRede(r1, self.rede.saidas)
				self.salvar()
		self.rede.receberRede(r1, self.rede.saidas)
		self.salvar()
	def taxa(self):
		self.rede.taxa()
	def aleatoriar(self):
		self.rede.aleatoriar()









