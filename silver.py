from pyspark.sql import SparkSession
from delta import DeltaTable
from config import BRONZE_DELTA_PATH, SILVER_DELTA_PATH

# Lineage
from lineage import emit_start_event, emit_complete_event, emit_fail_event

spark = (
    SparkSession.builder
    .appName("SilverLayer")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

def run_silver_delta():
    task = "silver_delta"
    emit_start_event(task)

    try:
        print("Running Silver Delta Layer...")

        
        df = spark.read.format("delta").load(BRONZE_DELTA_PATH)

      
        df_clean = (
            df.dropDuplicates(["Patient_ID"])
              .fillna({"Name": "Unknown", "Age": 0})
        )

        # MERGE 
        if DeltaTable.isDeltaTable(spark, SILVER_DELTA_PATH):
            delta_table = DeltaTable.forPath(spark, SILVER_DELTA_PATH)

            delta_table.alias("t").merge(
                df_clean.alias("s"),
                "t.Patient_ID = s.Patient_ID"
            ).whenMatchedUpdateAll() \
             .whenNotMatchedInsertAll() \
             .execute()

        else:
            df_clean.write.format("delta").mode("overwrite").save(SILVER_DELTA_PATH)

        print("Silver Delta Completed Successfully.")
        emit_complete_event(task)

    except Exception as e:
        print("Silver Delta Failed:", str(e))
        emit_fail_event(task)
        raise e