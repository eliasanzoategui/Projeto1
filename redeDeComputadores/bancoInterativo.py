import Banco as b
import socket as s

class BancoInterativo():
    def __init__(self, caminho, numero, porta, ip):
        self.porta = porta
        self.ip = ip
        self.unidade = b.UnidadeDeSaveELoad(caminho, numero)
    def exe(self):
        s1 = s.socket(s.AF_INET, s.SOCK_STREAM)
        s1.bind((self.ip, self.porta))
        while True:
            s1.listen()
            print('Aguardando conexão...')
            con, ende = s1.accept()
            print('conectado em: ', str(ende))
            while True:
                data = con.recv(1024).decode()
                if not data:
                    print('fechando conexão...')
                    con.close()
                    break
                con.sendall(self.decodificarComando(data).encode())
                
    def decodificarComando(self, texto):
        try:
            comando = texto.split('(')[0]
            valor = texto.split('(')[1].split(')')[0]
            if comando == 'retornar':
                try:
                    return self.unidade.retornarValor(valor)
                except:
                    return 'erro no retornar valor'
            elif comando == 'salvar':
                try:
                    valores = valor.split(',')
                    nome = valores[0]
                    valorDoItem = valores[1]
                    self.unidade.salvarValor(nome, valorDoItem)
                    return 'feito'
                except:
                    return 'erro no salvar valor'
            else:
                return 'falta de compreensao'
        except:
            return 'erro no ler comando'

class Cliente():
    def __init__(self, ip, porta):
        self.ip = ip
        self.porta = porta
    def conectar(self, dados):
        s1 = s.socket(s.AF_INET, s.SOCK_STREAM)
        s1.connect((self.ip, self.porta))
        s1.sendall(str(dados).encode())
        ens = s1.recv(1024)
        print(ens.decode())

