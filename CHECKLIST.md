# Plano de Implementação: Pipeline Medallion Rethink

## Fase 0: Setup e Arquitetura Base

- [X] **Repositório Git:** Criar o repositório e configurar um `.gitignore` rigoroso (ignorando diretórios como `data/`, `delta/`, `__pycache__/`, e arquivos `*.log`).
- [X] **Estrutura de Diretórios:** Criar as pastas base do projeto (`data/raw/`, `delta/bronze/`, `delta/silver/`, `delta/gold/`, `output/`).
- [X] **Ingestão de Arquivos:** Fazer o download dos 7 datasets do Olist e alocá-los em `data/raw/`.
- [X] **Configuração Centralizada:** Criar o arquivo `config.py` para mapear todos os caminhos locais, facilitando a transição futura para o DBFS (Databricks).
- [X] **Instalar dependências:** pip install pyspark delta-spark
---

## Fase 1: O "Motor" do Pipeline (Utils)

- [ ] **Arquivo:** `spark_utils.py`
- [ ] **Objetivo:** Criar um módulo focado na inicialização modular da `SparkSession`.
- [ ] **Configuração:** Injetar as dependências e *jars* do Delta Lake (`delta-spark`) para permitir operações ACID no ambiente local.

---

## Fase 2: Camada Bronze (A Ingestão Bruta)

- [ ] **Arquivo:** `01_bronze.py`
- [ ] **Ler os 7 arquivos CSV originais** de forma iterativa.
- [ ] **Adicionar a coluna de metadados** `ingestion_timestamp` com o horário de processamento.
- [ ] **Salvar os DataFrames** no formato Delta em `delta/bronze/` (sem aplicar regras de negócio ou filtros de limpeza).

---

## Fase 3: Camada Silver (Limpeza e Consolidação)

- [ ] **Arquivo:** `02_silver.py`
- [ ] **Ler** as tabelas da camada Bronze.
- [ ] **Aplicar tipagem correta** em colunas de data.
- [ ] **Remover valores nulos** em chaves primárias/estrangeiras (ex: `order_id`).
- [ ] **Realizar deduplicação** e manter apenas os pedidos com *status* `delivered` ou `shipped`.
- [ ] **Criar e salvar** a tabela `orders_consolidated` (via *join* das entidades principais).
- [ ] **Criar e salvar** a tabela agregada `payments_summary`.

---

## Fase 4: Camada Gold (O Valor para o Negócio)

- [ ] **Arquivo:** `03_gold.py`
- [ ] **Ler** as tabelas da camada Silver.
- [ ] **Criar e salvar** a tabela Delta `gold_customer_summary`.
- [ ] **Criar e salvar** a tabela Delta `gold_product_summary`.
- [ ] **Criar e salvar** a tabela Delta `gold_seller_summary`.

---

## Fase 5: Orquestração e Simulação de Consumo

- [ ] **Arquivo:** `pipeline_runner.py`
  - [ ] Utilizar `subprocess` (ou similar) para executar os scripts 01, 02 e 03 sequencialmente.
  - [ ] Capturar logs de tempo de execução por etapa.
  - [ ] Tratar falhas com `try/except` (simulando o Azure Data Factory).
- [ ] **Arquivo:** `04_share_simulation.py`
  - [ ] Ler a camada Gold.
  - [ ] Exportar os dados consolidados como `.csv` na pasta `output/`.
  - [ ] Gerar um Resumo Executivo via console (simulando a ponta final de um Delta Sharing).

---

## Fase 6: Documentação e Migração (README)

- [ ] **Arquivo:** `README.md`
- [ ] **Diagrama de arquitetura** do pipeline Medallion.
- [ ] **Justificativa das decisões de design** (ex: descarte de status específicos na camada Silver).
- [ ] **Instruções claras de execução local** (dependências, ambiente, comandos).
- [ ] **Análise crítica** sobre as diferenças estruturais entre a solução local e um ambiente produtivo real na nuvem (Databricks + Azure).
