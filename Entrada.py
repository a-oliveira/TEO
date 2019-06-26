#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:21:15 2019

@author: andressa
"""
import datetime
from Tarefas         import Tarefa
from Agenda          import Agenda
from Dispositivos    import Dispositivo
from DispositivoHVAC import DispositivoHVAC

class DadosEntrada():
    
    def lerArquivo(self):
        arquivo = open("dadosEntrada.txt", "r")
        linhas  = arquivo.readlines()
        tarefas = []
        
        for linha in linhas:
            dados = linha.split()
            tarefas.append(self.criarTarefa(dados))
            #print("Nova tarefa EST = " + str(novaTarefa.est) + '\n' + "Dispositivo = " + novaTarefa.dispositivo.consumo)
            #print(linha)
        return tarefas

    def criarDispositivo(self, dados):
        #posicao 0 = tipo
        #posicao 6 = consumo
        
        if dados[5] == "<class 'DispositivoHVAC.DispositivoHVAC'>":
            dispositivo = DispositivoHVAC(dados[6], dados[7], dados[8], dados[9])
        else:
            dispositivo = Dispositivo(dados[0], dados[6])
            
        return dispositivo
    
    def criarTarefa(self, dados):
        #pega os valores de est, rst e lst e converte pra inteiro para
        #atribuir às variáveis da Tarefa
        
        est                     = datetime.time(int(dados[1].split(":")[0])) 
        rst                     = datetime.time(int(dados[2].split(":")[0]))
        lst                     = datetime.time(int(dados[3].split(":")[0]))
        duracao                 = datetime.time(int(dados[4].split(":")[0]))
        novaTarefa              = Tarefa(est, rst, lst, duracao)
        novaTarefa.definirDispositivo(self.criarDispositivo(dados))
        
        return novaTarefa