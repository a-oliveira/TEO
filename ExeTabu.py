from ModeladorDeSolucao import Modelador
from Agenda             import Agenda
from Entrada            import DadosEntrada
from Dispositivos import Dispositivo
from copy import deepcopy


def calcularCustoAgenda(agenda):
    custoTotal = 0
    for contador in range(len(agenda.intervalos)):
        if agenda.intervalos[contador][0] is not None:
            for tarefa in agenda.intervalos[contador]:
                custoTarefa = ((tarefa.dispositivo.calcularConsumo(agenda.fracao)) * agenda.custos[contador])
                custoTotal = custoTotal + custoTarefa
    return custoTotal

def gerarVizinhanca(agenda):
    vizinhanca = []
    for contador in range(agenda.totalTarefas):
        novaAgenda = deepcopy(agenda)
        moverTarefa(novaAgenda,contador)

def moverTarefa(agenda,idTarefa):   
    melhorCusto = calcularCustoAgenda(agenda)
    melhorInicio = 0
    melhorFim = 0     
    for intervalo in range(len(agenda.intervalos)):
        posTarefa = agenda.verificarHorario(intervalo,idTarefa)
        if posTarefa != -1:
            tarefa = agenda.intervalos[intervalo][posTarefa]
            melhorInicio = intervalo
            melhorFim = agenda.hashHora(tarefa.duracao) + melhorInicio
    
    agenda.removerTarefa(melhorInicio,melhorFim,idTarefa)
    inicio = agenda.hashHora(tarefa.est)
    inicioMax = agenda.hashHora(tarefa.lst)
    fim = agenda.hashHora(tarefa.duracao) + inicio
    continua = True
    while inicio < inicioMax and continua:
        if agenda.verificaIntervalo(inicio,fim,tarefa.recuperaTipo()):
            agenda.alocarTarefa(inicio,fim,tarefa)
            custoAgenda = calcularCustoAgenda(agenda)
            if custoAgenda < melhorCusto:
                melhorCusto = custoAgenda
                melhorInicio = inicio
                melhorFim = fim
        else:
            a = 
            
        
    
    
    
    
            

def main():
    model = Modelador()
#    model.gerarDadosIniciais(60,2)
    entradaDados = DadosEntrada()
    tarefas      = entradaDados.lerArquivo("dadosEntrada2.txt")
#
    agenda = Agenda(60)
    model.definirCustoAleatoriamente(agenda.custos)
    agenda.agendar(tarefas)
#    
    agenda.imprimirIntervalos()
    for tarefas in agenda.intervalos:
        if tarefas[0] != None:
            tarefa = tarefas[0]
            inicio = agenda.hashHora(tarefa.start)
            fim = inicio + agenda.hashHora(tarefa.duracao)
            tipo = tarefa.recuperaTipo()
            print("inicio = " + str(inicio))
            print("fim = " + str(fim))
            print("tipo para remover=" + tipo)
            break
#    
    agenda.removerTarefa(inicio,fim,tipo)
    agenda.imprimirIntervalos()
    
if __name__ == "__main__":
    main()    