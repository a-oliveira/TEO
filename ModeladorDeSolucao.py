# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:26:54 2019

@author: thiag
"""
from random import random
from random import randint
import datetime
import json
from Tarefas import Tarefa
from Agenda import Agenda
from Dispositivos import Dispositivo
class Modelador():
    
    def gerarDadosIniciais(self,fracaoDesejada,qntTarefas):
        agenda = Agenda(15)
        tarefas = []
        for i in range(qntTarefas):
            tarefa = None
            if fracaoDesejada == 60:
                horarios = self._gerarHorariosAleatorios(True)                
            else:
                horarios = self._gerarHorariosAleatorios(False)
            
            tarefa = Tarefa(horarios.get("EST"),horarios.get("LST"),horarios.get("RST"))
            tarefa.definirDispositivo(Dispositivo())
            tarefas.append(tarefa)
        
        agenda.agendarTarefas(tarefas)
                
                
                
    
    
    def _gerarHorariosAleatorios(self,flagHora):
        horaEst = randint(0,23)
        horaLst = randint(horaEst,24)
        horaRst = randint(horaEst,horaLst)
        retorno = {}
        
        if flagHora:
            est = datetime.time(horaEst,0)
            lst = datetime.time(horaLst,0)
            rst = datetime.time(horaRst,0)
            retorno.update({"EST",est})
            retorno.update({"LST",lst})
            retorno.update({"RST",rst})
        else:
            est = datetime.time(horaEst,randint(0,60))
            lst = datetime.time(horaLst,randint(0,60))
            rst = datetime.time(horaRst,randint(0,60))
            start = datetime.time(horaStart,randint(0,60))
            retorno.update({"EST",est})
            retorno.update({"LST",lst})
            retorno.update({"RST",rst})
        
        return retorno
                
        
        