import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd
import numpy as np
import plotly.express as px


class Dashboard:
    """
    Classe que implementa o Dashboard.

    Atributo:
        estrutura_db: Cria a estrutura do Dashboard.
    """
    def __init__(self, df) -> None:
        """
        Iniciador da classe.

        Args:
            df: DataFrame pandas com os dados para
            serem mostrados no Dashboard.
        Returns:
            Renorna um None.
        """
        self.df = df
        self.pg_title = "Vendas de Cursos Online"
        st.set_page_config(page_title=self.pg_title,
                           layout="wide",
                           initial_sidebar_state="collapsed")
        self.pages = ["Docs", "Portfólio", "LinkedIn", "GitHub"]
        self.styles = {
            "nav": {
                "background-color": "#44475a",
            },
            "div": {
                "max-width": "32rem",
            },
            "span": {
                "border-radius": "0.5rem",
                "color": "#EFEFEF",
                "margin": "0 0.125rem",
                "padding": "0.4375rem 0.625rem",
            },
            "active": {
                "background-color": "rgba(255, 255, 255, 0.25)",
            },
            "hover": {
                "background-color": "rgba(255, 255, 255, 0.35)",
            }
        }
        self.options = {
            "show_menu": False,
            "show_sidebar": False,
        }

        self.urls = {
            "Docs": "#",
            "GitHub": "https://github.com/Oseiasdfarias/ETL-Ecommerce-produtos",  # noqa: E501
            "LinkedIn": "https://www.linkedin.com/in/oseiasfarias/",
            "Portfólio": "https://oseiasfarias.info"}
        self.page = st_navbar(self.pages, styles=self.styles,
                              urls=self.urls, options=self.options)

        # Título da aplicação
        st.title('Vendas de Cursos Online')
        self.estrutura_db()

    def estrutura_db(self):
        """Método responável por implementar a estrutura do Dashboard."""
        # Melhorar o layout com colunas para KPIs
        st.subheader("KPIs Principais")
        col1, col2 = st.columns(2)

        # KPI 1: Número Total de vendas
        total_items = round(np.sum(df.qt_de_vendas*df.preco_unitario), 2)
        col1.metric(label="Número Total de Vendas (R$)", value=total_items)

        # KPI 2: curso com o maior número de vendas
        curso_mvendido = (df.groupby("nome_curso")["qt_de_vendas"]
                          .sum()
                          .sort_values(ascending=False)
                          .to_frame()
                          .reset_index())

        col2.metric(label="Curso mais Vendido: " + curso_mvendido.loc[0]["nome_curso"] + " (UN)",  # noqa: E501
                    value=curso_mvendido.loc[0]["qt_de_vendas"])

        # Distribuição das Vendas por curso
        df_venda_total_por_curso = (df.groupby("nome_curso")["valor_vendas"]
                                    .sum()
                                    .to_frame()
                                    .sort_values("valor_vendas")
                                    .reset_index())
        st.subheader('Distribuição das Vendas por curso')
        col1, col2 = st.columns([6, 6])
        fig = px.bar(df_venda_total_por_curso,
                     x='valor_vendas',
                     y='nome_curso',
                     orientation='h',
                     text_auto='.2s')
        col1.plotly_chart(fig)
        col2.write(df_venda_total_por_curso.sort_values(
            "valor_vendas", ascending=False))

        # Visualizar a distribuição das
        # vendas ao longo do tempo através de gráficos.
        st.subheader('Distribuição das Vendas ao Longo do Tempo')
        col1, col2 = st.columns([6, 3])

        fig1 = px.bar(df, x='data',
                      y='qt_de_vendas',
                      text_auto='.2s')
        col1.plotly_chart(fig1)
        col2.write(df[["data", "qt_de_vendas"]])


if __name__ == "__main__":

    df = pd.read_csv("./data/gold/tratados_dados_vendas_cursos_online.csv")

    dash = Dashboard(df)
