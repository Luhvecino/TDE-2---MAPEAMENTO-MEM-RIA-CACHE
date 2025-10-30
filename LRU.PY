entrada = input("Digite a sequência de páginas separadas por vírgula: ")
paginas = [int(x.strip()) for x in entrada.split(",")]

num_quadros = int(input("Digite o número de quadros de memória: "))

memoria = [None] * num_quadros
uso_recente = []  # Guarda índices de uso
page_faults = 0

print("\n--- Simulação LRU ---")

for pagina in paginas:
    print(f"\n🔹 Inserindo página: {pagina}")
    if pagina not in memoria:
        page_faults += 1
        if None in memoria:
            idx = memoria.index(None)
        else:
            # O menos recentemente usado é o primeiro da lista
            idx = uso_recente.pop(0)

        removida = memoria[idx]
        memoria[idx] = pagina
        print(f"📦 Page Fault! Substituiu {removida} no quadro {idx}.")
    else:
        idx = memoria.index(pagina)
        print(f"✅ Página {pagina} acessada (quadro {idx}).")

        # Remove e adiciona novamente no final (mais recente)
        if idx in uso_recente:
            uso_recente.remove(idx)

    uso_recente.append(idx)

    # Mostrar estado atual
    for i, p in enumerate(memoria):
        print(f" q{i}: {p if p is not None else '-'}")

print(f"\nTotal de Page Faults (LRU): {page_faults}")

# Menos Recentemente Usado

# 1 - Teste com a sequencia de paginas para 8 quadros.:
# a ) 4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7
# qual quadro na memória possuirá a página 7 ?
# q5
# Total de Page Faults (LRU): 12

# b)  4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11
# qual quadro na memória possuirá a página 11?
# q2
# Total de Page Faults (LRU): 16

# c) 4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11 
# qual quadro na memória possuirá a página 11?
# q5
# Total de Page Faults (LRU): 11