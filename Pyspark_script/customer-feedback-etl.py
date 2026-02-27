import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col, lower, length, regexp_replace

# Initialize contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init("customer-feedback-etl", {})

# Read from Glue Catalog (raw table)
raw_df = glueContext.create_dynamic_frame.from_catalog(
    database="customer_feedback_db",
    table_name="amazon_csv"  # change if needed
).toDF()

# Transformations
clean_df = raw_df \
    .withColumn(
        "clean_review",
        lower(regexp_replace(col("review_content"), "[^a-zA-Z0-9 ]", ""))
    ) \
    .withColumn("review_length", length(col("review_content"))) \
    .withColumn(
        "price_diff",
        col("actual_price") - col("discounted_price")
    )

# Convert back to DynamicFrame
clean_dyf = DynamicFrame.fromDF(clean_df, glueContext, "clean_dyf")

# Write to S3 (Processed Zone)
glueContext.write_dynamic_frame.from_options(
    frame=clean_dyf,
    connection_type="s3",
    connection_options={
        "path": "s3://company-feedback-customer/processed/",
        "partitionKeys": ["category"]
    },
    format="parquet"
)

job.commit()