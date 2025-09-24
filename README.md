# 💱 Pipeline de Cotações Cambiais com LLM e Streamlit

Este projeto realiza a coleta de dados de câmbio via API, transforma e armazena os dados em banco, gera insights com uma LLM (modelo de linguagem) e apresenta tudo em um dashboard interativo com Streamlit.


## 📂 Estrutura do projeto

```plaintext
pipeline-cambio/
├── raw/                  # Dados brutos
├── silver/               # Dados transformados
├── gold/                 # Dados finais
│   └── insights/         # Relatórios gerados pela LLM
├── .env.example          # Exemplo de configuração (sem dados reais)
├── run_pipeline.py       # Executa o pipeline completo
├── dashboard.py          # Executa o Streamlit
├── pipeline_utils.py     # Funções reutilizáveis
├── README.md             # Documentação do projeto



## 🧠 Tecnologias utilizadas


- Python
- Pandas
- Requests
- SQLAlchemy
- OpenAI API
- ExchangeRate API
- Streamlit
- dotenv
- PostgreSQL (ou outro banco compatível)

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LilianSouza/pipeline-cambio.git
cd pipeline-cambio

Instale as dependências:

pip install -r requirements.txt

Crie um arquivo requirements.txt com:

pandas
requests
python-dotenv
openai
sqlalchemy
streamlit

🔐 Configuração das chaves 

 Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

EXCHANGE_API_KEY=coloque_sua_chave_da_api_de_cambio_aqui
OPENAI_KEY=coloque_sua_chave_da_openai_aqui
DB_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco



🚀 Execução do pipeline

Para rodar o pipeline completo (ingestão, transformação, carga e geração de insight):

python run_pipeline.py

Esse script irá:

- 🔄 Buscar os dados da API de câmbio
- 🧹 Transformar e salvar os dados em formato Parquet
- 🗄️ Inserir os dados no banco de dados
- 🧠 Gerar um insight com LLM (ou texto padrão, caso a API falhe)

📊 Visualização do dashboard

Para abrir o dashboard interativo com Streamlit:

streamlit run dashboard.py

Você poderá:

- 📅 Selecionar a data desejada
- 💱 Visualizar as cotações das moedas
- 🧠 Ler o insight gerado pela LLM

📁 Arquivos gerados
Os arquivos finais ficam na pasta /gold/:

gold/YYYY-MM-DD.parquet → dados limpos

gold/insights/YYYY-MM-DD.txt → relatório gerado pela LLM

📄 Licença
Este projeto é de uso acadêmico e não possui licença de distribuição comercial.