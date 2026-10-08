entrada = input("Digite as páginas separadas por espaço: ")
paginas_usuario = [int(valor) for valor in entrada.split()]

quantidade_frames = int(input("Digite a quantidade de frames: "))

if quantidade_frames <= 0 or len(paginas_usuario) == 0:
    print("Informe pelo menos uma página e uma quantidade de frames maior que zero.")
else:
    print("\nSequência:", paginas_usuario)
    print("Frames:", quantidade_frames)

    # FIFO
    memoria = []
    proximo = 0
    faults_fifo = 0
    hits_fifo = 0

    print("\nFIFO")

    for pagina in paginas_usuario:
        if pagina in memoria:
            hits_fifo += 1
            resultado = "HIT"
        else:
            faults_fifo += 1
            resultado = "PAGE FAULT"

            if len(memoria) < quantidade_frames:
                memoria.append(pagina)
            else:
                memoria[proximo] = pagina
                proximo += 1

                if proximo == quantidade_frames:
                    proximo = 0

        print(f"Página {pagina} -> {memoria} {resultado}")

    # LRU
    memoria = []
    ordem_uso = []
    faults_lru = 0
    hits_lru = 0

    print("\nLRU")

    for pagina in paginas_usuario:
        if pagina in memoria:
            hits_lru += 1
            resultado = "HIT"
            ordem_uso.remove(pagina)
        else:
            faults_lru += 1
            resultado = "PAGE FAULT"

            if len(memoria) < quantidade_frames:
                memoria.append(pagina)
            else:
                menos_recente = ordem_uso.pop(0)
                posicao = memoria.index(menos_recente)
                memoria[posicao] = pagina

        # A página acessada passa a ser a mais recente.
        ordem_uso.append(pagina)

        print(f"Página {pagina} -> {memoria} {resultado}")

    # Taxas
    total_acessos = len(paginas_usuario)

    taxa_faults_fifo = faults_fifo / total_acessos * 100
    taxa_hits_fifo = hits_fifo / total_acessos * 100

    taxa_faults_lru = faults_lru / total_acessos * 100
    taxa_hits_lru = hits_lru / total_acessos * 100

    # Resultados
    print("\nRESULTADOS")

    print("\nFIFO")
    print("Page Faults:", faults_fifo)
    print("Hits:", hits_fifo)
    print(f"Taxa de page faults: {taxa_faults_fifo:.2f}%")
    print(f"Taxa de hits: {taxa_hits_fifo:.2f}%")

    print("\nLRU")
    print("Page Faults:", faults_lru)
    print("Hits:", hits_lru)
    print(f"Taxa de page faults: {taxa_faults_lru:.2f}%")
    print(f"Taxa de hits: {taxa_hits_lru:.2f}%")

    # Comparação
    print("\nCOMPARAÇÃO")

    if faults_fifo < faults_lru:
        print("FIFO teve menos page faults nesta sequência.")
    elif faults_lru < faults_fifo:
        print("LRU teve menos page faults nesta sequência.")
    else:
        print("FIFO e LRU tiveram a mesma quantidade de page faults.")
