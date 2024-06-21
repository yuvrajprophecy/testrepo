from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Report(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .option("ignoreLeadingWhiteSpace", True)\
        .option("ignoreTrailingWhiteSpace", True)\
        .mode("overwrite")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/Prophecy/8d2414fd5624f95be2d3b65f32dcc8c7/report-top-customers.csv")
