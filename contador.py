import os
import threading
from collections import defaultdict

# Função para contar palavras em uma parte do texto
def contar_palavras(parte_texto, resultado, index):
    palavras = parte_texto.split()
    resultado[index] = len(palavras)

# Função para contar caracteres em uma parte do texto
def contar_caracteres(parte_texto, resultado_caractere, index):
    resultado_caractere[index] = len(parte_texto)

# Função principal para contar palavras e caracteres no arquivo
def contar_palavras_e_caracteres_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    partes_texto = texto.split('\n')
    
    resultados_palavras = [0] * len(partes_texto)
    resultados_caracteres = [0] * len(partes_texto)

    # Iniciando threads para armazenar a contagem
    threads_palavras = []
    threads_caracteres = []

    for i, parte in enumerate(partes_texto):
        thread_palavras = threading.Thread(target=contar_palavras, args=(parte, resultados_palavras, i))
        threads_palavras.append(thread_palavras)
        thread_palavras.start()

        thread_caracteres = threading.Thread(target=contar_caracteres, args=(parte, resultados_caracteres, i))
        threads_caracteres.append(thread_caracteres)
        thread_caracteres.start()

    for thread in threads_palavras:
        thread.join()
    for thread in threads_caracteres:
        thread.join()

    # Combinar os resultados após a conclusão de todas as threads
    contagem_total_palavras = sum(resultados_palavras)
    contagem_total_caracteres = sum(resultados_caracteres)

    return contagem_total_palavras, contagem_total_caracteres

# Função para contar frequências de palavras no arquivo
def contar_frequencias(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()
    palavras = texto.split()
    frequencia_palavras = defaultdict(int)

    for palavra in palavras:
        palavra_limpa = palavra.strip('.,!?"\'').lower()
        frequencia_palavras[palavra_limpa] += 1

    return frequencia_palavras

# Nome do arquivo a ser lido
arquivo = 'Sinopse.txt'

# Contar palavras e caracteres no arquivo
total_palavras, total_caracteres = contar_palavras_e_caracteres_arquivo(arquivo)
frequencia_palavras = contar_frequencias(arquivo)

# Imprimir o resultado
print(f'A contagem total de palavras no arquivo é: {total_palavras}')
print(f'A contagem total de caracteres no arquivo é: {total_caracteres}')

# Imprimir a frequência das palavras
print("Frequência das palavras no arquivo:")
for palavra, frequencia in frequencia_palavras.items():
    print(f"'{palavra}': {frequencia} vez(es)")
