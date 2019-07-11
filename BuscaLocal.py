from copy import copy
from copy import deepcopy
from Agenda import Agenda

class BuscaLocal():    
    
    def gerarVizinhanca(self,agenda):
        vizinhanca = []
        for contador in range(agenda.totalTarefas):  
            novaAgenda = None      
            novaAgenda = self._copiarAgenda(agenda)    
            self._executarBuscaLocal(novaAgenda,contador)
            vizinhanca.append(novaAgenda)
        return vizinhanca
    
    def _copiarAgenda(self,agenda):   
        custos = deepcopy(agenda.custos)
        fracao = copy(agenda.fracao)
        intervalos = deepcopy(agenda.intervalos)
        totalTarefas = copy(agenda.totalTarefas)
        novaAgenda = Agenda(fracao)
        novaAgenda.custos = custos
        novaAgenda.intervalos = intervalos  
        novaAgenda.custos = custos
        novaAgenda.totalTarefas = totalTarefas
        agenda.custos = custos
        return novaAgenda            
    
    def _calcularCustoAgenda(self,agenda):
        custoTotal = 0
        for contador in range(len(agenda.intervalos)):
            if agenda.intervalos[contador][0] is not None:
                for tarefa in agenda.intervalos[contador]:
                    custoTarefa = tarefa.dispositivo.calcularConsumo(agenda.fracao) * agenda.custos[contador]
                    custoTotal = custoTotal + custoTarefa
        return custoTotal
    

    
    def _executarBuscaLocal(self,agenda,idTarefa):   
        melhorCusto = self._calcularCustoAgenda(agenda)    
        melhorInicio = 0
        melhorFim = 0     
        for intervalo in range(len(agenda.intervalos)):
            posTarefa = agenda.verificarHorario(intervalo,idTarefa)
            if posTarefa != -1:
                tarefa = agenda.intervalos[intervalo][posTarefa]
                melhorInicio = intervalo
                melhorFim = agenda.hashHora(tarefa.duracao) + melhorInicio
                break    
        agenda.removerTarefa(melhorInicio,melhorFim,idTarefa)
        inicio = agenda.hashHora(tarefa.est)
        inicioMax = agenda.hashHora(tarefa.lst)
        fim = (agenda.hashHora(tarefa.duracao) + inicio) +1
        continua = True
    
        while inicio <= inicioMax and continua:
            if agenda.verificaIntervalo(inicio,fim,tarefa.recuperaTipo()):
                agenda.alocarTarefa(inicio,fim,tarefa)
                custoAgenda = self._calcularCustoAgenda(agenda)
                if custoAgenda < melhorCusto:
                    melhorCusto = custoAgenda
                    melhorInicio = inicio
                    melhorFim = fim + 1
                agenda.removerTarefa(inicio,fim,idTarefa)
                inicio += 1
            else:
                continua = False            
        tarefa.start = melhorInicio
        agenda.alocarTarefa(melhorInicio,melhorFim,tarefa)
