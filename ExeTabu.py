# -*- coding: utf-8 -*-
from ModeladorDeSolucao import Modelador
from BuscaLocal import BuscaLocal
from math import inf

class ExecutorBuscaTabu():
    listaTabu = []
    tamLimitBuscaTabu = 0
    tamVizinhanca = 0
    buscador = None
    agendaInicial = None
    limitExecucao = 0
    totalExecucao = 0
    penalideCusto = 0
    
    
    def __init__(self,pathArquivo,limitExecucao,maxCusto):        
        modeladorSolucao = Modelador()
        self.agendaInicial = modeladorSolucao.gerarAgendaArquivo(pathArquivo)
        self.limitExecucao = limitExecucao
        self.buscador = BuscaLocal()
        self.penalideCusto = maxCusto
        self.execucaoSemMelhora = 0
        self.totalExecucao = 0
        self.continuar = True
        self.faseIntensificacao = False
        
    def encontrarMelhorVizinho(self,vizinhanca):
        melhorVizinho = None
        melhorCusto = inf
        for vizinho in vizinhanca:
            if vizinho not in self.listaTabu:  
                custoVizinho = self.buscador._calcularCustoAgenda(vizinho)
                if self.faseIntensificacao:                    
                    if custoVizinho < self.penalideCusto:                                          
                        if custoVizinho < melhorCusto:
                            melhorCusto = custoVizinho
                            melhorVizinho = vizinho
                else:
                    if custoVizinho < melhorCusto:
                        melhorCusto = custoVizinho
                        melhorVizinho = vizinho            
        if melhorVizinho is None:
            self.continuar = False
        return [melhorVizinho,melhorCusto]
    
    def atualizarContinuar(self):
        self.execucaoSemMelhora += 1
        if self.execucaoSemMelhora > self.limitExecucao:
            self.continuar = False
        else:
            if self.execucaoSemMelhora > int((self.limitExecucao/2)):
                self.faseIntensificacao = True
                self.tamLimitBuscaTabu = int((self.tamVizinhanca*10)/100)
    
    def zerarBusca(self):
        self.execucaoSemMelhora = 0
        self.listaTabu = []
    
    def adicionarNaListaTabu(self,solucao):
        if len(self.listaTabu) < self.tamLimitBuscaTabu:
            self.listaTabu.append(solucao)
        else:
            melhorValorTabu = inf
            indiceMelhorTabu = 0
            indiceTabu = 0
            for tabu in self.listaTabu:
                valorTabu = self.buscador._calcularCustoAgenda(tabu)
                if valorTabu < melhorValorTabu:
                    melhorValorTabu = valorTabu
                    indiceMelhorTabu = indiceTabu 
                indiceTabu += 1
            self.listaTabu.pop(indiceMelhorTabu)
            self.listaTabu.append(solucao)
    def gerarVizinhancaInicial(self):
        vizinhanca = self.buscador.gerarVizinhanca(self.agendaInicial)
        self.tamVizinhanca = len(vizinhanca)
        self.tamLimitBuscaTabu = int((self.tamVizinhanca*50)/100)
        return vizinhanca
            
    
def main():
    
    #===========================================================================
    # Modelador().gerarDadosIniciais(60,6)
    #===========================================================================
    buscaTabu = ExecutorBuscaTabu("dadosEntrada2.txt", 5, 20000)
    melhorResultado = inf
    melhorAgenda = None
    vizinhanca = buscaTabu.gerarVizinhancaInicial()
    print("vizinhanca inicial:")
    contAgenda = 0
    for vizinho in vizinhanca:       
        print("agenda " + str(contAgenda))
        vizinho.imprimirIntervalos()
        print("custo = " + str(buscaTabu.buscador._calcularCustoAgenda(vizinho)))
        contAgenda += 1
    contExecucao = 0
    while buscaTabu.continuar:
        resultadoBusca = buscaTabu.encontrarMelhorVizinho(vizinhanca)
        melhorVizinho = resultadoBusca[0]
        melhorCustoVizinhanca = resultadoBusca[1]
        if melhorVizinho is not None:            
            print("Melhor vizinho " + str(contExecucao) + ": ")
            melhorVizinho.imprimirIntervalos()
            print("Custo = " + str(melhorCustoVizinhanca))
            
            if melhorCustoVizinhanca < melhorResultado:
                buscaTabu.zerarBusca()
                melhorResultado = melhorCustoVizinhanca
                melhorAgenda = melhorVizinho
                   
            else:
                buscaTabu.adicionarNaListaTabu(melhorVizinho)
                buscaTabu.atualizarContinuar()
            vizinhanca = None
            vizinhanca = buscaTabu.buscador.gerarVizinhanca(melhorVizinho)
        contExecucao += 1
       
    print("melhor resultado: ")
    melhorAgenda.imprimirIntervalos()
    print("custo = " + str(buscaTabu.buscador._calcularCustoAgenda(melhorAgenda)))
    
    

        
    
if __name__ == "__main__":
    main()    