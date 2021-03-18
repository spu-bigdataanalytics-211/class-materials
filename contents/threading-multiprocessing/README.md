# Parallel Programming with Python

## Introduction

In order to do the parallel programming in the right way, we need to understand the type of problem we are dealing with first, to be able to find the right way to parallelize the task. Therefore, our first starting point is to understand the two different types of operations.

### IO Bound

[IO bound](https://en.wikipedia.org/wiki/I/O_bound) is when the ability to complete a task/ process is limited by the Input/ Output subsystem of the computer. This type may include the file system, networking, etc. IO bound therefore means, computer takes more time to request the data than to process it.

- Downloading a file from internet.
- Accessing a file/ folder from the computer.
- Accessing a resource in the network.
- Retreiving records from a database.

IO bound considered to be an inherent problem since the begining of the time with computers :smirk:, but no worries, we are here to understand it to live with it.

### CPU Bound

[CPU bound](https://en.wikipedia.org/wiki/CPU-bound) is a process or a task that is limited by the speed of the CPU in a computer.

For example, below is a list of examples for CPU bound.

- Training a machine learning model.
- Multiplying numbers, matrices.
- Preprocessing a dataset, such as transforming columns.
- Doing EDA on a dataset.

### Concurrency vs Parallelism

Concurrency is running two tasks together. When a computer is able to run two tasks at the same time, or it looks as if it started together, we think tasks are running concurrent. While achieving concurrency, a computer may take advantage of [CPU time sharing](https://en.wikipedia.org/wiki/Time-sharing) feature of the operating system, where tasks wait each other and when one runs on the CPU and other on the queue.

Parallelism is can be done on a task or a group of task together. It takes advantage of physical CPU cores of the infrastructure that the computer has, and assigns part of the task or seperate tasks to different CPUs.

In [oracle docs](), concurrency is `a condition that exists when at least two threads are making progress. A more generalized form of parallelism that can include time-slicing as a form of virtual parallelism`. And, paralellism is 	
`a condition that arises when at least two threads are executing simultaneously`.

Concurrency                 | Parallelism
:-------------------------: | :-------------------------:
![concurrency](assets/concurrency.gif) |  ![parallel](assets/parallelism.gif)

For more information on concurrency vs parallelism with python, check out this article on [Hackernoon](https://hackernoon.com/concurrent-programming-in-python-is-not-what-you-think-it-is-b6439c3f3e6a) written by [@melvinkcx](https://github.com/melvinkcx).

### Threading and Multiprocessing

To understand the difference of threading and multiprocessing, lets first have a look at what a thread and a process means.

A thread is the execution of instructions in a given program. It is a subset of a process. It is considered as "lightweight process", since it shares the resources alloted for a process.

A process is a program in execution by the computer. It holds a memory space, a disk space that is unique to the process itself. In a multiprocessing environment, multiple processes of the same task is executed in parallel. For example, creating multiple instance of an application, say, Calculator. Each instance of a calculator is a process.

The **main difference** between the two is that threads share the same memory space, and processes not.

Multithreading takes advantage of having multiple threads in a program. The advantage is the task in hand will be completed much faster if it is IO bound, where the CPU will process more parts of the instructions while all other threads are waiting for a network related delay.

In multiprocessing, IO bound tasks won't be enough since the CPU has to wait for the data to be retreived from the network. However, it the data is already awailable, such as in CPU bound tasks, multiprocessing will be much much faster the total CPU power assigned to the task is much more.

### Packages in Python for Parallel Programming

There are many options to do parallel programming using python. You are more than welcome to choose any of those libraries including the standard packages. My advise is to test diffrent ones, so that you will cover more.

Some of these packages are, but not limited to:

- [Ray](https://github.com/ray-project/ray)
- [Numba](http://numba.pydata.org/)
- [Modin](https://github.com/modin-project/modin)
- [Dask](https://dask.org/)
- [multiprocessing](https://docs.python.org/3.8/library/multiprocessing.html)
- [threading](https://docs.python.org/3.8/library/threading.html)
- [concurrent.futures](https://docs.python.org/3.8/library/concurrent.futures.html)
