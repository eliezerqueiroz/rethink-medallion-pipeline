import os

# Pega o diretório atual onde o projeto está rodando
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define os caminhos
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
BRONZE_DIR = os.path.join(BASE_DIR, "delta", "bronze")
SILVER_DIR = os.path.join(BASE_DIR, "delta", "silver")
GOLD_DIR = os.path.join(BASE_DIR, "delta", "gold")