# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:26:54 2019

@author: thiag
"""
from random import randint
import datetime
from Tarefas import Tarefa
from Agenda import Agenda
from Dispositivos import Dispositivo
class Modelador():
    
    tiposIniciais = ["lavar-roupa","passar-roupa","secar-roupa","lavar-louça","jogar-truco"]
    
    def gerarDadosIniciais(self,fracaoDesejada,qntTarefas):
        agenda = Agenda(fracaoDesejada)
        tarefas = []
        for i in range(qntTarefas):
            tarefa = None
            if fracaoDesejada == 60:
                horarios = self._gerarHorariosAleatorios(True)                
            else:
                horarios = self._gerarHorariosAleatorios(False)
            duracao = datetime.time(randint(1,3),0)
            tarefa = Tarefa(horarios.get("EST"),horarios.get("LST"),horarios.get("RST"),duracao)
            dispositivo = Dispositivo(self.tiposIniciais[randint(0,len(self.tiposIniciais)-1)],0)
            tarefa.definirDispositivo(dispositivo)
            tarefas.append(tarefa)
        
        agenda.agendar(tarefas)
        agenda.imprimirIntervalos()
        
    def _gerarHorariosAleatorios(self,flagHora):
        horaEst = randint(0,22)
        horaLst = randint(horaEst,23)
        if horaLst == horaEst:
            horaLst = horaLst + 1
        horaRst = randint(horaEst,horaLst)
        est = None
        lst = None
        rst = None
        retorno = {}
        
        if flagHora:
            est = datetime.time(horaEst,0)
            lst = datetime.time(horaLst,0)
            rst = datetime.time(horaRst,0)           
        else:
            est = datetime.time(horaEst,randint(0,59))
            lst = datetime.time(horaLst,randint(0,59))
            rst = datetime.time(horaRst,randint(0,59))
        
        retorno.update({"EST":est})
        retorno.update({"LST":lst})
        retorno.update({"RST":rst})        
        return retorno
                
        
        