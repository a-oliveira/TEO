# -*- coding: utf-8 -*-
from random          import randint
import datetime
from Tarefas         import Tarefa
from Dispositivos    import Dispositivo
from DispositivoHVAC import DispositivoHVAC
from Entrada import DadosEntrada
from Agenda import Agenda
class Modelador():
    
    tiposIniciais = ["lavar-roupa","passar-roupa","secar-roupa","lavar-louça","jogar-truco"]
    
    def gerarDadosIniciais(self,fracaoDesejada,qntTarefas):   
        tarefas = []
        for i in range(qntTarefas):
            tarefa = None
            if fracaoDesejada == 60:
                horarios = self._gerarHorariosAleatorios(True)                
            else:
                horarios = self._gerarHorariosAleatorios(False)
            duracao = datetime.time(randint(1,4),0)
            tarefa = Tarefa(horarios.get("EST"),horarios.get("LST"),horarios.get("RST"),duracao)
            dispositivo = Dispositivo(self.tiposIniciais[randint(0,len(self.tiposIniciais)-1)],1)
            tarefa.definirDispositivo(dispositivo)
            tarefas.append(tarefa)
        
        arquivo = open("dadosEntrada2.txt", "w")
        
        for tarefa in tarefas:
            dadosTarefa = str(tarefa.est) + '\t' + str(tarefa.rst) + '\t' + str(tarefa.lst) + '\t' + str(tarefa.duracao) + '\t' + tarefa.recuperaTipo()        
            
            if tarefa.dispositivo.tipo == "HVAC":
                hvac = '\t' + str(DispositivoHVAC.resTermica) + '\t' + str(DispositivoHVAC.tempIn) + '\t' + str(DispositivoHVAC.tempOut) + '\t' + str(DispositivoHVAC.capTermica) + '\n'
                dados = dadosTarefa + hvac
            else:
                dados = dadosTarefa + '\t' + str(tarefa.dispositivo.consumo) + '\n'
            
            arquivo.writelines(dados)
        
        arquivo.close()
        
    def _gerarHorariosAleatorios(self,flagHora):
        horaEst = randint(0,22)
        horaLst = randint(horaEst,23)
        if horaLst == horaEst:
            horaLst = horaLst + 1
        horaRst = randint(horaEst,horaLst)
        est = None
        lst = None
        rst = None
        retorno = {}
        
        if flagHora:
            est = datetime.time(horaEst,0)
            lst = datetime.time(horaLst,0)
            rst = datetime.time(horaRst,0)           
        else:
            est = datetime.time(horaEst,randint(0,59))
            lst = datetime.time(horaLst,randint(0,59))
            rst = datetime.time(horaRst,randint(0,59))
        
        retorno.update({"EST":est})
        retorno.update({"LST":lst})
        retorno.update({"RST":rst})        
        return retorno
    
    def _definirCustoAleatoriamente(self,arrayCusto):
        contador = 0
        while contador < len(arrayCusto):
            intervalo = randint(1,5)
            valorIntervalo = randint(5,15)
            for i in range(intervalo):
                if (i+contador) > len(arrayCusto):
                    break
                else:
                    arrayCusto[contador] = valorIntervalo
                    contador = contador + 1
    
    def _definirCustoFixo(self):
        arrayCusto = [5,5,5,5,5,5,5,8,8,8,8,11,11,11,11,20,20,20,20,20,20,11,11,8]
        return arrayCusto
    
    def gerarAgendaArquivo(self,pathArquivo):
        entradaDados = DadosEntrada(pathArquivo)
        tarefas      = entradaDados.lerArquivo()
    
        agenda = Agenda(60)
        agenda.custos = self._definirCustoFixo()
        #=======================================================================
        # self._definirCustoFixo(agenda.custos)
        #=======================================================================
        agenda.agendar(tarefas)
        return agenda
                
        
        