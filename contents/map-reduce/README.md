# Introduction to MapReduce Algorithm

The challanges of working a dataset that is larger than your computer RAM brings some serious problems that you may not able to solve, unless you use parallel programming, or big data algorithms. 

[MapReduce](https://research.google/pubs/pub62/) is one of those algorithms to help you overcome problems.


### What is MapReduce

[MapReduce](https://en.wikipedia.org/wiki/MapReduce) is a processing technique and a program model for distributed computing.

The MapReduce algorithm contains two important tasks, namely Map and Reduce. Map takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key/value pairs). Secondly, reduce task, which takes the output from a map as an input and combines those data tuples into a smaller set of tuples. As the sequence of the name MapReduce implies, the reduce task is always performed after the map job.

The major advantage of MapReduce is that it is easy to scale data processing over multiple computing nodes. Under the MapReduce model, the data processing primitives are called *mappers* and *reducers*. 

Decomposing a data processing application into mappers and reducers is sometimes nontrivial. But, once we write an application in the MapReduce form, **scaling** the application to run **over hundreds, thousands, or even tens of thousands of machines** in a cluster is merely a configuration change.

MapReduce Algorithm uses the following three main steps:

1. Map Function
2. Shuffle Function
3. Reduce Function

### 1. Map

![map](assets/map.png)

Map function takes the task and divides it into subtasks. It may have two substeps under mapping:

1. Splitting 
2. Mapping

In splitting, the data is divided into sub-datasets.
In mapping, each of the sub-datasets are used in performing a required action or computation on each dataset.

The output of the mapping function should be a <key, value> pairs.

### 2. Shuffling

![shuffle](assets/shuffle.png)

Shuffling is the step where each <key, value> pairs are performed on ordering. It has two substeps:

1. Merging
2. Sorting

Merging combines all keys together and puts the same key's values into a list.
Sorting is the substep where the values are sorted per key.

The output of the shuffling is <key, sorted(value)> pairs. 

### 3. Reduce

![reduce](assets/reduce.png)

Reduce is the action of reducing the sorted values into a value using the required action or computation.

As a result, all <key, sorted(value)> pairs are returned back to <key, value> pairs with performed calculation.

<sup><sub>Images are from [an article at JournalDev](https://www.journaldev.com/8848/mapreduce-algorithm-example).</sup></sub>
<sup><sub>MapReduce introductory is from [Ravi Sharma's answer at Quora](https://www.quora.com/What-is-Map-Reduce/answer/Ravi-Sharma-3187/).</sup></sub>
