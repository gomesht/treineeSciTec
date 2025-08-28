import streamlit as st
import pandas as pd

st.title("Painel de Filtros e Visualização da Planilha")

# Verifica se o dataframe está no session_state
if 'df' not in st.session_state or st.session_state.df.empty:
    st.warning("Base de dados não carregada. Volte para a página principal.")
    st.stop()

df = st.session_state.df

# --- Barra Lateral de Filtros (Sidebar) ---
# Usar a sidebar é uma ótima prática de layout para não poluir a página principal.
st.sidebar.header("Filtros")

# Filtro por Gênero (Multiselect)
gender_filter = st.sidebar.multiselect(
    "Gênero:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Filtro por Localização (Multiselect)
location_filter = st.sidebar.multiselect(
    "Localização:",
    options=df["Urban_or_Rural"].unique(),
    default=df["Urban_or_Rural"].unique()
)

# Filtro por Dispositivo (Multiselect)
device_filter = st.sidebar.multiselect(
    "Dispositivo Principal:",
    options=df["Primary_Device"].unique(),
    default=df["Primary_Device"].unique()
)

# Filtro por Idade (Slider)
age_slider = st.sidebar.slider(
    "Intervalo de Idade:",
    min_value=int(df["Age"].min()),
    max_value=int(df["Age"].max()),
    value=(int(df["Age"].min()), int(df["Age"].max()))
)

# --- Lógica de Filtragem ---
# Aplica os filtros ao dataframe. A sintaxe com @variável permite uma leitura mais clara.
df_filtered = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Urban_or_Rural"].isin(location_filter)) &
    (df["Primary_Device"].isin(device_filter)) &
    (df["Age"] >= age_slider[0]) &
    (df["Age"] <= age_slider[1])
]

# --- Exibição dos Dados ---
st.subheader("Dados Filtrados")
st.write(f"Exibindo **{df_filtered.shape[0]}** de **{df.shape[0]}** registros.")

# st.dataframe é ideal para exibir tabelas interativas.
st.dataframe(df_filtered, use_container_width=True)