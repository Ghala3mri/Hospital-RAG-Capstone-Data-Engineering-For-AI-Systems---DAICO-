from pyspark.sql import SparkSession
from delta import DeltaTable
import json
from config import BRONZE_DELTA_PATH

spark = (
    SparkSession.builder
    .appName("BronzeLayer")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

def bronze_layer(record):
    df = spark.createDataFrame([record])

    df.write.format("delta").mode("append").save(BRONZE_DELTA_PATH)