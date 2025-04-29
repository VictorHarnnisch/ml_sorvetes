import pandas as pd

# Criando os dados completos
dados = {
    "Data": pd.date_range(start="01/01/2025", periods=100, freq="D").strftime("%d/%m/%Y").tolist(),
    "Vendas de Sorvetes (unidades)": [45, 50, 38, 25, 60, 58, 65, 30, 40, 70] * 10,
    "Temperatura (ºC)": [32, 33, 30, 28, 35, 34, 36, 29, 31, 37] * 10
}

# Criando DataFrame
df = pd.DataFrame(dados)

# Salvando como TSV (Tab-Separated Values)
df.to_csv("vendas_sorvetes.tsv", sep="\t", index=False)

print("Arquivo vendas_sorvetes.tsv gerado com sucesso!")


# Lendo o arquivo TSV gerado anteriormente
# Certifique-se de que 'vendas_sorvetes.tsv' está na mesma pasta onde você roda este script
try:
    df = pd.read_csv("vendas_sorvetes.tsv", sep="\t")
    print("Arquivo TSV lido com sucesso.")
except FileNotFoundError:
    print("Erro: Arquivo 'vendas_sorvetes.tsv' não encontrado. Certifique-se de que ele está na mesma pasta.")
    exit() # Sai do script se o arquivo não for encontrado

# Salvando como CSV (Comma Separated Values)
# O delimitador padrão do to_csv é a vírgula (,), que é o padrão para CSV
df.to_csv("vendas_sorvetes.csv", index=False)

print("Arquivo convertido para CSV ('vendas_sorvetes.csv') gerado com sucesso!")