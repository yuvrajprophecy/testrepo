from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *

@execute_rule
def br_src_parquet_all_type_and_partition_withspacehyphens(
        c__short: Column=lambda: col("`c- short`"), 
        c____int: Column=lambda: col("`c  - int`"), 
        c_float_____: Column=lambda: col("`c_float-__  `"), 
        c_string: Column=lambda: col("`c-string`"), 
        c_date_for_today: Column=lambda: col("`c_date-for today`"), 
        c_timestamp_____for__today: Column=lambda: col("`c_timestamp  __ for--today`"), 
        c_array_string____string: Column=lambda: col("`c_array-string  _ string`"), 
        c_struct_______: Column=lambda: col("`c_struct -- _  `"), 
        c____boolean____: Column=lambda: col("`c -  boolean _  `"), 
        c_decimal_____: Column=lambda: col("`c_decimal  -  `")
):
    return when(
          (
            (
              (
                (c__short == lit(10))
                & c____int.isNotNull()
              )
              & (
                (c_float_____ < lit(0))
                & (
                  c_string.like("%4%")
                  | (
                    (
                      ((lit("50").cast(IntegerType()) > lit(5)) & lit("testADrone").like("%A%"))
                      | (lit(1).bitwiseAND(lit(1)) == lit(1))
                    )
                    | (
                      (
                        (
                          (
                            expr("named_struct('a', 1, 'b', 2)")\
                              .isin(expr("named_struct('a', 1, 'b', 1)"), expr("named_struct('Abhishek', 1, 'Bharat', 3)"))
                            & (length(lit("Spark SQL ")) > lit(20))
                          )
                          & (
                            (levenshtein(lit("kitten"), lit("sitting")) > lit(10))
                            & (locate("bar", lit("abcbarbar")) > lit(2))
                          )
                        )
                        & (
                          (
                            (
                              concat(concat(lit("->"), expr("split_part('Hello,world,!', ',', 1)")), lit("<-"))
                              != lit(None)
                            )
                            & lit("SparkSQL").startswith(lit("Spark"))
                          )
                          & (
                            lit(None).startswith(lit("Spark"))
                            & (upper(lit("SparkSql")) != lit(None))
                          )
                        )
                      )
                      & (
                        (
                          (
                            (bround(lit(13.5), - 1) == lit(1))
                            & array_contains(array(lit(1), lit(2), lit(3)), lit(2))
                          )
                          & (
                            map_concat(create_map(lit(1), lit("a"), lit(2), lit("b")), create_map(lit(3), lit("c")))\
                              .isNotNull()
                            & map_entries(create_map(lit(1), lit("a"), lit(2), lit("b")))\
                              .isNotNull()
                          )
                        )
                        & (
                          (
                            (add_months(lit("2016-08-31"), - 6) != lit(None))
                            & (current_date() != lit(None))
                          )
                          & (
                            (expr("date('2021-03-21')") != lit(None))
                            & (date_add(lit("2016-07-30"), 1) != lit(None))
                          )
                        )
                      )
                    )
                  )
                )
              )
            )
            & (
              (
                (c_date_for_today == lit("is null").cast(DateType()))
                & (c_timestamp_____for__today == to_timestamp(lit("2001-10-13 10:20:44")))
              )
              & (
                ~ c____boolean____.eqNullSafe(lit(True))
                & (c_decimal_____ == lit(12321))
              )
            )
          ),
          lit(1)
        )\
        .when(
          (
            (
              c_float_____.isNotNull()
              & (c_date_for_today != lit("is null").cast(DateType()))
            )
            & (c_decimal_____ > lit(12321))
          ),
          lit(2)
        )\
        .when(
          (
            (
              (
                (c__short > lit(10))
                & ~ c_string.like("%4%")
              )
              & (c_timestamp_____for__today != to_timestamp(lit("2001-10-13 10:20:44")))
            )
            & (
              ~ c____boolean____.eqNullSafe(lit(False))
              & (c_decimal_____ <= lit(12321))
            )
          ),
          lit(3)
        )\
        .when(((c__short < lit(20)) & c_string.like("%7%")), lit(4))\
        .when(
          (
            (
              (c____int > lit(22))
              & c_string.like("%6%")
            )
            & (
              c_date_for_today.isNotNull()
              & c____boolean____.isNotNull()
            )
          ),
          lit(5)
        )\
        .when(
          (
            (
              c____int.isin(lit(6540), lit(6541))
              & c_string.isin(
                lit(
                  "r#$%@#4!*&^()_=ASD~!405"
                )
              )
            )
            & (
              c_timestamp_____for__today.isNotNull()
              & c____boolean____.isin(lit(True), lit(False))
            )
          ),
          lit(6)
        )\
        .when(((c_float_____ > lit(0)) & c_array_string____string.isNotNull()), lit(7))\
        .when(c_struct_______.isNotNull(), lit(8))\
        .when(c__short.isNotNull(), lit(9))\
        .when(
          (
            (
              (
                c__short.isNull()
                & c____int.isNull()
              )
              & (
                c_float_____.isNull()
                & c_string.isNull()
              )
            )
            & (
              (
                c_date_for_today.isNull()
                & c_timestamp_____for__today.isNull()
              )
              & (
                c_array_string____string.isNull()
                & c_struct_______.isNull()
              )
            )
          ),
          lit(10)
        )\
        .otherwise(lit(22))\
        .alias("br_src_parquet_all_type_rule")

@execute_rule
def br_src_parquet_all_type_and_partition_withspacehyphens_basic(
        c_double: Column=lambda: col("c_double"), 
        c_string: Column=lambda: col("`c-string`")
):
    return when(((c_double > lit(45730)) & c_string.like("%6%")), lit("Valid"))\
        .when(((c_double > lit(34)) & c_string.like("%9%")), lit("Invalid"))\
        .otherwise(lit("Other"))\
        .alias("br_basic_parquet")
