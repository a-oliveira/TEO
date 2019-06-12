from Agenda       import Agenda
from Tarefas      import Tarefa
from Dispositivos import Dispositivo
import numpy as np
from datetime     import datetime, timedelta, time

def main():

        tempo1 = time(00, 59)
        tempo2 = time(00, 30)
        tempo3 = time(00, 15)

        est1   = time(0)
        est2   = time(1, 30)
        est3   = time(3)

        lst1   = time(2)
        lst2   = time(2,15)
        lst3   = time(10)
        
        #print(tempo1)
        #print(tempo2)
        #print(tempo3)

        #print(lst1.hour)
        #print(lst2)
        #print(lst3)
        
        dispositivo1 = Dispositivo("maquina de lavar", 200)
        dispositivo2 = Dispositivo("ferro de passar", 15)

        tarefa1 = Tarefa(est1, lst1, 1, tempo1)
        tarefa2 = Tarefa(est2, lst2, 3, tempo2)
        tarefa3 = Tarefa(est3, lst3, 5, tempo3)

        tarefa1.definirDispositivo(dispositivo1)
        tarefa2.definirDispositivo(dispositivo2)
        tarefa3.definirDispositivo(dispositivo1)

        minhaAgenda = Agenda(15)

        listaTarefas = [tarefa1, tarefa2, tarefa3]

        minhaAgenda.agendar(listaTarefas)

        for i in range(len(minhaAgenda.intervalos)):
                for j in range(len(minhaAgenda.intervalos[i])):
                        if minhaAgenda.intervalos[i][j] is not None:
                                print("Agenda[",i,"]","[",j,"] = ", minhaAgenda.intervalos[i][j].recuperaTipo())
                

if __name__ == "__main__":
    main()