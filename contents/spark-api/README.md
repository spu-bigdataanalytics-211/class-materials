

#### RDD

RDD (Resilient, Distributed, Dataset) is **immutable** distributed collection of objects. RDD is a logical reference of a dataset which is partitioned across many server machines in the cluster. RDDs are Immutable and are self recovered in case of failure. An RDD could come from any datasource, e.g. text files, a database via JDBC, etc.

RDDs have two sets of operations.

1. Transformations 
2. Actions


#### Shared Variables

Generally, while functions passed on, it executes on the specific remote cluster node. Usually, it works on separate copies of all the variables those we use in functions. These specific variables are *precisely copied to each machine*. Also, on the remote machine, no updates to the variables sent back to the driver program. Therefore, it would be inefficient to support general, read-write shared variables across tasks. Although, in spark for two common usage patterns, there are two types of shared variables, such as:

1. Broadcast Variables
2. Accumulators

<sub>Content taken from [techvidvan.com](https://techvidvan.com/tutorials/spark-shared-variable/).</sub>


##### Transformations and Actions

Transformation applies some function on a RDD and creates a new RDD, it does not modify the RDD that you apply the function on.(Remember that RDDs are immutable). Also, the new RDD keeps a pointer to it’s parent RDD.

Transformations are lazy operations on a RDD that create one or many new RDDs, e.g. map,filter, reduceByKey, join, cogroup, randomSplit

**Narrow transformation** — doesn’t require the data to be shuffled across the partitions. for example, Map, filter etc..
**Wide transformation** — requires the data to be shuffled for example, reduceByKey etc..

**An Action** is used to either save result to some location or to display it. You can also print the RDD lineage information by using the command filtered.toDebugString(filtered is the RDD here).

#### Spark DataFrame

In Spark, DataFrames are the distributed collections of data, **organized into rows and columns**. Each column in a DataFrame has a name and an associated type. DataFrames are similar to traditional database tables, which are structured and concise. We can say that DataFrames are relational databases with better optimization techniques.

Spark DataFrames can be created from various sources, such as Hive tables, log tables, external databases, or the existing RDDs. DataFrames allow the processing of huge amounts of data.

### Spark Python API

Create your Spark Environment using Google Colab with the script we had. After creating the environment, you can do the following to get your `sc` object.

After loading Spark, initating an instance of spark can be done as below.

``` py
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("My Awesome Spark App!") \
    .getOrCreate()
```

Read from a text file, create an RDD.

```py
sc.textFile('data.csv', use_unicode=True).take(4)
```

Creating a dataframe.

``` py
df = sqlContext.createDataFrame(
  data=[('a', 4), ('b', 2)], 
  schema=['Column A', 'Column B']
)
```

Apply a transformation to the data.

```py
df2 = df[df.column_name != 'some_value']
```

Apply an action to get a result.

```py
df3.filter(df3.size > 1000).count()
```
<sub>Content taken from [Spark Basics : RDDs,Stages,Tasks and DAG](https://medium.com/@goyalsaurabh66/spark-basics-rdds-stages-tasks-and-dag-8da0f52f0454).</sub>