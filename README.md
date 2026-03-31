# Batch Data Engineering Pipeline

Airflow + dbt + Snowflake

## Overview

This project demonstrates a batch data pipeline that ingests sales data, orchestrates workflows using Apache Airflow, performs SQL transformations with dbt, and stores results in Snowflake for analytics.

The pipeline simulates a modern data warehouse architecture commonly used for business intelligence and reporting.

## Architecture

API Data
→ Apache Airflow
→ dbt Transformations
→ Snowflake Data Warehouse
→ BI Dashboard

## Tech Stack

Apache Airflow
dbt
Snowflake
Python
SQL

## Pipeline Workflow

1. Sales data is ingested from an API source.
2. Airflow schedules and orchestrates the pipeline.
3. dbt transforms raw data into analytics-ready tables.
4. Data is stored in Snowflake for reporting.

## Use Cases

Batch ETL pipelines
Data warehouse transformations
Business intelligence data platforms
