# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:22:55 2019

@author: thiag
"""
from Dispositivos import Dispositivo
class DispositivoHVAC(Dispositivo):
    
    resTermica = 0
    tempIn = 0
    tempOut = 0
    capTermica = 0
    
    def __init__(self,tipo,consumo,capTermica,resTermica,tempIn,tempOut):
        Dispositivo.__init__(tipo,consumo)
        self.resTermica = resTermica
        self.tempIn = tempIn
        self.tempOut = tempOut
    
    def calcularConsumo(self,tempoExecutando):
        return (self.capTermica - ((self.tempIn - self.tempOut)/self.resTermica)) * tempoExecutando
    
    def setTempIn(self,novoTempIn):
        self.tempIn = novoTempIn
        
    def setTempOut(self,novoTempOut):
        self.tempOut = novoTempOut