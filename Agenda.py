# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:07:36 2019

@author: thiag
"""
from numpy import zeros
class Agenda():
    
    intervalos = []
    fracao = 0
    
    def __init__(self,fracao):
        self.intervalos = zeros(int((24*60)/fracao))
        self.fracao = fracao
        
    def hashHora(self,horario):
        hora = horario.hour
        minuto = horario.minute
        posicao = int(((hora*60)+minuto)/self.fracao)
        return posicao