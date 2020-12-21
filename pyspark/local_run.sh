#!/bin/bash
export PYSPARK_PYTHON=/usr/bin/python3

/opt/spark/bin/spark-submit \
    --jars /home/ubuntu/kaggle_riiid/jars/aws-java-sdk-bundle-1.11.908.jar,/home/ubuntu/kaggle_riiid/jars/hadoop-aws-3.2.0.jar \
    /home/ubuntu/kaggle_riiid/test_script.py