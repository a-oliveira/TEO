from random     import randint
from datetime   import time
class Agenda():
    
    intervalos  = []
    fracao      = 0
    
    def __init__(self,fracao):
        for i in range(int((24*60)/fracao)):
            self.intervalos.append([None])
        self.fracao = fracao
        
    def hashHora(self,horario):
        hora    = horario.hour
        minuto  = horario.minute
        posicao = int(((hora*60)+minuto)/self.fracao)
        return posicao

    def agendarTarefa(self, tarefa):
        #define horário de início aleatoriamente
        hora    = randint(tarefa.est.hour,tarefa.lst.hour)
        minuto  = randint(0,59)
        start   = time(hora, minuto)
        #calcula posicao no array de acordo com o horário de início
        posIni = self.hashHora(start)
        posFim = posIni + self.hashHora(tarefa.duracao)
        if posFim > (len(self.intervalos)-1):
            posFim = posFim - len(self.intervalos)
        i       = posIni
        j       = posFim 
        aloca   = False

        #percorre do começo até o meio e do fim até o meio simultaneamente 
        #pra verificar se nesse intervalo existem tarefas conflitantes
        while i < j:
            if not(self.choqueDeTarefas(i, tarefa.recuperaTipo())) and not(self.choqueDeTarefas(j, tarefa.recuperaTipo())):
                aloca = True
            else:
                aloca = False
            i = i+1
            j = j-1
        if aloca:
            while posIni <= posFim:
                self.intervalos[posIni].append(tarefa)
                posIni = posIni + 1
            return True
        else:
            self.agendarTarefa(tarefa)
            #return False
    
    def agendar(self,tarefas):
        for tarefa in tarefas:
            self.agendarTarefa(tarefa)
    
    def choqueDeTarefas(self,pos,tipoTarefa):
        for j in range(len(self.intervalos[pos])):
            if self.intervalos[pos][j] is not None:
                if self.intervalos[pos][j].recuperaTipo() == tipoTarefa:
                    return True
                else:
                    return False
                
    def imprimirIntervalos(self):
        for i in range(len(self.intervalos)):
            for j in range(len(self.intervalos[i])):
                    if self.intervalos[i][j] is not None:
                            print("Agenda[",i,"]","[",j,"] = ", self.intervalos[i][j].recuperaTipo())

''' def _atrasarHorario(self,horarioAtual,tempoAtraso):
        horario = horarioAtual.hour
        return horario + tempoAtraso
    
    def _adiantarHorario(self,horarioAtual,tempoAdianto):
        horario = horarioAtual.hour
        return horario - tempoAdianto'''

                            
                
        