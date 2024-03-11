from pyspark.sql.session import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName('pyspark_demo').getOrCreate()
spark.sql("select 1").show()

###############################################
# Create Dataset/DataFrame via SparkSession

# 1. from python list of tuples
# df = spark.createDataFrame([Row(id=1, name="andy", age=20, country="USA"), Row(id=2, name="jeff", age=23, country= "China"), Row(id=3, name="james", age=18, country="USA")])