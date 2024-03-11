from pyspark.sql.session import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName('pyspark_demo').getOrCreate()
spark.sql('create schema test_db')
###############################################
# Create Dataset/DataFrame via SparkSession

# 1. from python list of tuples
df = spark.createDataFrame(
    [
        (1, "andy", 20, "USA"),
        (2, "jeff", 23, "China"),
        (3, "james", 18, "USA")
    ]
).toDF("id", "name", "age", "country")
df.printSchema()
df.show()
df.repartition(1).write.saveAsTable('test_db.test_hive')
# 2. from python list of dicts
d = [{'name': 'Alice', 'age': 1}]
df = spark.createDataFrame(d)
df.repartition(1).write.saveAsTable('test_db.test_hive')
df.printSchema()
df.show()

# 3. from python list of Row objects
df = spark.createDataFrame(
    [
        Row(id=1, name="andy", age=20, country="USA"),
        Row(id=2, name="jeff", age=23, country="China"),
        Row(id=3, name="james", age=18, country="USA")
    ]
)
df.printSchema()
df.show()

# 4. with Schema definition
from pyspark.sql.types import *

l = [('Alice', 1)]
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)])

df = spark.createDataFrame(l, schema)
df.show()

# 5. from sql query
df = spark.sql("select 'Alice' as name, 1 as age")
df.show()

###############################################
# Create DataFrame via DataFrameReader
# json
df = spark.read.json("data/test_data.json")
df.show()

# csv
df = spark.read.csv("data/test_data.csv")
df.printSchema()
df.show()

df = spark.read.csv("data/test_data.csv", header=True, inferSchema=True)
df.printSchema()
df.show()


schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)])

df = spark.read.csv("data/test_data.csv", schema = schema)
df.show()



# from folder
df = spark.read.csv("data/csv", header=True, inferSchema=True)
df.printSchema()
df.show()

# text
df = spark.read.text("data/csv")
df.printSchema()
df.show()

# parquet/orc

# jdbc
df = spark.read.jdbc(url="jdbc:postgresql://localhost:5432/postgres",
                     table='spark_test_data',
                     properties={
                         "driver": "org.postgresql.Driver",
                         "user": "postgres",
                         "password": "postgres",
                     })
df.show()

query = """
(select * 
  from rmu.all_projects
 where "domain"  = 'Opportunity') as t
"""

df = spark.read.jdbc(url="jdbc:postgresql://localhost:5432/postgres",
                     table=query,
                     properties={
                         "driver": "org.postgresql.Driver",
                         "user": "postgres",
                         "password": "postgres",

                     })
df.show()



###############################################
# Use SQL directly
df = spark.createDataFrame(
    [
        Row(id=1, name="andy", age=20, country="USA"),
        Row(id=2, name="jeff", age=23, country="China"),
        Row(id=3, name="james", age=18, country="USA")
    ]
)
df.createOrReplaceTempView("test_data")
spark.sql("select * from test_data limit 2").show()

# Show Tables


###############################################
#Data Frame methods
df.show()
df.printSchema()
df.collect()
df.describe()
df.columns
df.count()
df.first()
df.explain()
df.schema.jsonValue()



###############################################
# Add New Column
import pyspark.sql.functions as f

df2 = df.withColumn("age2", df["age"] + 1)
df2.show()
df2 = df.withColumn("age2", df.age + 1)
df2.show()
df2 = df.withColumn("age2", f.col("age") + 1)
df2.show()

df2 = df.withColumn("name", f.upper(df["name"]))
df2.show()

###############################################
# Rename Column
df2 = df.withColumnRenamed("name", "new_name")
df2.show()

###############################################
# Remove Column
df2 = df.drop("name")
df2.show()

df2 = df.drop(df.name)
df2.show()

df2 = df.drop(f.col("age"))
df2.show()

df2 = df.drop("name", "age")
df2.show()

l = ["name", "age"]
df2 = df.drop(*l)
df2.show()

###############################################
# Select Subset of Columns
df1 = df.select("name", "age")
df1.show()

df1 = df.select("name", f.col("age"), df.country)
df1.show()

df1 = df.select("name", f.col("age"), f.col("age") + 50, df.country)
df1.show()

df1 = df.select("name", f.col("age"), (f.col("age") + 50).alias("new_age"), df.country)
df1.show()

df1 = df.selectExpr("age", "age + 50 as new_age")
df1.show()

###############################################
# Filter Rows
df2 = df.filter(df["age"] >= 20)
df2.show()
df2 = df.where(df1["age"] >= 20)
df2.show()

df2 = df.where("age >= 20")
df2.show()

df2 = df.filter((df["age"] >= 20) & (df["country"] == "China"))
df2.show()

df2 = df.filter((df["age"] >= 20) | (df["country"] == "China"))
df2.show()

spark.sql('create schema test_db')

###############################################
# Create UDF

# Create udf create python lambda
from pyspark.sql.functions import udf

custom_upper = udf(lambda e: e.upper())
df2 = df.select(custom_upper(df["name"]))
df2.show()

# UDF could also be used in filter, in this case the return type must be Boolean
# We can also use annotation to create udf
from pyspark.sql.types import *


