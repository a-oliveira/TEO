from random     import randint
from datetime   import datetime, time
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
        pos_ini = self.hashHora(start)
        pos_fim = pos_ini + int((tarefa.duracao.hour*60 + tarefa.duracao.minute)/self.fracao)
        i       = pos_ini
        j       = pos_fim
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
            while pos_ini <= pos_fim:
                self.intervalos[pos_ini].append(tarefa)
                pos_ini = pos_ini + 1
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

''' def _atrasarHorario(self,horarioAtual,tempoAtraso):
        horario = horarioAtual.hour
        return horario + tempoAtraso
    
    def _adiantarHorario(self,horarioAtual,tempoAdianto):
        horario = horarioAtual.hour
        return horario - tempoAdianto'''

                            
                
        