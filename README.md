# Algorithm p-way merge sort

Este projeto apresenta uma implementação em Python do algoritmo de ordenação externa **p-way merge sort**. O algoritmo foi desenvolvido como parte dos requisitos da disciplina MATA54 - Algoritmos e Estrutura de Dados II, com foco em manipular arquivos que não cabem inteiramente na memória principal.

## Funcionalidades

- **Ordenação Externa:** Capaz de ordenar arquivos de tamanho arbitrário, superando as limitações da memória RAM.
- **Geração de Runs com Seleção por Substituição:** As séries ordenadas iniciais (runs) são geradas eficientemente usando o método de seleção por substituição com um buffer em memória de tamanho `p`.
- **Intercalação Balanceada de p-vias:** Múltiplas runs são intercaladas (merged) simultaneamente usando uma heap mínima, garantindo um processo de ordenação eficiente.
- **Uso de Arquivos Temporários:** O processo utiliza arquivos temporários para armazenar as runs intermediárias, que são removidos ao final da execução.

## Como Funciona

O algoritmo opera em duas fases principais:

1.  **Geração de Runs Iniciais:**
    -   O arquivo de entrada é lido e `p` registros são carregados em uma heap mínima na memória.
    -   O menor elemento da heap é removido e escrito em um arquivo de run temporário.
    -   Um novo registro é lido do arquivo de entrada. Se for maior ou igual ao último elemento escrito, ele é inserido na heap. Caso contrário, é temporariamente "congelado" e será usado na próxima run.
    -   Este processo continua, gerando múltiplas runs ordenadas em arquivos temporários.

2.  **Intercalação das Runs (Merge):**
    -   As runs geradas na fase anterior são intercaladas em grupos de `p`.
    -   Uma heap mínima é usada para selecionar o menor elemento entre as `p` runs abertas, escrevendo-o em um novo arquivo de saída temporário.
    -   Este processo de intercalação é repetido em passagens, reduzindo o número de runs a cada passagem, até que reste apenas um único arquivo totalmente ordenado.

## Como Executar

### Executando no Replit (Recomendado)

#### Como Abrir o Shell no Replit

1. **Localizando o Shell:**
   - Na interface do Replit, procure pela aba **"Shell"** na parte inferior da tela ou na barra lateral esquerda
   - Caso não esteja visível, clique no ícone de **"Tools"** (ferramentas) na barra lateral e selecione **"Shell"**
   - Alternativamente, você pode usar o atalho `Ctrl + Shift + S` (ou `Cmd + Shift + S` no Mac)

2. **Abrindo o Shell:**
   - Clique na aba **"Shell"** para abrir o terminal
   - Você verá um prompt de comando similar a: `~/p-way-merge-sort$`

#### Executando o Programa

1. **Navegue até o diretório do projeto:**
   ```bash
   cd p-way-merge-sort
   ```

2. **Execute o programa com os parâmetros necessários:**
   ```bash
   python3 pways_mergesort.py <p> <arquivo_de_entrada> <arquivo_de_saida>
   ```

**Exemplo prático:**
```bash
python3 pways_mergesort.py 3 input_file.txt output_file.txt
```

### Executando Localmente

#### Pré-requisitos

-   Python 3.x

#### Instalação

1.  Clone o repositório:
    ```bash
    git clone https://github.com/jeanandersonhs/p-way-merge-sort
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd p-way-merge-sort
    ```

#### Uso

Para executar o programa, utilize o seguinte comando no terminal:

```bash
python3 pways_mergesort.py <p> <arquivo_de_entrada> <arquivo_de_saida>
```

**Parâmetros:**

-   `<p>`: O número de caminhos (e o tamanho do buffer em memória) para o merge sort. Deve ser um inteiro maior ou igual a 2.
-   `<arquivo_de_entrada>`: O caminho para o arquivo de texto contendo os números a serem ordenados (um número por linha).
-   `<arquivo_de_saida>`: O caminho para o arquivo onde o resultado ordenado será salvo.

**Exemplo:**

```bash
python3 pways_mergesort.py 3 input_file.txt output_file.txt
```

#### Limpar saida e Executar novamente
Para executar novamente basta limpar o arquivo de saida(_output_file.txt_) por meio de 
```bash
python clean.py
```

E assim pode ser refeito os passos de execução via `shell`

## Formato da Saída

Ao final da execução, além de gerar o arquivo de saída ordenado, o programa exibirá estatísticas sobre o processo de ordenação no console:

```
#Regs  Ways    #Runs   #Parses
25      3       5       2
```

-   `#Regs`: Número total de registros processados.
-   `Ways`: O valor de `p` (caminhos) utilizado.
-   `#Runs`: O número de sequências ordenadas iniciais geradas.
-   `#Parses`: O número de passagens de intercalação necessárias para obter o arquivo final ordenado.





Desenvolvido por Jean Anderson Hugo Jesus Santos