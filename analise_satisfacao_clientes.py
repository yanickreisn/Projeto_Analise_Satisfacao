# análise_satisfacao_clientes.py

#  1. Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo dos gráficos
plt.style.use('seaborn-vibrant')
sns.set_theme()

#  2. Leitura dos dados (após upload do arquivo no Colab)
df = pd.read_excel("satisfacao_clientes.xlsx")

#  3. Preparação dos dados
df["Data da Pesquisa"] = pd.to_datetime(df["Data da Pesquisa"])

bins = [0, 17, 25, 35, 50, 100]
labels = ["<18", "18-25", "26-35", "36-50", "50+"]
df["Faixa Etária"] = pd.cut(df["Idade"], bins=bins, labels=labels)

#  4. Visualizações

# 4.1 Nota média por região
plt.figure(figsize=(8,5))
df.groupby("Região")["Nota_Satisfacao"].mean().plot(kind='bar', color='cornflowerblue')
plt.title("Nota Média por Região")
plt.ylabel("Nota")
plt.xlabel("Região")
plt.tight_layout()
plt.savefig("nota_media_regiao.png")
plt.show()

# 4.2 Proporção de recomendação (pizza)
plt.figure(figsize=(6,6))
df["Recomenda"].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'salmon'])
plt.title("Clientes que Recomendam a Empresa")
plt.ylabel("")
plt.tight_layout()
plt.savefig("proporcao_recomendacao.png")
plt.show()

# 4.3 Nota média por faixa etária
plt.figure(figsize=(8,5))
df.groupby("Faixa Etária")["Nota_Satisfacao"].mean().plot(kind='bar', color='orange')
plt.title("Nota Média por Faixa Etária")
plt.ylabel("Nota")
plt.xlabel("Faixa Etária")
plt.tight_layout()
plt.savefig("nota_media_faixa_etaria.png")
plt.show()

# 4.4 Evolução da satisfação semanal
plt.figure(figsize=(10,5))
df.set_index("Data da Pesquisa").resample("W")["Nota_Satisfacao"].mean().plot(marker='o', linestyle='-', color='purple')
plt.title("Evolução da Satisfação Semanal")
plt.ylabel("Nota")
plt.xlabel("Data")
plt.grid(True)
plt.tight_layout()
plt.savefig("evolucao_semanal.png")
plt.show()

#  5. Desafio Extra

# 5.1 Taxa de recomendação por faixa etária
tabela_taxa = df.groupby("Faixa Etária")["Recomenda"].value_counts(normalize=True).unstack() * 100
print("\n Taxa de recomendação por faixa etária:")
print(tabela_taxa.round(2))

# 5.2 Relação entre nota e recomendação (boxplot)
plt.figure(figsize=(8,5))
sns.boxplot(x="Recomenda", y="Nota_Satisfacao", data=df, palette="Set2")
plt.title("Distribuição das Notas por Recomendação")
plt.tight_layout()
plt.savefig("boxplot_recomendacao.png")
plt.show()

# Comparativo das médias
print("\n Média das notas por recomendação:")
print(df.groupby("Recomenda")["Nota_Satisfacao"].mean())

#  Fim do código.
