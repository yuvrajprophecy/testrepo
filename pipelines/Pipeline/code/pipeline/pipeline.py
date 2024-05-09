from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline.config.ConfigStore import *
from pipeline.udfs.UDFs import *
from prophecy.utils import *
from pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    print_hello(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Pipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Pipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()
