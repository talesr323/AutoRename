import os
import json
import re

folder = r'C:\Users\Windows10\Desktop\Nova pasta\\'

nome = '''
{
  "02168787000120": "A. F. Auto Mecânica",
  "07682215000189": "Baby Anjo",
  "": "Boa Carne",
  "": "Baby Soffete",
  "": "Funilaria  Parpinelli",
  "": "HIDROBRAS",
  "55774590000100": "IMPE",
  "": "GILZA CLELIA GAJARDONI RODRIGUES",
  "": "PIETRO GAJARDONI RODRIGUES - ME",
  "": "PABLO GAJARDONI RODRIGUES - ME",
  "": "Neide Presentes",
  "": "Rocha Transportes",
  "": "Steel Prime",
  "": "Terra Forte",
  "": "Transsolar Energia Solar",
  "": "Wm Representações",
  "": "MC Injetados",
  "": "Import Tênis",
  "": "Birigui Piscinas",
  "": "JACOMO BOTAS",
  "": "JORGE FUHRMANN",
  "": "DOM ORIONE",
  "": "RELUBIA"
}
'''

# Carregue o JSON
dados_json = json.loads(nome)

# Função para extrair o CNPJ de uma string
def extrair_cnpj(nome_arquivo):
    padrao_cnpj = r'\d{14}'  # Procura 14 dígitos em sequência, que é o formato de um CNPJ
    resultados = re.findall(padrao_cnpj, nome_arquivo)
    if resultados:
        return resultados[0]  # Retorna o primeiro CNPJ encontrado
    return None

# Itere sobre os arquivos na pasta
for file_name in os.listdir(folder):
    old_name = os.path.join(folder, file_name)

    # Verifique se o arquivo é um arquivo regular
    if os.path.isfile(old_name):
        cnpj_arquivo = extrair_cnpj(file_name)

        if cnpj_arquivo:
            # Procure o CNPJ no JSON
            if cnpj_arquivo in dados_json:
                novo_nome = dados_json[cnpj_arquivo] + "_" + cnpj_arquivo + os.path.splitext(file_name)[1]
                new_name = os.path.join(folder, novo_nome)

                # Lidar com possíveis conflitos de nome
                counter = 1
                while os.path.exists(new_name):
                    novo_nome = f"{dados_json[cnpj_arquivo]}_{cnpj_arquivo}_{counter}" + os.path.splitext(file_name)[1]
                    new_name = os.path.join(folder, novo_nome)
                    counter += 1

                # Renomeie o arquivo
                os.rename(old_name, new_name)
                print(f"Arquivo renomeado: {file_name} -> {novo_nome}")
