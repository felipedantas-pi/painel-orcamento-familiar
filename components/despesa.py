import streamlit as st
import pandas as pd
from datetime import datetime

# Carregador os dados
#@st.cache_data
def load_despesa(sheet_name):
  df = pd.read_excel(
      io='dataset/dataset_full.xlsx',
      engine='openpyxl',
      sheet_name=sheet_name,
  )
  df.insert(1, column='mes', value=df["data"].dt.month)
  df['data'] = df['data'].sort_values().dt.date
  return df

# df_despesa = load_despesa('despesa')
# #st.dataframe(df_receita)

# # ---- SIDEBAR ------
# # Filtros
# st.sidebar.header("Filtre Aqui:")

# # Filtro de data: mês

# mes = st.sidebar.multiselect(
#   "Selecione o mês: ",
#   options = df_despesa["mes"].sort_values().unique(),
#   default = df_despesa["mes"].sort_values().unique(),
# )

# # Filtro de conta
# conta = st.sidebar.multiselect(
#   "Selecione a conta: ",
#   options = df_despesa["conta"].sort_values().unique(),
#   default = df_despesa["conta"].sort_values().unique()
# )

# #Filtros de categoria
# categoria = st.sidebar.multiselect(
#   "Selecione a categoria: ",
#   options = df_despesa["categoria"].sort_values().unique(),
#   default = df_despesa["categoria"].sort_values().unique()
# )

# df_despesa_selection = df_despesa.query(
#   "mes==@mes & conta==@conta & categoria==@categoria"
# )

# # ----- Página Principal -----
# # Titulo
# st.title(":bar_chart: Dashboard do Orçamento 2023")
# st.markdown("##")

# # Indicadores
# despesa_total = int(df_despesa_selection["valor_atual"].sum())

# left_colunm, middle_colunm, right_colunm = st.columns(3)
# with left_colunm:
#   st.subheader("Total Receita:")
#   st.subheader(f"R$ {despesa_total:,.2f}".replace(",","_").replace(".", ",").replace("_", "."))