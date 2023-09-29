from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from bug_repro_escape.config.ConfigStore import *
from bug_repro_escape.udfs.UDFs import *

def src_avro_CustsDatasetInput(spark: SparkSession) -> DataFrame:
    return spark.sql(
        'SELECT * FROM `qa_database`.`test_catalog_source` WHERE pipeline_name = CONCAT_WS(\"-\", \"raw-curated\", \\'{Config.raw_schema}\\')'
    )
