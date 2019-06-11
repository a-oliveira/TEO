# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 23:10:49 2019

@author: thiag
"""

class Tarefa():
    
    rst = 0
    est = 0
    lst = 0
    start = 0
    
    def __init__(self,rst,est,lst):
        self.rst = rst
        self.est = est
        self.lst = lst
    
    def definirStart(self,start):
        self.start = start