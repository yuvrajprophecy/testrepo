from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_1.config.ConfigStore import *
from pipeline_1.udfs.UDFs import *

def reformat_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(concat(col("first_name"), lit(" "), col("last_name")).alias("full_name"))
