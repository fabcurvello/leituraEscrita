# Trabalhando em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo leitura

palavras = [] # Lista dinâmica!

# Usando uma estrutura de repetição e inserindo as palavras capturadas na lista dinâmica
for linha in arquivo:
    palavras.append(linha.strip())

arquivo.close()

print(palavras)