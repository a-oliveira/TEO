# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:12:52 2019

@author: thiag
"""

class Dispositivo():
    
    tipo      = ""
    categoria = "HVAC"
    consumo   = 0

    def __init__(self, tipo, consumo):
        self.tipo    = tipo
        self.consumo = consumo