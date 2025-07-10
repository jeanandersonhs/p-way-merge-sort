import os

def clean_output_file(filename="output_file.txt"):
    with open(filename, 'w') as f:
        pass
    print(f"Arquivo {filename} limpo com sucesso!")

if __name__ == "__main__":
    clean_output_file()
