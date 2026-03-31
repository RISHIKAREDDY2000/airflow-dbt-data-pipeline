# Batch Data Engineering Pipeline

**Airflow + dbt + Snowflake**

## Overview

This project demonstrates a batch data engineering pipeline that ingests sales data, orchestrates workflows with **Apache Airflow**, performs transformations using **dbt**, and stores the results in **Snowflake** for analytics.

The goal is to simulate a modern batch data platform commonly used in data engineering environments.

## Architecture

API / Source Data
→ Apache Airflow (workflow orchestration)
→ dbt Transformations
→ Snowflake Data Warehouse
→ BI Dashboard / Analytics

## Tech Stack

* Apache Airflow
* dbt (data transformations)
* Snowflake
* Python
* SQL

## Repository Structure

```id="n2skqz"
airflow-dbt-data-pipeline
│
├── dags
│   └── data_pipeline_dag.py
├── ingestion
│   └── api_ingestion.py
├── dbt_project
│   └── models
│       └── sales_transformation.sql
├── warehouse
│   └── create_tables.sql
├── datasets
│   └── api_sales_sample.csv
├── architecture
│   └── pipeline_architecture.png
└── README.md
```

## Dataset

The project uses a sample **sales dataset** representing orders from an API source.

Columns include:

* order_id
* customer_id
* product
* price
* quantity
* date

Only a small sample dataset is included in the repository.

## Pipeline Workflow

### Step 1 – Data Ingestion

The ingestion script reads the dataset and stores it as raw data.

File:

```id="r31v9f"
ingestion/api_ingestion.py
```

### Step 2 – Workflow Orchestration

Apache Airflow schedules and orchestrates the pipeline using a DAG.

File:

```id="9vcytf"
dags/data_pipeline_dag.py
```

Pipeline tasks:

1. ingest API data
2. run dbt transformations

### Step 3 – Data Transformation

dbt performs SQL transformations to calculate total sales per customer.

File:

```id="o1j8m6"
dbt_project/models/sales_transformation.sql
```

Example transformation:

```id="skt9jz"
SELECT
customer_id,
SUM(price * quantity) AS total_sales
FROM raw_sales
GROUP BY customer_id
```

### Step 4 – Data Warehouse Storage

Processed data is stored in **Snowflake** tables for analytics.

Table definition:

```id="fy2td9"
warehouse/create_tables.sql
```

## Use Cases

This architecture is commonly used for:

* batch ETL data pipelines
* analytics data platforms
* warehouse data modeling
* automated data workflows
