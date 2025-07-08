
import sys
import heapq
from heap import *

import os 
import math
import tempfile
import shutil
class BalancedSorterPways:
    def __init__(self, p_ways: int, input_file: str, output_file: str):
        
        if p_ways<2:
            raise Exception ("opcao invalida para p, caminhos n pode ser menor que 2")

        self.input_file = input_file
        self.output_file = output_file
        self.p_ways = p_ways
        self.total_regs = 0
        self.runs = 0
        self.parses =0



    def sort(self):
        
        """
        Gerenciamento do processo de ordenação
        - Gera as runs iniciais
        - Verifica se há arquivos gerados
        - Realiza o merge das runs
        - Gera o arquivo de saída final
        - Exclui os arquivos temporários
        - Exibe estatísticas do processo de ordenação

        
        """
        print("sort")

        # Gera as runs iniciais
        path_run_files  = self.generate_runs()

        # verifica se há arquivos
        if not path_run_files:
            return

        #merge 
        saida = self.merge_runs(path_run_files)

        # Gera o arquivo de saída final
        self.generate_output(saida)

        #mostrar estatisticas
        self.show_stats()
        

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
      

       

        try: 
            # ler um a um e colocar na heap inicial
            with open (self.input_file, "r") as entrada:
            
                min_heap = []
                
                conteudo = entrada.read()

                numeros = iter(int(x) for x in conteudo.split() if x.isdigit())
                for _ in range(self.p_ways):
                    try:
                        numero = next(numeros)
                        heapq.heappush(min_heap, numero)
                    except StopIteration:
                        break

                print(min_heap)

                if not min_heap:
                    return []


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
                                self.total_regs += 1

                                # ler proximo e joga na heap      
                
                                try:
                                    proximo_numero = next(numeros)

                                    heapq.heappush(min_heap, proximo_numero)

                                except StopIteration:   
                                    pass
                               
                            else:
                                # Marca o numero como marcado
                                registros_marcados.append((numero))

                    with open(path_run_file, "r") as temp_run_file:
                        arquivo = temp_run_file.read()
                        print(f"sequencia criada: {arquivo}")
                    run_files.append(path_run_file)
            return run_files

        except FileNotFoundError:
            raise("Arquivo não encontrado")
        

    def merge_runs(self, run_files: list):
        """
        Intercala arquivos usando uma min-heap 
        no maximo 2p arquivos abertos 
        """
        print("merge") 


        if len(run_files)<=1:
            return run_files[0] if run_files else None

        level = 0

        #apontando para runs iniciais gerados
        current_files = run_files
        while len(current_files) > 1:
            level+=1

            new_merged_files = []


            # intercalar em grupos de p tamanho 
            for i in range(0, len(current_files), self.p_ways ):

                #pode dar index of ra
                group_files = current_files[i: i+ self.p_ways]

                merged_file = self.merge_groups(group_files)
                new_merged_files.append(merged_file)

            
            #arquivos intercalados

                for arquivo in group_files:
                    try:
                        os.remove(arquivo)
                    except OSError:
                        pass

            current_files = new_merged_files
            print(f"Nivel {level} - Arquivos intercalados: {len(current_files)}")

        # Se sobrou apenas um arquivo, retorna ele 
        return current_files[0] if current_files else None
            

     
        

    def merge_groups(self, group_files, index_group=0):

        """
            intercala um grupo de até p arquivos
            Garante que no máximo p arquivos estão abertos (entrada) + 1 arquivo (saida)
        """

        if len(group_files)==1:
            return group_files[0]
        

        file_out = self.create_run_file("temp", index_group)

        # 
        input_files_merge = []

        for file in group_files:
            try:
                f = open(file, "r")
                input_files_merge.append(f)
            except FileNotFoundError:
                print(f"arquivo {file} nao encontrao")
                continue
        

        try:

            #heap para intercalar os arquivos
            # cada elemento da heap é uma tupla (valor, indice_arquivo)
            heap_merge = []

            # Inicializa a heap com o primeiro valor de cada arquivo
            for i, arquivo in enumerate(input_files_merge):
                conteudo = arquivo.readline()
                
                if conteudo:
                    valor = int(conteudo.strip())
                    # i indica indice do arquivo 
                    heapq.heappush(heap_merge, (valor,i))

            #intercala os arquivos até que a heap esteja vazia
            with open(file_out, "w") as saida:
                while heap_merge:
                    # Pega o menor elemento da heap
                    valor, indice = heapq.heappop(heap_merge)

                    # Escreve o valor no arquivo de saída
                    saida.write(f"{valor}\n")

                    # Lê o próximo valor do arquivo correspondente
                    conteudo = input_files_merge[indice].readline()
                    
                    if conteudo:
                        novo_valor = int(conteudo.strip())
                        heapq.heappush(heap_merge, (novo_valor, indice))
                    
        
        except Exception as e:
            print(f"Erro ao mesclar arquivos: {e}")
            raise e

        finally:
            # Fecha todos os arquivos de entrada    
            for file in input_files_merge:
                file.close()
            
            # remover arquivos temporários
            for file in group_files:
                try:
                    os.remove(file)
                except OSError:
                    print(f"Erro ao remover arquivo temporário: {file}")

        return file_out

    #copiar arquivo de saida para o arquivo de saida final
    def generate_output(self, file_out):
        """
        Copia o arquivo de saida temporario para o arquivo de saida final
        e excluir o arquivo temporário.
        """
        
        shutil.copy(file_out, self.output_file)
        print(f"Arquivo de saída gerado: {self.output_file}")   
        # excluir o arquivo e diretorio temporario
        try:
            shutil.rmtree("temp")
        except OSError as e:
            print(f"Erro ao remover diretório temporário: {e}")
    
    def show_stats(self):
        """
        Mostra estatisticas do processo de ordenacao


            #Regs Ways #Runs #Parses
              25   3     5      2
        """
        print(f"#Regs Ways #Runs #Parses\n"
             f" {self.total_regs}   {self.p_ways}     {self.runs}      {self.parses}")

def main():

    if len(sys.argv) != 4:
        print(f"Argumentos insuficientes\n Tente: python3 pwats_mergesort.py <p_ways> input_file.text output_file.text ")
    try:
         p_ways = int(sys.argv[1])
         input_file = (sys.argv[2])
         output_file = (sys.argv[3])

         sort = BalancedSorterPways(p_ways, input_file, output_file)
         sort.sort()
    except Exception as e: 
        print(f"Error {e}")


if __name__ == "__main__":
    main()