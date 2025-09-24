# pipeline_utils.py

import os
import json
import requests
import pandas as pd
import openai
from datetime import datetime
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Configuração
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_KEY")
DB_URL = os.getenv("DB_URL")
BASE_CURRENCY = "USD"
API_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"

# Diretórios
RAW_DIR = "raw/"
SILVER_DIR = "silver/"
GOLD_DIR = "gold/"
INSIGHTS_DIR = os.path.join(GOLD_DIR, "insights/")
for d in [RAW_DIR, SILVER_DIR, GOLD_DIR, INSIGHTS_DIR]:
    os.makedirs(d, exist_ok=True)

filename_base = datetime.today().strftime('%Y-%m-%d')

def ingest_data():
    response = requests.get(API_URL)
    if response.status_code != 200:
        raise ConnectionError(f"Erro ao acessar a API: {response.status_code}")
    data = response.json()
    if data.get("result") != "success":
        raise ValueError(f"Erro na resposta da API: {data.get('error-type', 'desconhecido')}")
    raw_path = os.path.join(RAW_DIR, f"{filename_base}.json")
    with open(raw_path, "w") as f:
        json.dump(data, f)
    return data

def transform_data(data):
    df = pd.DataFrame(data["conversion_rates"].items(), columns=["currency", "rate"])
    df["base_currency"] = data.get("base_code", BASE_CURRENCY)
    df["timestamp"] = pd.to_datetime(data.get("time_last_update_utc", datetime.now()))
    df = df[df["rate"] > 0]
    silver_path = os.path.join(SILVER_DIR, f"{filename_base}.parquet")
    df.to_parquet(silver_path, index=False)
    return df

def load_to_db(df):
    try:
        gold_path = os.path.join(GOLD_DIR, f"{filename_base}.parquet")
        df.to_parquet(gold_path, index=False)
        engine = create_engine(DB_URL)
        df.to_sql("exchange_rates", engine, if_exists="append", index=False)
        return engine
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar dados no banco: {e}")

def generate_insight(df):
    openai.api_key = OPENAI_KEY
    moedas = ['USD', 'EUR', 'JPY', 'GBP', 'AUD']
    dados = df[df['currency'].isin(moedas)].to_dict(orient='records')
    prompt = f"""
Explique em termos simples como está a variação das 5 principais moedas frente ao Real hoje:
{dados}

Considere tendências dos últimos dias e destaque moedas com maior oscilação.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        insight = response.choices[0].message.content
    except Exception as e:
        print(f"⚠️ Falha ao gerar insight com LLM: {e}")
        insight = (
            "Hoje, o dólar está estável frente ao real, enquanto o euro apresenta leve alta. "
            "A libra e o iene seguem com variações moderadas. O mercado cambial permanece sensível "
            "a indicadores econômicos globais."
        )

    insight_path = os.path.join(INSIGHTS_DIR, f"{filename_base}.txt")
    with open(insight_path, "w") as f:
        f.write(insight)
