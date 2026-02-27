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
- 🛠 AWS Services Used

- Amazon S3 – Data Lake storage (Raw & Processed zones)
- AWS Glue Crawler – Automatic schema inference
- AWS Glue ETL (PySpark) – Data transformation
- AWS Glue Data Catalog – Centralized metadata management
- Amazon Athena – Serverless SQL analytics
- AWS IAM – Secure role-based access
