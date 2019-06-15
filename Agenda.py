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
        #se o tempo final extrapolar o final da agenda, significa q sera no dia seguinte
        if posFim > (len(self.intervalos)-1):
            posFim = posFim - len(self.intervalos)
        aloca   = self.verificaIntervalo(posIni,posFim,tarefa.recuperaTipo())
        
        if aloca:
            self.alocarTarefa(posIni,posFim,tarefa)                
            return True
        else:
            posEst = self.hashHora(tarefa.est)
            posLst = self.hashHora(tarefa.lst)
            #tenta atrasar a tarefa
            for i in range(posIni,posLst):
                if not(self.choqueDeTarefas(i,tarefa.recuperaTipo())):
                    novoIni = i
                    novoFim = i + self.hashHora(tarefa.duracao)
                    if novoFim > len(self.intervalos):
                        novoFim = novoFim - len(self.intervalos)
                    aloca = self.verificaIntervalo(novoIni,novoFim)
                    if aloca:
                        self.alocarTarefa(novoIni,novoFim,tarefa)
                        return True
            #tenta adiantar a tarefa
            for i in range(posEst,posIni):
                if not(self.choqueDeTarefas(i,tarefa.recuperaTipo())):
                    novoIni = i
                    novoFim = i + self.hashHora(tarefa.duracao)
                    if novoFim > len(self.intervalos):
                        novoFim = novoFim - len(self.intervalos)
                    aloca = self.verificaIntervalo(novoIni,novoFim)
                    if aloca:
                        self.alocarTarefa(novoIni,novoFim,tarefa)
                        return True
            return False
                    

    def verificaIntervalo(self,inicio,fim,tipoTarefa):
        #percorre do começo até o meio e do fim até o meio simultaneamente 
        #pra verificar se nesse intervalo existem tarefas conflitantes
        aloca = False
        i = inicio
        j = fim
        while i < j:
            if not(self.choqueDeTarefas(i, tipoTarefa)) and not(self.choqueDeTarefas(j,tipoTarefa)):
                aloca = True
            else:
                aloca = False
            i = i+1
            j = j-1
        return aloca
    
    def alocarTarefa(self,inicio,fim,tarefa):
        while inicio <= fim:            
            if self.intervalos[inicio][0] is None:
                self.intervalos[inicio][0] = tarefa                    
            else:
                self.intervalos[inicio].append(tarefa)
            inicio = inicio + 1
        return True
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

                            
                
        