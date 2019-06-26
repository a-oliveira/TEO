from ModeladorDeSolucao import Modelador
from Agenda             import Agenda
from Entrada            import DadosEntrada


def calcularCustoAgenda(agenda):
    custoTotal = 0
    for contador in range(len(agenda.intervalos)):
        if agenda.intervalos[contador][0] is not None:
            for tarefa in agenda.intervalos[contador]:
                custoTarefa = ((tarefa.dispositivo.calcularConsumo(agenda.fracao)) * agenda.custos[contador])
                custoTotal = custoTotal + custoTarefa
    return custoTotal


def main():
    model = Modelador()
#   model.gerarDadosIniciais(60,6)
    entradaDados = DadosEntrada()
    tarefas      = entradaDados.lerArquivo("dadosEntrada2.txt")

    agenda = Agenda(60)
    model.definirCustoAleatoriamente(agenda.custos)
    agenda.agendar(tarefas)
    
    agenda.imprimirIntervalos()
    
if __name__ == "__main__":
    main()    