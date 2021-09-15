import scriptDeSaveELoadDeRede as sslr
import NetWorkApp as nwa
import treinadorDeRede as tr



banco = 'E:\pacote1\WorkSpaceDeRede\processoDeTreinoDeRede\Bancos2'
numero = 0


# responder [0, 0, 0, 1]
# gato [1, 0, 0, 0]
# bonito [0, 1, 0, 0]
# é ou não [0, 0, 1, 0]

rede1 = nwa.RedeRecorrente(banco, numero)
#rede1.criarRede([10, 10], 1, 1)

d = nwa.Data
dados = [
    d([0, 0], [0]),
    d([1, 0], [1]),
    d([0, 1], [1]),
    d([1, 1], [0]),
]
try:
    #rede1.treinar(dados)
    pass
except:
    pass

print(rede1.processar([[1], [0], [1], [1], [1]]))
