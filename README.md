
<p align=center> <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white""> <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black"> <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white"> <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white"> <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"> <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/statsmodels-%230C55A5.svg?style=for-the-badge&logoColor=white">
  </ul>
  <br> <br>
</p>



<p align="center">
  <img height="60" src="https://static.wixstatic.com/media/924126_5f1bb95cd3db48f7a9f55feade3cd4fc~mv2.png/v1/crop/x_0,y_43,w_500,h_414/fill/w_134,h_111,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/a863-removebg-preview.png">
  <br>
</p>


<!-- <p align="center">
  <img height="9" src=" "> &
  <img height="13" src=" ">
</p> -->


# 📚 Trilha Inicial Ciência de Dados Jr
Este projeto tem como objetivo realizar uma análise básica de dados utilizando Python, explorando um conjunto de dados pré-definido para extrair insights simples através de estatísticas descritivas e visualizações gráficas.


---


# Solução do Case

### Notebook 

Para solucionar o case foi usado o Jupyter notebook, para ter acesso a análise exploratória completa [Click aqui](https://github.com/Oseiasdfarias/TrilhaDadosJR-JUN15/blob/main/notebook/analise_de_dados_vendas_cursos_online.ipynb) ou acesse a pasta `notebook` este repositório. A análise possui explicações para cada célula de código implementada no notebbok.

<p align="center">
  <img width="90%" src="./reports/demo_notebook.png">
</p>

#### Resumo da Análise Exploratória

+ ***Visualização do DataFrame usando o método `head()`.***

 ```python
  df_vendas.head()
 ```

<div>
<!-- <style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style> -->
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Nome do Curso</th>
      <th>Quantidade de Vendas</th>
      <th>Preço Unitário</th>
      <th>Data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Introdução à Programação em Python</td>
      <td>50</td>
      <td>39.9</td>
      <td>2023-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Desenvolvimento Web com HTML e CSS</td>
      <td>30</td>
      <td>59.9</td>
      <td>2023-01-02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>JavaScript Avançado: Frameworks e Bibliotecas</td>
      <td>20</td>
      <td>79.9</td>
      <td>2023-01-03</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Introdução ao Machine Learning</td>
      <td>15</td>
      <td>99.9</td>
      <td>2023-01-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Desenvolvimento Mobile com React Native</td>
      <td>25</td>
      <td>69.9</td>
      <td>2023-01-05</td>
    </tr>
  </tbody>
</table>
</div>



 + ***Obtendo o detalhamento do DataFrame usando o método `info()`.***

 ```python
  df_vendas.info()
 ```

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 5 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   ID                    25 non-null     int64  
 1   Nome do Curso         25 non-null     object 
 2   Quantidade de Vendas  25 non-null     int64  
 3   Preço Unitário        25 non-null     float64
 4   Data                  25 non-null     object 
dtypes: float64(1), int64(2), object(2)
memory usage: 1.1+ KB
```


 + ***Obtendo resumo estatístico da base de dados para as columas `Quantitativas`***

 ```python
  df_vendas.describe()
 ```


<div>
<!-- <style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style> -->
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Quantidade de Vendas</th>
      <th>Preço Unitário</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>25.000000</td>
      <td>25.000000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>13.000000</td>
      <td>17.960000</td>
      <td>83.900000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.359801</td>
      <td>10.921996</td>
      <td>21.984843</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>39.900000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.000000</td>
      <td>10.000000</td>
      <td>69.900000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>13.000000</td>
      <td>15.000000</td>
      <td>79.900000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.000000</td>
      <td>20.000000</td>
      <td>99.900000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>50.000000</td>
      <td>119.900000</td>
    </tr>
  </tbody>
</table>
</div>


+ ***Distribuição da Variável Quantidade de Vendas***

```python
plt.figure(figsize=(9, 4))
cores = ["#0A66C2", "#ECF7AE", "#1AA0DB", "#8BD5DB"]
sns.set_palette(sns.color_palette(cores))
ax= sns.histplot(df_vendas["qt_de_vendas"], bins=10, kde=True, color=cores[-2])
sns.despine(right=True)

plt.title("Distribuição da Variável Quantidade de Vendas", fontsize=12)
plt.xlabel("Quantidade de Vendas")
plt.ylabel("Quantidade")
plt.show()
```

<p align="center">
<br>
  <img width="90%" src="./reports/output_distrib-vendas.png">
</p>



+ ***Distribuição da Variável Preço Unitário***

```python
plt.figure(figsize=(9, 4))
sns.set_palette(sns.color_palette(cores))
ax= sns.histplot(df_vendas["preco_unitario"], bins=8, kde=True, color=cores[-2])
sns.despine(right=True)

plt.title("Distribuição da Variável Preço Unitário", fontsize=12)
plt.xlabel("Preço Unitário")
plt.ylabel("Quantidade")
plt.show()
```

<p align="center">
<br>
  <img width="90%" src="./reports/output_preco_unit.png">
</p>



+ ***1. Calcular a receita total gerada pela venda dos cursos.***


```python
print(f"Receita Total das Vendas: {np.sum(df_vendas.qt_de_vendas*df_vendas.preco_unitario):.2f}")
```

Saída:

```
Receita Total das Vendas: 32735.10
```


+ ***2. Identificar o curso com o maior número de vendas.***

```python
df_qt_vendas = (df_vendas.groupby("nome_curso")["qt_de_vendas"]
 .sum()
 .sort_values(ascending=False)
 .to_frame()
 .reset_index())
df_qt_vendas

print(f"Curso com o maior número de vendas| {df_qt_vendas.nome_curso[0]} | Qt: {df_qt_vendas.qt_de_vendas[0]}")

```

Saída:

```
Curso com o maior número de vendas| Introdução à Programação em Python | Qt: 95

```


+ ***3. Visualizar a distribuição das vendas ao longo do tempo através de gráficos.***

```python
plt.figure(figsize=(9, 4))

ax = sns.barplot(data=df_vendas, x="data", y="qt_de_vendas")


ax.bar_label(ax.containers[0])
ax.set(xlabel="Data", ylabel="Quantidade")
plt.title("Distribuição das Vendas ao Longo do Tempo", fontsize=12)
plt.xticks(rotation=90)
sns.despine(right=True)
plt.show()
```

<p align="center">
<br>
  <img width="90%" src="./reports/output_venda_data.png">
</p>

### Pré-Processamento dos Dados 

Além da análise exploratória dos dados, foi implementado um scritp python para o pré-processamento dos dados afim de ser consumido por um Dashboard, o script está no pasta `src` que realiza as seguintes transformações.


1. Renovea as colunas para facilitar o uso em códigos;
2. Converte a coluna `Data` no tipo `datetime`;
3. Cria uma nova coluna `valor_vendas`, contendo os valores de venda;
4. Salva os dados tratado no subpasta `data/gold`.


```python
import pandas as pd


df_vendas = pd.read_csv("./data/silver/dados_vendas_cursos_online.csv")


df_vendas = df_vendas.rename(columns={
    "Nome do Curso": "nome_curso",
    "Quantidade de Vendas": "qt_de_vendas",
    "Preço Unitário": "preco_unitario",
    "Data": "data"})


df_vendas["data"] = pd.to_datetime(df_vendas["data"], format='%Y-%m-%d')

print(f"Tipo do dado após conversão: {df_vendas['data'].dtypes}")
print(f"Amostrar para visualização {df_vendas['data'][1]}")


df_vendas["valor_vendas"] = df_vendas.qt_de_vendas*df_vendas.qt_de_vendas


df_vendas.to_csv("./data/gold/tratados_dados_vendas_cursos_online.csv",
                 index=False)

```


### Dashboard

Por fim, foi implementado um Dashboard usando `Streamlit` para melhor visualização dos insights.

<p align="center">
  <img width="90%" src="./reports/demo_dashboard.png">
</p>



---


<p align="center">
<br>
  <img width="90%" src="https://utfs.io/f/3b2340e8-5523-4aca-a549-0688fd07450e-j4edu.jfif">
</p>



---

<h3  id="id9">🎥 Rede Social</h3>

<p align=center> <a href="https://oseiasfarias.info"><img src="https://img.shields.io/badge/Portfólio-%230077B5.svg?style=for-the-badge&logoColor=white"></a> <a href="https://www.linkedin.com/in/oseiasfarias/"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://oseiasfarias.medium.com"><img src="https://img.shields.io/badge/Medium-%230077B5.svg?style=for-the-badge&logo=medium&logoColor=white"></a>
<a href="https://www.kaggle.com/osiasdfarias"><img src="https://img.shields.io/badge/Kaggle-%230077B5.svg?style=for-the-badge&logo=kaggle&logoColor=white"></a>
</p>