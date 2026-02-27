## Customer Feedback Analytics Pipeline (AWS)
# Project Overview
This project demonstrates the design and implementation of a serverless end-to-end data engineering pipeline on AWS to process and analyze Amazon product ratings and reviews data.
The solution ingests raw structured data into an Amazon S3 data lake, performs ETL transformations using AWS Glue (PySpark), and enables optimized SQL analytics through Amazon Athena.
The architecture follows modern Data Lake best practices including schema discovery, metadata cataloging, partitioning, and columnar storage optimization.

# Business Scenario
A company collects daily customer feedback data in CSV/JSON format.
The objective is to:
- ✔ Store raw feedback data reliably
- ✔ Clean and transform review data
- ✔ Optimize storage for analytics
- ✔ Enable business insights through SQL queries

# Flow:
CSV/JSON Feedback → S3 (Raw Layer) → Glue ETL (Clean Data) → S3 (Processed Layer) → Athena (SQL Queries)

 # AWS Services Used
- Amazon S3 – Data Lake storage (Raw & Processed zones)
- AWS Glue Crawler – Automatic schema inference
- AWS Glue ETL (PySpark) – Data transformation
- AWS Glue Data Catalog – Centralized metadata management
- Amazon Athena – Serverless SQL analytics
- AWS IAM – Secure role-based access

  # Project Structure
  customer-feedback-analytics/
│
├── raw/                # Raw dataset (CSV/JSON files)
├── processed/          # ETL output (Partitioned Parquet files)
├── queries/            # Athena SQL queries
├── Pyspark_script/     # AWS Glue ETL script
└── Screenshots/        # Execution & result screenshots

# Dataset Description
The dataset contains 1,000+ Amazon product records including:
- Product information
- Pricing & discount details
- Ratings & vote counts
- User review titles and content
- The dataset includes both structured and semi-structured data.

# Future Improvements
Sentiment analysis using AWS Comprehend
Dashboard integration (QuickSight / Power BI)
Incremental data processing
Event-driven ingestion using Lambda
Glue Workflow orchestration
