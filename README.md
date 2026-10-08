# Atividade prática

# Alunos:
Luccas Henrique Ribeiro da Silva 05223-053

João Francisco Bordini Ferreira 05223-012


## Simulador de Gerenciamento de Memória

Em dupla, desenvolva ou adapte um programa Python capaz de simular algoritmos de substituição de páginas.

O programa deverá:

1. receber uma **sequência de páginas**;
2. receber a **quantidade de frames**;
3. executar o algoritmo **FIFO**;
4. executar o algoritmo **LRU**;
5. mostrar cada acesso realizado;
6. indicar se ocorreu `HIT` ou `PAGE FAULT`;
7. mostrar a situação da memória após cada acesso;
8. apresentar ao final:
   - quantidade de page faults;
   - quantidade de hits;
   - taxa de page faults;
   - taxa de hits;
9. comparar os resultados dos dois algoritmos.

### Exemplo de entrada

```text
Quantidade de frames: 3
Páginas: 1 2 3 4 1 2 5 1 2 3 4 5
```

### Exemplo de saída esperada

```text
Página 1 -> [1]       PAGE FAULT
Página 2 -> [1, 2]    PAGE FAULT
Página 3 -> [1, 2, 3] PAGE FAULT
...
```

Ao final:

```text
FIFO
Page Faults: ...
Hits: ...

LRU
Page Faults: ...
Hits: ...
```

Código:

```python
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
```

Saída da execução:

```text
Digite as páginas separadas por espaço: 1 2 3 4 1 2 5 1 2 3 4 5
Digite a quantidade de frames: 3

Sequência: [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
Frames: 3

FIFO
Página 1 -> [1] PAGE FAULT
Página 2 -> [1, 2] PAGE FAULT
Página 3 -> [1, 2, 3] PAGE FAULT
Página 4 -> [4, 2, 3] PAGE FAULT
Página 1 -> [4, 1, 3] PAGE FAULT
Página 2 -> [4, 1, 2] PAGE FAULT
Página 5 -> [5, 1, 2] PAGE FAULT
Página 1 -> [5, 1, 2] HIT
Página 2 -> [5, 1, 2] HIT
Página 3 -> [5, 3, 2] PAGE FAULT
Página 4 -> [5, 3, 4] PAGE FAULT
Página 5 -> [5, 3, 4] HIT

LRU
Página 1 -> [1] PAGE FAULT
Página 2 -> [1, 2] PAGE FAULT
Página 3 -> [1, 2, 3] PAGE FAULT
Página 4 -> [4, 2, 3] PAGE FAULT
Página 1 -> [4, 1, 3] PAGE FAULT
Página 2 -> [4, 1, 2] PAGE FAULT
Página 5 -> [5, 1, 2] PAGE FAULT
Página 1 -> [5, 1, 2] HIT
Página 2 -> [5, 1, 2] HIT
Página 3 -> [3, 1, 2] PAGE FAULT
Página 4 -> [3, 4, 2] PAGE FAULT
Página 5 -> [3, 4, 5] PAGE FAULT

RESULTADOS

FIFO
Page Faults: 9
Hits: 3
Taxa de page faults: 75.00%
Taxa de hits: 25.00%

LRU
Page Faults: 10
Hits: 2
Taxa de page faults: 83.33%
Taxa de hits: 16.67%

COMPARAÇÃO
FIFO teve menos page faults nesta sequência.
```

# Perguntas

**1. Qual é a diferença entre um HIT e um PAGE FAULT?**  
**Resposta:**

Page HIT é o evento que ocorre quando a página solicitada já se encontra na memória. Page fault ocorre quando a página solicitada não é encontrada na memória e o sistema operacional precisa carregá-la a partir da memória secundária, substituindo outra página caso todos os frames estejam ocupados.

**2. Qual é a principal diferença entre FIFO e LRU?**  
**Resposta:**

A principal diferença é que o FIFO substitui a página que entrou primeiro na memória, enquanto o LRU substitui a página que está há mais tempo sem ser utilizada. O FIFO considera a ordem de entrada das páginas, e o LRU considera a última vez que cada página foi acessada.

**3. Um page fault significa necessariamente que existe um erro no programa? Explique.**  
**Resposta:**

Um page fault não significa necessariamente que existe um erro no programa. Ele ocorre quando a página solicitada não se encontra na memória e o sistema operacional precisa carregá-la a partir da memória secundária. Isso faz parte do funcionamento normal do gerenciamento de memória.

**4. Aumentar a quantidade de frames sempre reduz o número de page faults no FIFO? Utilize o experimento da Anomalia de Belady para justificar.**  
**Resposta:**

Aumentar a quantidade de frames nem sempre reduz o número de page faults no FIFO. No experimento com a sequência 1 2 3 4 1 2 5 1 2 3 4 5, o FIFO apresenta 9 page faults com 3 frames e 10 page faults com 4 frames. Esse comportamento é chamado de Anomalia de Belady, que ocorre quando o aumento da quantidade de frames provoca um aumento no número de page faults.

**5. Em quais situações FIFO e LRU podem produzir resultados diferentes?**  
**Resposta:**

FIFO e LRU podem produzir resultados diferentes quando uma página que entrou primeiro na memória é acessada novamente. Esse acesso não altera sua ordem no FIFO, mas faz com que ela seja considerada recente no LRU. Assim, quando a memória estiver cheia e outra página precisar ser carregada, os algoritmos podem escolher páginas diferentes para substituir.

**6. Por que o algoritmo Ótimo normalmente apresenta um bom resultado?**  
**Resposta:**

O algoritmo Ótimo apresenta um bom resultado porque considera os acessos futuros e substitui a página que vai demorar mais para ser utilizada novamente ou que não será mais utilizada. Dessa forma, ele mantém na memória as páginas que serão necessárias mais cedo, reduzindo o número de page faults.

**7. Por que um sistema operacional real não consegue utilizar perfeitamente o algoritmo Ótimo?**  
**Resposta:**

Um sistema operacional real não consegue utilizar perfeitamente o algoritmo Ótimo porque não sabe com certeza quais páginas serão acessadas no futuro. Como esse algoritmo depende dessa informação para escolher qual página substituir, ele é utilizado principalmente como referência para comparar o desempenho de outros algoritmos.

**8. Execute pelo menos três sequências diferentes e registre qual algoritmo apresentou menos page faults em cada uma.**

Utilizando 3 frames em cada teste, foram executadas as seguintes sequências:

1. **Sequência: 1 2 3 4 1 2 5 1 2 3 4 5**  
   O FIFO apresentou 9 page faults e o LRU apresentou 10. Portanto, o FIFO teve menos page faults.

2. **Sequência: 1 2 3 1 4 1**  
   O FIFO apresentou 5 page faults e o LRU apresentou 4. Portanto, o LRU teve menos page faults.

3. **Sequência: 1 2 3 1 2 3**  
   Os dois algoritmos apresentaram 3 page faults, tendo o mesmo resultado.
