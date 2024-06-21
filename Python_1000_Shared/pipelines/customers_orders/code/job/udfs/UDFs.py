from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.lookups import (
    createLookup,
    createRangeLookup,
    lookup,
    lookup_last,
    lookup_match,
    lookup_count,
    lookup_row,
    lookup_row_reverse,
    lookup_nth
)

def registerUDFs(spark: SparkSession):
    spark.udf.register("factorial1", factorial1)
    spark.udf.register("random_string", random_string)
    spark.udf.register("squared", squared)
    spark.udf.register("udf_scipy_dependency", udf_scipy_dependency)
    spark.udf.register("udf_swap_product", udf_swap_product)
    spark.udf.register("udf_timestamptype", udf_timestamptype)
    spark.udf.register("udf_maptype", udf_maptype)
    spark.udf.register("udf_tokenize", udf_tokenize)
    spark.udf.register("squared_udf", squared_udf)
    spark.udf.register("factorial", factorial)
    spark.udf.register("udf_prime", udf_prime)
    spark.udf.register("udf_datetype", udf_datetype)
    spark.udf.register("udf_arraytype1", udf_arraytype1)
    spark.udf.register("udf_arraytype", udf_arraytype)
    spark.udf.register("udf1", udf1)
    

    try:
        from prophecy.utils import ScalaUtil
        ScalaUtil.initializeUDFs(spark)
    except :
        pass

def factorial1Generator():
    initial = 10

    @udf(returnType = IntegerType())
    def func(input):
        input = int(input) if input is not None else 2

        return int(input) * int(input) if input is not None else initial

    return func

factorial1 = factorial1Generator()

def random_stringGenerator():
    initial = 10

    @udf(returnType = StringType())
    def func(length, extra_characters=""):
        import string, random
        length = int(length) if length is not None else 2

        return "".join(
            [
              random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + extra_characters)
              for _ in range(length)
            ]
        )

    return func

random_string = random_stringGenerator()

def squaredGenerator():
    initial = 10

    @udf(returnType = IntegerType())
    def func(value=10):
        return (value * value)

    return func

squared = squaredGenerator()

def udf_scipy_dependencyGenerator():
    initial = 10

    @udf(returnType = StringType())
    def func():
        from scipy.special import cbrt
        cb = cbrt([27, 64])

        return str(cb[0])

    return func

udf_scipy_dependency = udf_scipy_dependencyGenerator()

def udf_swap_productGenerator():
    initial = 10

    @udf(returnType = IntegerType())
    def func(x, y):
        x = x ^ y
        y = x ^ y
        x = x ^ y

        return x * y

    return func

udf_swap_product = udf_swap_productGenerator()

def udf_timestamptypeGenerator():
    initial = 10

    @udf(returnType = TimestampType())
    def func(value):
        return to_timestamp(value)

    return func

udf_timestamptype = udf_timestamptypeGenerator()

def udf_maptypeGenerator():
    initial = 10

    @udf(
         returnType = ArrayType(StructType([
StructField("char", StringType(), False), StructField("count", IntegerType(), False)]))
    )
    def func():
        return [{"char" : "char1", "count" : 10}]

    return func

udf_maptype = udf_maptypeGenerator()

def udf_tokenizeGenerator():
    initial = 10

    @udf(returnType = ArrayType(StringType()))
    def func(text):
        # Tokenize the text
        tokens = text.split(" ")
        '''Remove stop words'''
        stop_words = {"the", "is", "are", "and", "to", "of", "in"}
        tokens = [token for token in tokens if token not in stop_words]
        """Perform stemming"""
        stemmer = SnowballStemmer("english")
        tokens = [stemmer.stem(token) for token in tokens]

        return tokens

    return func

udf_tokenize = udf_tokenizeGenerator()

def squared_udfGenerator():
    int_value = 15
    N = 10

    @udf(returnType = IntegerType())
    def func(value=10):
        return ((value * value) + int_value - float_value) if value else int_value

    return func

squared_udf = squared_udfGenerator()

def factorialGenerator():
    initial = 10

    @udf(returnType = IntegerType())
    def func(input):
        input = int(input) if input is not None else 2

        return int(input) * int(input) if input is not None else initial

    return func

factorial = factorialGenerator()

def udf_primeGenerator():
    initial = 10

    @udf(returnType = BooleanType())
    def func(x):
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    return func

udf_prime = udf_primeGenerator()

def udf_datetypeGenerator():
    initial = 10

    @udf(returnType = DateType())
    def func(value):
        return to_date(value)

    return func

udf_datetype = udf_datetypeGenerator()

def udf_arraytype1Generator():
    initial = 10

    @udf(returnType = ArrayType(IntegerType()))
    def func(value, repeattimes):
        return [value] * repeattimes

    return func

udf_arraytype1 = udf_arraytype1Generator()

def udf_arraytypeGenerator():
    initial = 10

    @udf(returnType = ArrayType(IntegerType()))
    def func(value, repeattimes):
        return [value] * repeattimes

    return func

udf_arraytype = udf_arraytypeGenerator()

def udf1Generator():
    initial = 10

    @udf(returnType = StringType())
    def func(input1):
        return input1 + str(initial)

    return func

udf1 = udf1Generator()
