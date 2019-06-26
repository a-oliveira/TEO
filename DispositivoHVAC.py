# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:22:55 2019

@author: thiag
"""
from Dispositivos import Dispositivo
import numpy as np
class DispositivoHVAC(Dispositivo):
    
    resTermica = 0
    tempIn = 0
    tempOut = 0
    capTermica = 0
    
    def __init__(self,capTermica,resTermica,tempIn,tempOut):
        Dispositivo.__init__(self,"HVAC",0)
        self.capTermica = capTermica
        self.resTermica = resTermica
        self.tempIn = tempIn
        self.tempOut = tempOut

    
    def calcularConsumo(self,tempoExecutando,tempDesejada):
        expoente = np.e**(-1*(tempoExecutando/(self.resTermica*self.capTermica)))
        pri = self.tempIn * expoente
        sec = self.resTermica*(1-expoente)
        tec = self.tempOut*(1-expoente)
        return (tempDesejada - pri - tec)/sec
    
    def setTempIn(self,novoTempIn):
        self.tempIn = novoTempIn
        
    def setTempOut(self,novoTempOut):
        self.tempOut = novoTempOut