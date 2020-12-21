import boto3
s3_session = boto3.Session()
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
bucket_name = 'npa02012-main'
s3_bucket = s3_resource.Bucket(bucket_name)


import pyspark

spark_context = pyspark.SparkContext()
spark_session = pyspark.sql.SparkSession \
    .builder \
    .appName("Spark ML example on titanic data ") \
    .getOrCreate()

aws_creds = s3_session.get_credentials().get_frozen_credentials()
hadoop_conf = spark_context._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("fs.s3a.awsAccessKeyId", aws_creds.access_key)
hadoop_conf.set("fs.s3a.awsSecretAccessKey", aws_creds.access_key)

train_path = "s3a://npa02012-main/kaggle_data/titanic/train.csv"

titanic_df = spark_session.read.option('header', 'true').csv(train_path)

print(titanic_df.count())