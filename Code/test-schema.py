from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.functions as sf

spark = SparkSession.builder.appName("spark-test") \
  .config("spark.hadoop.javax.jdo.option.ConnectionURL","jdbc:mysql://10.213.199.18:3306/hive?useSSL=false") \
  .config("spark.hadoop.javax.jdo.option.ConnectionDriverName","com.mysql.jdbc.Driver") \
  .config("spark.hadoop.javax.jdo.option.ConnectionUserName", "lyvemysql") \
  .config("spark.hadoop.javax.jdo.option.ConnectionPassword", "lyvemysql@sv15") \
  .config("fs.s3a.secret.key","0S5YJVUG3BD2YYEVBWUW4NSUVL2W1WYS") \
  .config("fs.s3a.access.key","ONUCU4LYNLMEM5HG") \
  .config("fs.s3a.endpoint", "https://s3.us-west-1.svl.lyvecloud.seagate.com") \
  .enableHiveSupport() \
  .getOrCreate() 



spark.sql("CREATE SCHEMA tmp2")
#spark.sql("""Alter table tmp2.p282_sensitivity_margin2_fact_test ADD partition(event_date_key='20211106',atlas_insert_ver='2111070311'),partition(event_date_key='20211107',atlas_insert_ver='2111070311'),partition(event_date_key='20211108',atlas_insert_ver='2111080310'),partition(event_date_key='20211106',atlas_insert_ver='2111080310'),partition(event_date_key='20211107',atlas_insert_ver='2111080310')""")

#spark.sql("""ALTER TABLE tmp2.p282_sensitivity_margin2_fact_test ADD IF not EXISTS PARTITION  (event_date_key=20211106, atlas_insert_ver=2111060311) location 's3a://stx-lcva03-ehc-prd-data-v1/spark__poc/drive.db_p282_sensitivity_margin2_fact/event_date_key=20211106/atlas_insert_ver=2111060311'""")

#spark.sql("""ALTER TABLE tmp2.p282_sensitivity_margin2_fact_test ADD IF not EXISTS PARTITION  (event_date_key=20211106, atlas_insert_ver=2111070311) location 's3a://stx-lcva03-ehc-prd-data-v1/spark__poc/drive.db_p282_sensitivity_margin2_fact/event_date_key=20211106/atlas_insert_ver=2111070311'""")

#spark.sql("""ALTER TABLE tmp2.p282_sensitivity_margin2_fact_test ADD IF not EXISTS PARTITION  (event_date_key=20211107, atlas_insert_ver=2111070311) location 's3a://stx-lcva03-ehc-prd-data-v1/spark__poc/drive.db_p282_sensitivity_margin2_fact/event_date_key=20211107/atlas_insert_ver=2111070311'""")

#spark.sql("""ALTER TABLE tmp2.p282_sensitivity_margin2_fact_test ADD IF not EXISTS PARTITION  (event_date_key=20211108, atlas_insert_ver=2111080310) location 's3a://stx-lcva03-ehc-prd-data-v1/spark__poc/drive.db_p282_sensitivity_margin2_fact/event_date_key=20211108/atlas_insert_ver=2111080310'""")


#spark.sql("""ALTER TABLE tmp2.p282_sensitivity_margin2_fact_test ADD IF not EXISTS PARTITION  (event_date_key=20211106, atlas_insert_ver=2111080310) location 's3a://stx-lcva03-ehc-prd-data-v1/spark__poc/drive.db_p282_sensitivity_margin2_fact/event_date_key=20211106/atlas_insert_ver=2111080310'""")


#spark.sql("""ALTER TABLE tmp2.p282_sensitivity_margin2_fact_test ADD IF not EXISTS PARTITION  (event_date_key=20211107, atlas_insert_ver=2111080310) location 's3a://stx-lcva03-ehc-prd-data-v1/spark__poc/drive.db_p282_sensitivity_margin2_fact/event_date_key=20211107/atlas_insert_ver=2111080310'""")


#spark.sql("show partitions tmp2.p282_sensitivity_margin2_fact_test").show(truncate=False)
#spark.sql("show create table tmp2.p282_sensitivity_margin2_fact_test").show(truncate=False)


print("done")

#spark.sql("select * from tmp2.p282_sensitivity_margin2_fact_test limit 10").show(truncate=False)