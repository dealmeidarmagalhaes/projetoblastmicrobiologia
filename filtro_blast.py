import re
from datetime import datetime

caminho_arquivo = "/home/ricardo/resultado_real.txt"
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

try:
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            if linha.startswith(">") and re.search(r"NDM-1\b", linha):
                gene = linha.replace(">", "").strip()
                
                # CRIAÇÃO DO LAUDO
                with open("laudo_final.txt", "w") as laudo:
                    laudo.write(f"RELATÓRIO DE VIGILÂNCIA GENÔMICA\n")
                    laudo.write(f"Data: {data_atual}\n")
                    laudo.write(f"Responsável: Ricardo\n")
                    laudo.write(f"Resultado: POSITIVO para {gene}\n")
                    laudo.write(f"Status: Alerta de resistência detectado.\n")
                
                print("✅ Laudo gerado com sucesso em: laudo_final.txt")
                break
except Exception as e:
    print(f"Erro: {e}")
