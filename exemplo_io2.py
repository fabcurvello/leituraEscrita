# Trabalhando em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo leitura

# Usando uma estrutura de repetição para ler linha por linha, todas as linhas:
for linha in arquivo:
    print("Linha capturada:", linha)

# Execute e observe o conteúdo apresentado no console
# Veja que a saída mostra cada fruta e uma linha separada. Isso acontece porque o print já pula uma linha, e cada palavra está salva com \n, que também pula uma linha

arquivo.close()


# Trabalhando em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo leitura

# Lendo apenas uma linha do arquivo:
linha = arquivo.readline()

print("Única linha capturada:", linha)

# Execute e observe o conteúdo apresentado no console

linha = arquivo.readline()

print("Única linha capturada:", linha)
print("Única linha capturada:", linha)

# Execute e observe o conteúdo apresentado no console

# Para remover o \n após a palavra capturada:
linha = linha.strip()

print("Única linha capturada:", linha)
print("Única linha capturada:", linha)

# Execute e observe o conteúdo apresentado no console

arquivo.close()