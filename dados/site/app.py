import streamlit as st  
import pandas as pd


if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_parquet('Indian_Kids_Screen_Time_Optimized.parquet')  

pg = st.navigation([
    st.Page("pages/page1.py", title="Dashboard", icon="📊"),
    st.Page("pages/page2.py", title="Adicionar Dados", icon="➕"),
    st.Page("pages/page3.py", title="Filtrar Planilha", icon="🔍"),
])
pg.run()