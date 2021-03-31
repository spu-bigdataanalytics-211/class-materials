
# How to Use/ Install Apache Spark

## Methods

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
