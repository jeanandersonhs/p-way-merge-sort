
import sys
import heapq

import os 
import math
import tempfile
class BalancedSorterPways:
    def __init__(self, p_ways: int, input_file: str, output_file: str):
        
        if p_ways<2:
            raise Exception ("opcao invalida para p, caminhos n pode ser menor que 2")

        self.input_file = input_file
        self.output_file = output_file
        self.p_ways = p_ways
        self.processed_regs = 0
        self.runs = 0
        self.parses =0



    def sort(self):
        
        """
        Gerar as sequencias iniciais ordenadas(runs) utilizando algoritmo
        de selecao por substituicao

        Intercalacao de ate p sequencias para gerar um unico arquivo ordenado 

        Geracao da saida 

        
        """
        print("sort")
    

    def create_run_file(self, directory, index_run):
        """
        Cria um arquivo temporário para armazenar a run ordenada,
        não excluído automaticamente, dentro do diretório especificado.
        Retorna o caminho relativo do arquivo criado.
        """

        # Garante que o diretório existe
        os.makedirs(directory, exist_ok=True)

        try:
            fd, absolute_path = tempfile.mkstemp(
                prefix=f"run_file{index_run}_", suffix=".txt", dir=directory, text=True
            )
            os.close(fd)  # Fecha o descritor, apenas queremos o caminho
            return os.path.relpath(absolute_path)
        except Exception as e:
            raise Exception(f"erro ao criar arquivo temporario {e}")
    

    def generate_runs(self):
        

        """
        Geração das sequencias ordenadas iniciais(runs) utilizando algoritmo de selecao por substituicao
        carregando p registros do arquivo de entrada na memória por meio de uma min-heap.

        - remove root heap escreve no arquivo de saida
        - ler registro arquivo de entrda
        - se é maior que o anterior 

        retorna os arquivos criados para alternar

        """
        run_files = []
        heap_inicial = []

       

        try: 
            # ler um a um e colocar na heap inicial
            with open (self.input_file, "r") as entrada:
            
                min_heap = []
                conteudo = entrada.read()
                
                numeros = iter(int(x) for x in conteudo.split() if x.isdigit())
                for _ in range(self.p_ways):
                    try:
                        numero = next(numeros)
                        heapq.heappush(min_heap, (numero,0))
                    except StopIteration:
                        break

                print(min_heap)


                registros_marcados = []



                # enquanto heap nao estiver vazia e ainda houver numeros marcados
                # pegar o menor elemento da heap, escrever no arquivo de saida
                # ler o proximo registro do arquivo de entrada, se for maior que o menor elemento
                # da heap, adicionar na heap e remover o menor elemento da heap
                # se for menor, adicionar na lista de numeros marcados
                # se a lista de numeros marcados estiver vazia, escrever o menor elemento da heap
                # no arquivo de saida e continuar o loop 

                index_run = 0
                ultimo_inserido = -math.inf 

                while min_heap or registros_marcados:

                    if not min_heap:
                        """Acabou a sequencia anterior assim
                        leva todos os marcados para a min_reap 
                        """
                        
                        min_heap = registros_marcados
                        heapq.heapify(min_heap)
                        index_run += 1
                        registros_marcados = []
                        ultimo_inserido = -math.inf  # Resetando o ultimo inserido para o novo

                    
                    #Criar arquivo temporario para run inicial
                    path_run_file = self.create_run_file("temp", index_run)
                    self.runs += 1


                    
                    with open(path_run_file, "w") as temp_run_file:

                        
                        while min_heap:
                            # Pega o menor elemento da heap
                            numero = heapq.heappop(min_heap)
                            

                            # Verifica se o numero é maior que o ultimo inserido
                            if numero > ultimo_inserido:
                                # Escreve o numero no arquivo de run
                                temp_run_file.write(f"{numero}\n")
                                ultimo_inserido = numero
                                self.processed_regs += 1

                                # ler proximo e joga na heap
                                linha = entrada.readline()
                                if not linha:
                                    continue           
                                proximo_numero = int(linha.strip())
                                heapq.heappush(min_heap, proximo_numero)
                            else:
                                # Marca o numero como marcado
                                registros_marcados.append((numero))

                    with open(path_run_file, "r") as temp_run_file:
                        arquivo = temp_run_file.read()
                        print(f"sequencia criada: {arquivo}")
                    run_files.append(path_run_file)

                    
                    
                            

        except FileNotFoundError:
            raise("Arquivo não encontrado")
                







        












    


def main():

    if len(sys.argv) != 4:
        print(f"Argumentos insuficientes\n Tente: python3 pwats_mergesort.py <p_ways> input_file.text output_file.text ")
    try:
         p_ways = int(sys.argv[1])
         input_file = (sys.argv[2])
         output_file = (sys.argv[3])

         sort = BalancedSorterPways(p_ways, input_file, output_file)
         sort.generate_runs()
    except Exception as e: 
        print(f"Error {e}")

    

    
#    pways_order = BalancedSorterPways(p_ways, input_file, output_file)




if __name__ =="__main__":
    main()









