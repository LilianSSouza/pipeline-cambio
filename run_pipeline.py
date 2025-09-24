# run_pipeline.py

from pipeline_utils import ingest_data, transform_data, load_to_db, generate_insight

if __name__ == "__main__":
    try:
        raw_data = ingest_data()
        df = transform_data(raw_data)
        engine = load_to_db(df)
        generate_insight(df)
        print("✅ Pipeline executado com sucesso!")
    except Exception as e:
        print(f"❌ Erro no pipeline:", e)
