import numpy as np

def salvaTamanhoInstancia(instancia, matriz):
    linha, coluna = matriz.shape    #função numpy que retorna as dimensões de uma matriz

    string = instancia + ' ' + str(linha) + ' ' + str(coluna)   #estrutura nome_instância qtd_linhas qtd_colunas

    print(string)   #mostra o resultado na tela

    arquivo = open('C:/Users/rocha/Documents/Unifei/Algoritmos em Grafos/Atividade 1/Instâncias/Resultados/' + instancia + '_dimensão', 'a+')
    arquivo.writelines(string + '\n')   #salva o resultado em arquivo
    arquivo.close()
