from os.path import abspath 
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
# Create spark session
warehouse_location = abspath('/tmp/warehouse/e2e_warehouse/')
spark = SparkSession.builder.appName('E2E') \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .config("spark.hadoop.orc.overwrite.output.file", "true") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

my_sql="select distinct date_key from dim_flat.drive_event_attr_flat where setl_load_date > timestamp '2021-10-29 22:09:34' and setl_load_date <= timestamp '2021-10-30 05:45:57'"

df = spark.sql(my_sql)

df.show()

