arquivo = open("palavras.txt", "w")
print(arquivo) # Mostra uma estrutura com nome do arquivo, modo (w, a ou r) e layout de caracteres (UTF-8)

arquivo.write("banana")
arquivo.write("melancia")
arquivo.write("abacate")

arquivo.close()

# Execute e observe o conteúdo do arquivo.txt

arquivo = open("palavras.txt", "w")
arquivo.write("banana")

arquivo.close()

# Execute e observe o conteúdo do arquivo.txt

arquivo = open("palavras.txt", "w")
print(arquivo) # Mostra uma estrutura com nome do arquivo, modo (w, a ou r) e layout de caracteres (UTF-8)

arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.write("abacate\n")
arquivo.write("morango\n")
arquivo.write("abacaxi\n")
arquivo.write("amora\n")

arquivo.close()

# Execute e observe o conteúdo do arquivo.txt

# Trabalhando em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo leitura

print(arquivo.read())

# Execute e observe o conteúdo apresentado no console

print(arquivo.read())

# Execute e observe o conteúdo apresentado no console

arquivo.close()