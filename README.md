# Pipeline de Cotações Cambiais com LLM e Streamlit

Este projeto foi desenvolvido como parte de um desafio acadêmico para aplicar conceitos de engenharia de dados, integração com modelos de linguagem (LLMs) e visualização interativa com Streamlit.

## 📌 Objetivo

Construir um pipeline completo que:

-Coleta dados de cotações cambiais

-Realiza transformações e enriquecimento

-Gera insights com auxílio de LLMs (OpenAI)

-Exibe os resultados em um dashboard interativo

## 🧰 Tecnologias utilizadas

-Python

-Pandas

-SQLAlchemy

-OpenAI API

-Streamlit

-Requests

-Datetime

-Matplotlib / Seaborn

## 🗂️ Estrutura do projeto

```
├── raw/           # Dados brutos
├── silver/        # Dados tratados
├── gold/          # Dados enriquecidos
├── insights/      # Resultados gerados com LLM
├── pipeline_utils.py
├── run_pipeline.py
├── dashboard.py
├── README.md
└── .gitignore
```



## ⚙️ Como executar o projeto

### 1. Clone o repositório

```
git clone https://github.com/LilianSSouza/pipeline-cambio.git
cd pipeline-cambio
```

### 2. Instale as dependências

```
pip install -r requirements.txt
```

Se você não tiver um arquivo requirements.txt, pode instalar manualmente:

```
pip install pandas sqlalchemy openai streamlit requests matplotlib seaborn
```

### 3. Configure suas variáveis de ambiente

Crie um arquivo .env com sua chave da OpenAI:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Este arquivo está no .gitignore e não será enviado ao GitHub.

### 4. 🚀 Execute o pipeline

```
python run_pipeline.py
```

Esse script irá:

🔄 Buscar os dados da API de câmbio

🧹 Transformar e salvar os dados em formato Parquet

🗄️ Inserir os dados no banco de dados

🧠 Gerar um insight com LLM (ou texto padrão, caso a API falhe)

### 5. 📊 Inicie o dashboard

```
streamlit run dashboard.py
```

Você poderá:

📅 Selecionar a data desejada

💱 Visualizar as cotações das moedas

🧠 Ler o insight gerado pela LLM


## 🌐 Acesse o dashboard online

```
👉 [Acesse o dashboard aqui](https://pipeline-cambio.streamlit.app)
```

## 📁 Arquivos gerados


Os arquivos finais ficam na pasta /gold/:

gold/YYYY-MM-DD.parquet → dados limpos

gold/insights/YYYY-MM-DD.txt → relatório gerado pela LLM

## 📄 Licença
Este projeto é de uso acadêmico .
