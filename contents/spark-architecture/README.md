## Introduction

Apache Spark is a general purpose processing engine for analytics. It is generally used for large datasets, typically in terabytes or petabytes. It has wide coverage on APIs and can be used for processing batches of data, real-time streams, machine learning, and ad-hoc query. 

Processing tasks are distributed over a cluster of nodes, and data is cached in-memory, to reduce computation time. 

Spark is a processing engine for large scale datasets. It handles parallel processing operations so that you don't have to build your own.

Spark runs on both Windows and UNIX-like systems (e.g. Linux, Mac OS), and it should run on any platform that runs a supported version of Java. This should include JVMs on x86_64 and ARM64. It’s easy to run locally on one machine

Spark uses a master/slave architecture with a central coordinator called Driver and a set of executable workflows called Executors that are located at various nodes in the cluster.

1. Master Daemon (Driver Process)
2. Worker Daemon (Slave Process)

The components of the spark application are:
- Driver
- Application Master
- Spark Context
- Cluster Resource Manager(aka Cluster Manager)
- Executors

## Directed Acyclic Graph (DAG)

DAG is nothing but a graph which holds the track of operations applied on RDD.

DAGScheduler is the scheduling layer of Apache Spark that implements stage-oriented scheduling. It transforms a logical execution plan (i.e. RDD lineage of dependencies built using RDD transformations) to a physical execution plan (using stages).

## Spark Driver

The spark driver is the program that declares the transformations and actions on RDDs of data and submits such requests to the master.

In practical terms, the driver is the program that creates the SparkContext, connecting to a given Spark Master. In the case of a local cluster, like is your case, the `master_url=spark://<host>:<port>`.

Its location is independent of the master/slaves. You could co-located with the master or run it from another node. The only requirement is that it must be in a network addressable from the Spark Workers.

This is how the configuration of your driver looks like:


``` py
from pyspark.sql import SparkSession

# initialization of spark context
conf = SparkConf().setAppName(appName).setMaster(master) 
sc = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .config(conf=conf)\
        .getOrCreate()
```

To explain a bit more on the different roles:

- The driver prepares the context and declares the operations on the data using RDD transformations and actions.
- The driver submits the serialized RDD graph to the master. The master creates tasks out of it and submits them to the workers for execution. It coordinates the different job stages.
- The workers is where the tasks are actually executed. They should have the resources and network connectivity required to execute the operations requested on the RDDs.

<sub>Best answer for the question in [spark-driver-in-apache-spark](https://stackoverflow.com/a/24638280/5159551).</sub>

## Spark Master

Application Master is a framework-specific entity charged with negotiating resources with ResourceManager(s) and working with NodeManager(s) to perform and monitor application tasks. Each application running on the cluster has its own, dedicated Application Master instance.

Spark Master is created simultaneously with Driver on the same node (in case of cluster mode) when a user submits the Spark application using spark-submit.

The Driver informs the Application Master of the executor's needs for the application, and the Application Master negotiates the resources with the Resource Manager to host these executors.

In offline mode, the Spark Master acts as Cluster Manager.

## Cluster Managers

Spark applications run as independent sets of processes on a cluster, coordinated by the SparkContext object in your main program (called the driver program).

SparkContext can connect to several types of cluster managers:

- Spark’s own standalone cluster manager
- Mesos
- YARN

These cluster managers allocate resources across applications. Once connected, Spark **acquires executors** on nodes in the cluster, which are **processes** that **run computations and store data** for your application. 

Next, it sends your application code (defined by JAR or Python files passed to SparkContext) to the executors. Finally, SparkContext sends tasks to the executors to run.

![cluster overview](cluster-overview.png)

The system currently supports several cluster managers:

- Standalone – a simple cluster manager included with Spark that makes it easy to set up a cluster.
- Apache Mesos – a general cluster manager that can also run Hadoop MapReduce and service applications.
- Hadoop YARN – the resource manager in Hadoop 2.
- Kubernetes – an open-source system for automating deployment, scaling, and management of containerized applications.

## Executors

Executors are the processes at the worker's nodes, whose job is to complete the assigned tasks. These tasks are executed on the worker nodes and then return the result to the Spark Driver.

Executors are started once at the beginning of Spark Application and then work during all life of the application, this phenomenon is known as "Static Allocation of Executors". However, users can also choose to dynamically allocate executors where they can add or remove executors to Spark dynamically to match the overall workload (but this can affect other applications running on the cluster). Even if one Spark executor crashes, the Spark application can continue to work.

Other executor properties:

- stores data in a cache in a JVM heap or on disk
- reads data from external sources
- writes data to external sources
- performs all data processing

## Glossary


| Term            | Meaning                                                                                                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application     | User program built on Spark. Consists of a driver program and executors on the cluster.                                                                                                                                                                                |
| Application jar | A jar containing the user's Spark application. In some cases users will want to create an "uber jar" containing their application along with its dependencies. The user's jar should never include Hadoop or Spark libraries, however, these will be added at runtime. |
| Driver program  | The process running the main() function of the application and creating the SparkContext                                                                                                                                                                               |
| Cluster manager | An external service for acquiring resources on the cluster (e.g. standalone manager, Mesos, YARN)                                                                                                                                                                      |
| Deploy mode     | Distinguishes where the driver process runs. In "cluster" mode, the framework launches the driver inside of the cluster. In "client" mode, the submitter launches the driver outside of the cluster.                                                                   |
| Worker node     | Any node that can run application code in the cluster                                                                                                                                                                                                                  |
| Executor        | A process launched for an application on a worker node, that runs tasks and keeps data in memory or disk storage across them. Each application has its own executors.                                                                                                  |
| Task            | A unit of work that will be sent to one executor                                                                                                                                                                                                                       |
| Job             | A parallel computation consisting of multiple tasks that gets spawned in response to a Spark action (e.g. save, collect); you'll see this term used in the driver's logs.                                                                                              |
| Stage           | Each job gets divided into smaller sets of tasks called stages that depend on each other (similar to the map and reduce stages in MapReduce); you'll see this term used in the driver's logs.                                                                          |


## References

- https://spark.apache.org/docs/latest/cluster-overview.html
- https://books.japila.pl/apache-spark-internals/
- https://pawanmishra.github.io/spark-stand-alone-mode/
- https://intellipaat.com/blog/tutorial/spark-tutorial/spark-architecture/
- https://www.dezyre.com/article/apache-spark-architecture-explained-in-detail/338/
- https://www.analyticsvidhya.com/blog/2020/11/data-engineering-for-beginners-get-acquainted-with-the-spark-architecture/
- https://luminousmen.com/post/spark-anatomy-of-spark-application
