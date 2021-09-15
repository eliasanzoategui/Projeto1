import bancoInterativo as bi

ip = '127.0.0.1'
porta = 50000


b1 = bi.Cliente(ip, porta)


nome = 'dados do dia 1'
valor = '100 de madeira'
b1.conectar('retornar(' + nome + ')')
#b1.conectar('salvar(' + nome + ',' + valor + ')')

