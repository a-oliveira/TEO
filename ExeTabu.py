from ModeladorDeSolucao import Modelador
from Agenda import Agenda
from Dispositivos import Dispositivo


def calcularCustoAgenda(agenda):
    custoTotal = 0
    for contador in range(len(agenda.intervalos)):
        if agenda.intervalos[contador][0] is not None:
            for tarefa in agenda.intervalos[contador]:
                custoTarefa = ((tarefa.dispositivo.calcularConsumo(agenda.fracao)) * agenda.custos[contador])
                custoTotal = custoTotal + custoTarefa
    return custoTotal


def main():

#    model = Modelador()
#    agenda = model.gerarDadosIniciais(60,2)
#    print(calcularCustoAgenda(agenda))
    
    

if __name__ == "__main__":
    main()