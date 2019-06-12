# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:10:49 2019

@author: thiag
"""

class Tarefa():
    
    est = 0
    lst = 0
    rst = 0
    start = 0
    dispositivo = None
    
    def __init__(self,est,lst,rst):        
        self.est = est
        self.lst = lst
        self.rst = rst
    
    def definirStart(self,start):
        self.start = start
    
    def definirDispositivo(self,dispositivo):
        self.dispositivo = dispositivo
    
    def recuperaTipo(self):
        return self.dispositivo.tipo
    
    def recuperaTempoDuracao(self):
        return self.lst.hour - self.est.hour