entrada = input("Digite a sequência de páginas separadas por vírgula: ")
paginas = [int(x.strip()) for x in entrada.split(",")]

num_quadros = int(input("Digite o número de quadros de memória: "))

memoria = [None] * num_quadros
uso_recente = []  # Guarda índices de uso
page_faults = 0

print("\n--- Simulação MRU ---")

for pagina in paginas:
    print(f"\n🔹 Inserindo página: {pagina}")
    if pagina not in memoria:
        page_faults += 1
        if None in memoria:
            idx = memoria.index(None)
        else:
            # O mais recentemente usado é o último da lista
            idx = uso_recente.pop()

        removida = memoria[idx]
        memoria[idx] = pagina
        print(f"📦 Page Fault! Substituiu {removida} no quadro {idx}.")
    else:
        idx = memoria.index(pagina)
        print(f"✅ Página {pagina} acessada (quadro {idx}).")
        if idx in uso_recente:
            uso_recente.remove(idx)

    uso_recente.append(idx)

    # Mostrar estado atual
    for i, p in enumerate(memoria):
        print(f" q{i}: {p if p is not None else '-'}")

print(f"\nTotal de Page Faults (MRU): {page_faults}")

# Mais Recentemente Usado

# 1 - Teste com a sequencia de paginas para 8 quadros.:
# a ) 4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7
# qual quadro na memória possuirá a página 7 ?
# q2
# Total de Page Faults (MRU): 11


# b)  4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11
# qual quadro na memória possuirá a página 11?
# q6
# Total de Page Faults (MRU): 14

# c) 4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11 
# qual quadro na memória possuirá a página 11?
# q7
# Total de Page Faults (MRU): 12

# 2 - Qual a melhor politica de substituição?

# R: Depende do padrão de acesso às páginas. 
# Em geral, LRU tende a ser mais eficiente para padrões de acesso locais, enquanto FIFO pode ser mais simples de implementar. 
# MRU pode ser útil em casos específicos onde as páginas mais recentemente usadas são menos propensas a serem reutilizadas em breve.
# 
