class Tarefa():
    
    est         = 0
    lst         = 0
    rst         = 0
    start       = 0
    dispositivo = None
    duracao     = 0
    
    def __init__(self,est,lst,rst, duracao):        
        self.est        = est
        self.lst        = lst
        self.rst        = rst
        self.duracao    = duracao
    
    def definirStart(self,start):
        self.start = start
    
    def definirDispositivo(self,dispositivo):
        self.dispositivo = dispositivo
    
    def recuperaTipo(self):
        return self.dispositivo.tipo