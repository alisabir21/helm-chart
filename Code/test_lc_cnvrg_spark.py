from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
spark = SparkSession.builder \
.appName("Write_data") \
.config("spark.hadoop.fs.s3a.path.style.access", "true") \
.config("spark.kubernetes.container.image","quay.io/avishay_sebban/seagate-spark-cnvrg:latest") \
.getOrCreate()





#print(spark.conf.get("spark.hadoop.fs.s3a.access.key"))
#print(spark.conf.get("spark.hadoop.fs.s3a.secret.key"))
#print(spark.conf.get("spark.hadoop.fs.s3a.endpoint"))



df_load = spark.read.orc('s3a://stx-lcva03-ehc-prd-data-v1/t1/slider.db_abl3_bar_fact/20211219150000-20211220150000/part-00000-e447b060-a9ba-432e-9442-c3adabd21c3f-c000.zlib.orc')
df_load.show(10)



df_load.write.orc('s3a://stx-lcva03-ehc-prd-data-v1/spark_test/20211219150000-20211220150000/test/')