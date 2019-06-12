# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:07:36 2019

@author: thiag
"""
from random import randint
import datetime
class Agenda():
    
    intervalos = []
    fracao = 0
    
    def __init__(self,fracao):
        for i in range(int((24*60)/fracao)):
            self.intervalos.append([None])
        self.fracao = fracao
        
    def hashHora(self,horario):
        hora = horario.hour
        minuto = horario.minute
        posicao = int(((hora*60)+minuto)/self.fracao)
        return posicao
    
    def agendarTarefas(self,tarefas):
        for tarefa in tarefas:
            start = datetime.time(randint(tarefa.est.hour,tarefa.lst.hour),randint(0,59))
            indexAgenda = self.hashHora(start)
            if self.intervalos[indexAgenda][0] is None:
                tarefa.definirStart(start)
                self.intervalos[indexAgenda][0] = tarefa
            else:                
                for tarefaAgendada in self.intervalos[indexAgenda]:
                    if tarefaAgendada.recuperaTipo() == tarefa.recuperaTipo():
                        duracaoAgendada = tarefaAgendada.recuperaTempoDuracao()
                        comecoAtrasado = self._atrasarHorario(start,duracaoAgendada)
                        if tarefa.lst.hour > comecoAtrasado:
                            start.hour = comecoAtrasado
                            
                tarefa.definirStart = start
                self.intervalos[indexAgenda].append(tarefa)
    
    def _atrasarHorario(self,horarioAtual,tempoAtraso):
        horario = horarioAtual.hour
        return horario + tempoAtraso
    
    def _adiantarHorario(self,horarioAtual,tempoAdianto):
        horario = horarioAtual.hour
        return horario - tempoAdianto
    
    def _verificarChoque(self,tipoTarefa):
        print("batata")
        
    
    def _agendarTarefa(self,tarefa):
        duracao = tarefa.recuperaTempoDuracao()
        horarioFinal = datetime.time(tarefa.start.hour+duracao,tarefa.start.minute)
        indexStart = self.hashHora(tarefa.start)
        indexFinal = self.hashHora(horarioFinal)
        for i in range(indexStart,indexFinal):
            self.intervalos[i].append(tarefa)
                        
                
        