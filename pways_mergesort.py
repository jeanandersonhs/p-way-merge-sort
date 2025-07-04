
import sys
import heapq

import os 

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



    def sort():
        
        """
        Gerar as sequencias iniciais ordenadas(runs) utilizando algoritmo
        de selecao por substituicao

        Intercalacao de ate p sequencias para gerar um unico arquivo ordenado 

        Geracao da saida 

        
        """
        print("sort")
    


    def generate_runs(self):
        

        """
        Geração das sequencias ordenadas iniciais(runs) utilizando algoritmo de selecao por substituicao
        carregando p registros do arquivo de entrada na memória por meio de uma min-heap.

        - remove root heap escreve no arquivo de saida
        - ler registro arquivo de entrda
        - se é maior que o anterior 

        retorna os arquivos criados para alternar

        """

        heap_inicial = []

       

        try: 
            # ler um a um e colocar na heap inicial
            with open (self.input_file, "r") as entrada:
            
                min_heap = []
                
                for _ in range(self.p_ways):
                    linha = entrada.readline()
                    
                    #verifica se a linha está vazia
                    if not linha:
                        break

                    numero = int(linha.strip())
                    heapq.heappush(min_heap, numero)
                    self.processed_regs += 1

                numeros_marcados = []


                # enquanto heap nao estiver vazia e ainda houver numeros marcados
                # pegar o menor elemento da heap, escrever no arquivo de saida
                # ler o proximo registro do arquivo de entrada, se for maior que o menor elemento
                # da heap, adicionar na heap e remover o menor elemento da heap
                # se for menor, adicionar na lista de numeros marcados
                # se a lista de numeros marcados estiver vazia, escrever o menor elemento da heap
                # no arquivo de saida e continuar o loop 

                while min_heap or numeros_marcados:

                    menor = heapq.heappop(min_heap)
                
            




                
                







                

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









