# Databricks notebook source
dfNetflixFile = spark.read.option("header",True).csv('/mnt/datalake/netflix_titles_2021.csv')
display(dfNetflixFile)

# COMMAND ----------

dfNetflixFile.write.partitionBy('type').mode("overwrite").format('delta').save('/mnt/datalake/NetflixTransactions')

# COMMAND ----------

dfOutput = spark.read.format('delta').load('/mnt/datalake/NetflixTransactions')
display(dfOutput)

# COMMAND ----------

dfOutput.write.format("delta").mode("overwrite").save("/mnt/datalake/NetflixTransactions")

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL LOCATION NetflixTransactions
# MAGIC URL 'abfs://datalake@innovantrastrgadls2.blob.core.windows.net/mnt/datalake/NetflixTransactions';
# MAGIC
# MAGIC CREATE TABLE NetflixTitlesMarch2025
# MAGIC USING DELTA
# MAGIC LOCATION 'abfss://datalake@innovantrastrgadls2.blob.core.windows.net/mnt/datalake/NetflixTransactions';
