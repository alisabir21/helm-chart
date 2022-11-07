from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
spark = SparkSession.builder \
 .appName("Write_data") \
 .config("spark.hadoop.fs.s3a.endpoint","https://s3.ap-southeast-1.lyvecloud.seagate.com") \
 .config("spark.hadoop.fs.s3a.access.key","RLSMK3I4WOHRRQIH") \
 .config("spark.hadoop.fs.s3a.secret.key","UOU3Q1YR32JVQE32MSNCBSPB5NKBPPRG") \
 .config("spark.hadoop.fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem") \
 .config("spark.hadoop.fs.s3a.path.style.access", "true") \
 .config("spark.kubernetes.container.image","quay.io/avishay_sebban/seagate-spark-cnvrg:latest") \
 .getOrCreate()



print(spark.conf.get("spark.hadoop.fs.s3a.access.key"))
print(spark.conf.get("spark.hadoop.fs.s3a.secret.key"))
print(spark.conf.get("spark.hadoop.fs.s3a.endpoint"))


df_load = spark.read.csv('s3a://lc-stx-ap1-edp-media-dl-prod-raw/raw.db/sputter_slot_machine_svc20/batch_id=1656060651074/StationPressure220621022600_MAINT_MBI_VB61U_11May22.csv')
df_load.show(10)

df_load.write.csv('s3a://lc-stx-ap1-edp-media-dl-prod-raw/raw.db/sputter_slot_machine_svc20/batch_id=1656060651123/StationPressure220621022600_MAINT_MBI_VB61U_11May22.csv')