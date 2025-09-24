# dashboard.py

import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine

DB_URL = st.secrets["DATABASE_URL"]

st.set_page_config(page_title="Cotações Cambiais", layout="wide")
st.title("📈 Dashboard de Cotações Cambiais")

engine = create_engine(DB_URL)
df_db = pd.read_sql("SELECT * FROM exchange_rates", engine)
datas = df_db["timestamp"].dt.date.unique()
data_selecionada = st.selectbox("Selecione a data", sorted(datas, reverse=True))
df_filtrado = df_db[df_db["timestamp"].dt.date == data_selecionada]

st.subheader(f"Cotações em {data_selecionada}")
st.dataframe(df_filtrado)
st.bar_chart(df_filtrado.set_index("currency")["rate"])

insight_path = os.path.join(INSIGHTS_DIR, f"{data_selecionada}.txt")
if os.path.exists(insight_path):
    with open(insight_path, "r") as f:
        insight_text = f.read()
    st.subheader("🧠 Insight da LLM")
    st.write(insight_text)
else:
    st.warning("Insight da LLM não encontrado para esta data.")
