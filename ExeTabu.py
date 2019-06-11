# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:25:03 2019

@author: thiag
"""
import numpy as np
import datetime
from Agenda import Agenda
def main():
    
    hora = int(input())
    minuto = int(input())
    
    data = datetime.time(hora,minuto)
    agenda = Agenda(60)
    
    print(agenda.hashHora(data))
    
    
    

if __name__ == "__main__":
    main()