@udf(returnType=BooleanType())
def udf2(e):
    if e >= 20:
        return True;
    else:
        return False


df3 = df.filter(udf2(df["age"]))
df3.show()

df3 = df.withColumn('flag', udf2(df["age"]))
df3.show()

# UDF could also accept more than 1 argument.
udf3 = udf(lambda e1, e2: e1 + "_" + e2)
df4 = df.select(udf3(df["name"], df["country"]).alias("name_country"))
df4.show()

# GroupBy
df2 = df.groupBy("country").count()
df2.show()

# Pass a Map if you want to do multiple aggregation
df3 = df.groupBy("country").agg({"age": "avg", "id": "count"})
df3.show()

df4 = df.groupBy("country")\
    .agg(f.avg(df["age"]).alias("avg_age"),
         f.count(df["id"]).alias("count"))
df4.show()

df5 = df.groupBy("country")\
    .agg(f.avg(df["age"]).alias("avg_age"),
         f.max(df["age"]).alias("max_age"))
df5.show()

###############################################
# Window functions
from pyspark.sql import Window
w = Window.partitionBy("country").orderBy(f.desc("id"))

df1 = df.withColumn("rn", f.row_number().over(w))
df1 = df1.withColumn("sum_age", f.sum("age").over(w))
df1.show()

###############################################
# Cast
df1 = df.withColumn("new_age", df.age.cast("string"))
df1.printSchema()

from pyspark.sql.types import StringType
df1 = df.withColumn("new_age", df.age.cast(StringType()))
df1.printSchema()

###############################################
# Nested data
from pyspark.sql import Row
from pyspark.sql.functions import explode

df = spark.createDataFrame([Row(a=1, intlist=[1, 2, 3], mapfield={"a": "b"})])
df.show()
df = df.select(explode(df.intlist).alias("anInt"))
df.show()

###############################################
# when otherwise
df.select(df.name, f.when(df.age > 20, 1).otherwise(0)).show()

###############################################
# Join on Single Field
df1 = spark.createDataFrame([(1, "andy", 20, 1), (2, "jeff", 23, 2), (3, "james", 18, 3)]).toDF("id", "name", "age", "c_id")
df1.show()

df2 = spark.createDataFrame([(1, "USA"), (2, "China")]).toDF("c_id", "c_name")
df2.show()

# You can just specify the key name if join on the same key
df3 = df1.join(df2, "c_id")
df3.show()

# Or you can specify the join condition expclitly in case the key is different between tables
df4 = df1.join(df2, df1["c_id"] == df2["c_id"])
df4.show()

# You can specify the join type afte the join condition, by default it is inner join
df5 = df1.join(df2, df1["c_id"] == df2["c_id"], "left_outer")
df5.show()

# sql not exists analog
df5 = df1.join(df2, on=['c_id'], how='left_anti')
df5.show()

# Join on Multiple Fields
df1 = spark.createDataFrame([("andy", 20, 1, 1), ("jeff", 23, 1, 2), ("james", 12, 2, 2)]).toDF("name", "age", "key_1", "key_2")
df1.show()

df2 = spark.createDataFrame([(1, 1, "USA"), (2, 2, "China")]).toDF("key_1", "key_2", "country")
df2.show()

# Join on 2 fields: key_1, key_2

# You can pass a list of field name if the join field names are the same in both tables
df3 = df1.join(df2, ["key_1", "key_2"])
df3.show()

# Or you can specify the join condition expclitly in case when the join fields name is differetnt in the two tables
df4 = df1.join(df2, (df1["key_1"] == df2["key_1"]) & (df1["key_2"] == df2["key_2"]))
df4.show()

###############################################
# set operators
df1 = spark.createDataFrame([(1, "andy", 20), (1, "andy", 20), (2, "jeff", 23), (2, "jeff", 23)]).toDF("id", "name", "age")
df1.show()

df2 = spark.createDataFrame([(2, "jeff", 23), (3, "james", 18)]).toDF("id", "name", "age")
df2.show()

df3 = df1.union(df2)
df3.show()

df3 = df1.unionAll(df2)
df3.show()

df3 = df1.intersect(df2)
df3.show()

df3 = df1.intersectAll(df2)
df3.show()

df3 = df1.exceptAll(df2)
df3.show()

###############################################
# Write DataFrame to files

df.write.parquet("data/parquet")

# repartition
df.write.repartition(1).parquet("data/parquet", mode="overwrite")

# partition by column
df.repartition(1).write.partitionBy("country").parquet("data/parquet", mode="overwrite")


# Write DataFrame to DB
df.write.format("jdbc") \
  .option("url", "jdbc:postgresql://localhost:5432/postgres") \
  .option("dbtable", "spark_test_data_wr") \
  .option("user", "postgres") \
  .option("password", "postgres") \
  .option("driver", "org.postgresql.Driver") \
  .save()


df = spark.read.jdbc(url="jdbc:postgresql://localhost:5432/postgres",
                     table='spark_test_data',
                     properties={
                         "driver": "org.postgresql.Driver",
                         "user": "postgres",
                         "password": "postgres",
                     })

