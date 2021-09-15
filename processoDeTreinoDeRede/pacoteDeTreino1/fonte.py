from tkinter import *
import gerenciadorDeBancos as gb
import scriptDeSaveELoadDeRede as sslr
import ClassesDeRede as cr
import comandosNeuraisBasicos as cnb
import scriptDeExecuçãoDeRede as ser
import os

aqui = 'E:\interface\leitorDeRede\processoDeTreinoDeRede'.replace('\\', '\\\\')
aquiPronto = 'E:\\interface\\leitorDeRede\\processoDeTreinoDeRede'

class Lab():
    def __init__(self, fonte, texto, x, y):
        self.lab = Label(fonte, text=texto)
        self.lab.grid(column=x, row=y)
    def mudarValor(self, novoValor):
        self.lab.config(text=novoValor)
    def lerValor(self):
        return self.lab.get()

class SistemaDeInterface():
    def __init__(self, entradas, saidas):
        self.sistemasDeEntrada = entradas
        self.sistemasDeSaida = saidas
    def lerUmParametroDeEntrada(self, parametro):
        return self.sistemasDeEntrada[parametro].lerValor()
    def mudarValor(self, parametro):
        self.sistemasDeEntrada[parametro].mudarValor(parametro)


class Tela():
    def __init__(self):
        self.tela = Tk()
        self.tela.geometry('500x500')
        self.sistema = SistemaDeInterface([Lab(self.tela, 'um texto qualquer', 0, 0)], [Lab(self.tela, 'outro texto', 1, 0)])
        self.tela.mainloop()



Tela()







