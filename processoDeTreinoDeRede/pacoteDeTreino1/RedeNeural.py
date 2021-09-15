import random

def seEIgualAsListas(lista1, lista2):
    if len(lista1) == len(lista2):
        return True
    else:
        print('As duas listas não tem o mesmo comprimento[...]')
        return False

def positivo(x):
    if x < 0:
        x = -x
    return x

def somatorioDeErro(saida, resultado):
    if seEIgualAsListas(saida, resultado):
        erro = 0
        for raio in range(len(saida)):
            erro += positivo(saida[raio] - resultado[raio])
        return erro


def numAleatorio():
    return random.randint(-1000, 1000) / 10

def numAleatoriaDeTaxa(erro):
    return random.randint(-100, 100) / 10 * erro

class Neuron():
    def gerarPesosEBias(self, pesos):
        self.pesos = []
        for num in range(pesos):
            self.pesos.append(numAleatorio())
        self.bias = numAleatorio()
        return self
    def receberPesosEBias(self, pesos, bias):
        self.pesos = pesos
        self.bias = bias
        return self
    def processar(self, entrada):
        if seEIgualAsListas(entrada, self.pesos):
            saida = 0
            for num in range(len(entrada)):
                saida += entrada[num] * self.pesos[num]
            saida += self.bias
            if saida > 0:
                return 1
            else:
                return 0
    def mudarGenoma(self, erro):
        for num in range(len(self.pesos)):
            self.pesos[num] += numAleatoriaDeTaxa(erro)
    def aleatoriar(self):
        for num in range(len(self.pesos)):
            self.pesos[num] = numAleatorio()
        self.bias = numAleatorio()

class Camada():
    def receberNeuronios(self, neuronios):
        self.neuronios = neuronios
        return self
    def gerarNeuronios(self, quantidadeDeNeuronios, entradas):
        self.neuronios = []
        for num in range(quantidadeDeNeuronios):
            self.neuronios.append(Neuron().gerarPesosEBias(entradas))
        return self
    def processar(self, entrada):
        saidas = []
        for neuronio in self.neuronios:
            saidas.append(neuronio.processar(entrada))
        return saidas
    def mudarGenoma(self, erro):
        for neuronio in self.neuronios:
            neuronio.mudarGenoma(erro)
    def aleatoriar(self):
        for neuronio in self.neuronios:
            neuronio.aleatoriar()

class Rede():
    def receberCamadas(self, camadas):
        self.camadas = camadas
    def gerarCamadas(self, camadas, entradas):
        self.camadas = [Camada().gerarNeuronios(camadas[0], entradas)]
        for num in range(1, len(camadas)):
            self.camadas.append(Camada().gerarNeuronios(camadas[num], camadas[num - 1]))
        return self
    def processar(self, entrada):
        saida = self.camadas[0].processar(entrada)
        for num in range(1, len(self.camadas)):
            saida = self.camadas[num].processar(saida)
        return saida
    def mudarGenoma(self, erro):
        for camada in self.camadas:
            camada.mudarGenoma(erro)
    def aleatoriar(self):
        for camada in self.camadas:
            camada.aleatoriar()

class RedeNeuralConvuluncional():
    def ReceberRede(self, rede):
        self.rede = rede
        return self
    def gerarRede(self, camadas, entradas):
        self.rede = Rede().gerarCamadas(camadas, entradas)
        return self
    def processar(self, valores):
        return self.rede.processar(valores)
    def treinar(self, entradas, resultados):
        melhorRede = self
        erroDaMelhorRede = melhorRede.retornarErros(entradas, resultados)
        menorErro = erroDaMelhorRede
        print(menorErro)
        redeAleatoria = melhorRede
        while erroDaMelhorRede > 0:
            redeAleatoria.mudarGenoma(erroDaMelhorRede)

            redeDeTreino = melhorRede
            erroDaRedeDeTreino = redeDeTreino.retornarErros(entradas, resultados)

            erroDaRedeAleatoria = redeAleatoria.retornarErros(entradas, resultados)

            if erroDaRedeDeTreino <= erroDaMelhorRede:
                melhorRede = redeDeTreino
                erroDaMelhorRede = erroDaRedeDeTreino
                print(erroDaMelhorRede)
            if erroDaRedeAleatoria <= erroDaMelhorRede:
                melhorRede = redeAleatoria
                erroDaMelhorRede = erroDaRedeAleatoria
                print(erroDaMelhorRede)
            if erroDaMelhorRede < menorErro:
                menorErro = erroDaMelhorRede
                print(menorErro)
        self = melhorRede
    def retornarErro(self, entrada, resultado):
        return somatorioDeErro(self.processar(entrada), resultado)
    def retornarErros(self, entradas, resultados):
        erros = 0
        for teste in range(len(entradas)):
            erros += self.retornarErro(entradas[teste], resultados[teste])
        return erros
    def aleatoriar(self):
        self.rede.aleatoriar()
    def mudarGenoma(self, erro):
        self.rede.mudarGenoma(erro)


r1 = RedeNeuralConvuluncional().gerarRede([2, 1], 1)

entradas = [[1], [2], [3]]
resultados = [[0], [1], [0]]

r1.treinar(entradas, resultados)

print(r1.processar([2]))
print(r1.processar([1]))
