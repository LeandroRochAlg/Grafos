import sys
from Inicialização import matrizes as mt
from Inicialização import salva as sv


def main(instancia):
    matriz = mt.criarMatrizArquivo(instancia)

    sv.salvaTamanhoInstancia(instancia, matriz)

if __name__ == '__main__':
    main(str(sys.argv[1]))