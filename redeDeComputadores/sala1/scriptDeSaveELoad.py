



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

def seExisteValor(arquivos, nome):
    if procurar(nome, arquivos) != None:
        return True
    else:
        return False


