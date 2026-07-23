from pyspark.sql import SparkSession
from delta import DeltaTable
from config import SILVER_DELTA_PATH, GOLD_DELTA_PATH

# Lineage
from lineage import emit_start_event, emit_complete_event, emit_fail_event

spark = (
    SparkSession.builder
    .appName("GoldLayer")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

def run_gold_delta():
    task = "gold_delta"
    emit_start_event(task)

    try:
        print("Running Gold Delta Layer...")

        df = spark.read.format("delta").load(SILVER_DELTA_PATH)

        # KPI: متوسط الفواتير لكل مستشفى
        gold_df = (
            df.groupBy("Hospital")
              .avg("Billing Amount")
              .withColumnRenamed("avg(Billing Amount)", "Average_Billing")
        )

        # MERGE 
        if DeltaTable.isDeltaTable(spark, GOLD_DELTA_PATH):
            delta_table = DeltaTable.forPath(spark, GOLD_DELTA_PATH)

            delta_table.alias("t").merge(
                gold_df.alias("s"),
                "t.Hospital = s.Hospital"
            ).whenMatchedUpdateAll() \
             .whenNotMatchedInsertAll() \
             .execute()

        else:
            gold_df.write.format("delta").mode("overwrite").save(GOLD_DELTA_PATH)

        print("Gold Delta Completed Successfully.")
        emit_complete_event(task)

    except Exception as e:
        print("Gold Delta Failed:", str(e))
        emit_fail_event(task)
        raise e