

class Tarefa():
    ID = 0
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
    
    def definirID(self,ID):
        self.ID = ID
    
    def definirStart(self,start):
        self.start = start
    
    def definirDispositivo(self,dispositivo):
        self.dispositivo = dispositivo
    
    def recuperaTipo(self):
        return self.dispositivo.tipo
    
    def calcularInstatisfacao(self):
        if self.start == self.rst:
            return 0
        elif self.start < self.rst:
            estMinuto = (self.est.hour * 60) + self.est.minute
            startMinuto = (self.start.hour * 60) + self.start.minute
            rstMinuto = (self.rst.hour * 60) + self.rst.minute
            return (startMinuto - estMinuto) / (rstMinuto - estMinuto)
        else:
            lstMinuto = (self.lst.hour * 60) + self.lst.minute
            startMinuto = (self.start.hour * 60) + self.start.minute
            rstMinuto = (self.rst.hour * 60) + self.rst.minute
            return (lstMinuto - startMinuto) / (lstMinuto - rstMinuto)
    
    def calcularCusto(self):
        duracaoHora = self.duracao.hour + (self.duracao.minute / 60)
        return self.dispositivo.consumo * duracaoHora
            
            
            