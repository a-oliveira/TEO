#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:21:15 2019

@author: andressa
"""
import datetime
from Tarefas import Tarefa
from Agenda import Agenda
from Dispositivos import Dispositivo

class DadosEntrada():
    
    def lerArquivo(self):
        arquivo = open("dadosEntrada.txt", "r")
        linhas  = arquivo.readlines()
        tarefas = []
        
        for linha in linhas:
            dados = linha.split()
            
            #pega os valores de est, rst e lst e converte pra inteiro para
            #atribuir às variáveis da Tarefa
            
            '''est                     = datetime.time(int(dados[1].split(":")[0])) 
            rst                     = datetime.time(int(dados[2].split(":")[0]))
            lst                     = datetime.time(int(dados[3].split(":")[0]))
            duracao                 = datetime.time(int(dados[4].split(":")[0]))
            novaTarefa              = Tarefa(est, rst, lst, duracao)
            dispositivo             = Dispositivo(dados[0], dados[5])
            novaTarefa.dispositivo  = dispositivo
            
            tarefas.append(novaTarefa)'''
            #print("Nova tarefa EST = " + str(novaTarefa.est) + '\n' + "Dispositivo = " + novaTarefa.dispositivo.consumo)
            print(linha)
            return tarefas