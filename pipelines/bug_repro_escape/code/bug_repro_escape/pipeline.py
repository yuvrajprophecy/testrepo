from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from bug_repro_escape.config.ConfigStore import *
from bug_repro_escape.udfs.UDFs import *
from prophecy.utils import *
from bug_repro_escape.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_avro_CustsDatasetInput = src_avro_CustsDatasetInput(spark)
    df_DONOT_DELETE = DONOT_DELETE(spark, df_src_avro_CustsDatasetInput)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/bug_repro_escape")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/bug_repro_escape", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/bug_repro_escape")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
