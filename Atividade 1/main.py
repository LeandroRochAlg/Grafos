import sys
from Inicialização import matrizes as mt, salva as sv
from Controle import testes as ts, calculos as cl, manejo as mj


def main(instancia):
    matriz = mt.criarMatrizArquivo(instancia)

    sv.salvaTamanhoInstancia(instancia, matriz)

if __name__ == '__main__':
    main(str(sys.argv[1]))
