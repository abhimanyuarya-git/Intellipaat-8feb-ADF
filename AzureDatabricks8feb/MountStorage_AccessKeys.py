# Databricks notebook source
# Use Databricks secrets instead of hardcoded keys
# accessKey = dbutils.secrets.get(scope="<scope-name>", key="<key-name>")
sourceContainer = 'datalake'
storageAccountName = 'innovantrastrgadls2'
sourceMountPoint = '/mnt/datalake'

# COMMAND ----------

# Option 1: Mount using Azure AD (recommended)
# dbutils.fs.mount(
#     source = f'wasbs://{sourceContainer}@{storageAccountName}.blob.core.windows.net',
#     mount_point= sourceMountPoint
# )

# Option 2: Mount using access key from Databricks secrets
# accessKey = dbutils.secrets.get(scope="azure-storage", key="storage-access-key")
# dbutils.fs.mount(
#     source = f'wasbs://{sourceContainer}@{storageAccountName}.blob.core.windows.net',
#     mount_point= sourceMountPoint,
#     extra_configs={f'fs.azure.account.key.{storageAccountName}.blob.core.windows.net': accessKey}
# )

# COMMAND ----------

dbutils.fs.ls("/mnt/datalake")

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

dbutils.fs.mounts()
