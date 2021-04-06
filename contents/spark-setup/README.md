
# How to Use/ Install Apache Spark

## Introduction

The following guide will help you to install spark-in memory.

1. Install JDK dependencies
2. Install Spark 
   1. From [Apache Spark website](https://spark.apache.org/downloads.html). This includes PySpark python package as well.
   2. Through PyPI with pip. This includes Apache Spark Java files.

## Methods

- [How to Use/ Install Apache Spark](#how-to-use-install-apache-spark)
  - [Introduction](#introduction)
  - [Methods](#methods)
    - [Google Colab](#google-colab)
    - [Using Databricks](#using-databricks)
    - [Saint Peter's Data Science Lab [NOT AVAILABLE]](#saint-peters-data-science-lab-not-available)
  - [Install Locally](#install-locally)
  - [References](#references)

### Google Colab

Install dependencies.

``` sh
# install java libs and spark.
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://downloads.apache.org/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz
!tar xf spark-3.1.1-bin-hadoop3.2.tgz
!pip install -q findspark
```

Add pyspark to path.

``` py
# set environment variables for java and spark
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.1.1-bin-hadoop3.2"
# add pyspark to sys.path
import findspark
findspark.init()
```

Initiate a spark object to connect to spark.

``` py
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
```

### Using Databricks

1. Create an account in Databricks.
2. Login to [Databricks Community Edition](https://community.cloud.databricks.com/)
3. [Create a cluster](https://docs.databricks.com/clusters/create.html).
4. Create notebook.

### Saint Peter's Data Science Lab [NOT AVAILABLE]

1. Be at the school network or connect with SPU VPN.
2. Go to [Notebooks](https://dsl.saintpeters.edu:8443/).
3. Instructor will create an account and give it to you.
4. Access lab through the guide in the website.

<!-- ### Using Docker and Docker Compose -->

## Install Locally

1. Download [JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
2. Download Spark from [Downloads Page](https://spark.apache.org/downloads.html).
3. Install JDK.
4. Install Apache.

## References

- [Spark Installation Guide](https://spark.apache.org/docs/latest/api/python/getting_started/install.html)
- [Creating a Spark Standalone Structure](https://medium.com/@marcovillarreal_40011/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-ba9d743a157f)

