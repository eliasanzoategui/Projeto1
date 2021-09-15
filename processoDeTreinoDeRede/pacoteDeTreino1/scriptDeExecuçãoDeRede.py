
def porcentragemDeAcerto(saidas, erro):
    return ((saidas - erro) / saidas) * 100

def imprimirPorcentagemDeAcerto(dados, erros):
    saidas = len(dados[0].resultado)
    comprimento = len(dados)
    totalDeSaidas = saidas * comprimento
    print('Taxa de acerto:' + str(int(porcentragemDeAcerto(totalDeSaidas, erros))) + '%')


class Data():
	def __init__(self, entrada, resultado):
		self.entrada = entrada
		self.resultado = resultado




