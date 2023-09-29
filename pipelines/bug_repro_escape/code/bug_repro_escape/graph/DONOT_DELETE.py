from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bug_repro_escape.config.ConfigStore import *
from bug_repro_escape.udfs.UDFs import *

def DONOT_DELETE(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print(f"String: {Config.raw_schema}")
    out0 = in0

    return out0
