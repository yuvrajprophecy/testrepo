from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Customers(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("customer_id", StringType(), True), StructField("first_name", StringType(), True), StructField("last_name", StringType(), True), StructField("phone", StringType(), True), StructField("email", StringType(), True), StructField("country_code", StringType(), True), StructField("account_open_date", StringType(), True), StructField("account_flags", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .option("ignoreLeadingWhiteSpace", True)\
        .option("ignoreTrailingWhiteSpace", True)\
        .csv("dbfs:/Prophecy/8d2414fd5624f95be2d3b65f32dcc8c7/CustomersDatasetInput.csv")
