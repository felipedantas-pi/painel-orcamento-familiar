import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime, date

from streamlit_option_menu import option_menu

from components import config

# Set page configuration
st.set_page_config(
  page_title="Orçamento App",
  page_icon=":bar_chart:",
  layout="wide",
  initial_sidebar_state="expanded",
)

# Difine styles for the app
styles = """
<style>
img {
  max-width: 50%;
}
.sidebar .sidebar-content {
  max-width: 50%;
  background-color: #f5f5f5;
}
</style>
"""

# Render styles
st.markdown(styles, unsafe_allow_html=True)

sidebar_container = st.container()
with sidebar_container:
  st.sidebar.title("MyBudget")
  st.sidebar.write("by Felipe Dantas")
  st.sidebar.image("./assets/img_fam.png", use_column_width="always")
  #st.sidebar.markdown("---")

pages_names = ['Receitas', 'Despesas']

# left_sid_col, right_sid_col = st.sidebar.columns(2)
# with left_sid_col:
#   st.button(f":green[{pages_names[0]}]")
  
# with right_sid_col:
#   st.button(f":red[{pages_names[1]}]")

with st.sidebar:
  selected = option_menu(
    menu_title = "Meu Orçamento",
    options = ["Receitas", "Despesas", "Cartões de Crédito"],
    default_index = 0,
    menu_icon = 'coin',
    icons=['graph-up-arrow','graph-down-arrow','credit-card-2-front'],
    styles={
      "container": {"padding": "0!important", "background-color": "#262730"},
      "menu-title": {"font-size": "20px"},
      "icon": {"color": "orange", "font-size": "15px"}, 
      "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#a2a2a2"},
      "nav-link-selected": {"background-color": "green"},
    }
  )

dashboard, filtros = st.tabs(["📈 Painel", "Filtros"])

if selected == 'Receitas':
  df_receita = config.load_dataset('receita')
  dashboard.dataframe(df_receita, use_container_width=True)
  
if selected == 'Despesas':
  df_despesa = config.load_dataset('despesa')
  dashboard.dataframe(df_despesa, use_container_width=True)

