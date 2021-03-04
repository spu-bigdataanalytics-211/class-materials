# Class Materials

Hi!

This is the repository to find all everything about big data analytics. You will find tutorials we did in the class, class notes, python files, etc.

The content of this repository will be updated between **March 1st to May 22nd, 2021**, on a weekly basis.

### Contents

The content on this repository is organized based on the topic. 

| Directory                                        | Description                                                                 |
| ------------------------------------------------ | --------------------------------------------------------------------------- |
| [contents/python-warmup](contents/python-warmup) | Revisiting python, functions, classes, decorators, generators, etc.         |
| Upcoming...                                      | Introduction to parallelism                                                 |
<!-- |                                                  | Introduction to clustering systems, MongoDB, and Cassandra, Cloud Computing |
|                                                  | Map-Reduce Algorithm                                                        |
|                                                  | Spark and Hadoop Ecosystem. Understanding Spark architecture.               |
|                                                  | Spark API Introduction (RDDs, Accumulators, Broadcast variables, Dataframe) |
|                                                  | Midterm (Everything upto Spark), FP Start                                   |
|                                                  | Spark Examples 1 (RDD and Dataframe), FP Session 1                          |
|                                                  | Spark Examples 2 (Machine Learning), FP Session 2                           |
|                                                  | Spark Examples 3, FP Session 3                                              |
|                                                  | Final Project Presentations, What's Next                                    | -->

### How to use this Repository?

You should do the following while going over this repository.

1. Download this repository to your local machine using `git clone https://github.com/spu-bigdataanalytics-211/class-materials.git`.
2. Download python 3 from [python.org](https://www.python.org/), if you don't have python already on your computer.
3. [Create a virtual environment](#how-to-create-a-new-virtual-environment) and activate this environment everytime you need to use it.
4. Install [requirements.txt](requirements.txt) file using `pip install -r requirements.txt`.
5. That's it. 

Following are the recommendations.

6. Read the README file for each section.
7. For some sections, there will be `Examples.ipynb` and `Examples-Solutions.ipynb` files. These will have some examples, and their solutions on the related topic.
8. There will also be `Notes.ipynb`, which may have some more content about the topic.
9. Follow up with the assignments to practice more.

### How to create a new Virtual Environment?

Environment is a container for your application to run isolated with safely and without interrupting any other existing applications in the same machine.

Make sure you have python installed on your system.

```
python --version; pip --version
```

To create a virtual environment, you need a virtual environment manager. By default, python comes up with [venv](https://docs.python.org/3/library/venv.html) module. There are more modules like [virtualenv](https://virtualenv.pypa.io/en/latest/), etc.

In below command, using python, you are invoking `venv` module to create a new virtual environment folder with name `.venv`, in the current directory that you are in.

``` sh
python -m venv .venv
```

To activate the environment, you do the following.

``` ps
# on windows
 me@MacBook-Pro ~ .\.venv\Scripts\Activate

# on mac
 me@MacBook-Pro ~ source .venv/bin/activate

# your console will change to this
(.venv) me@MacBook-Pro ~ 
```

### Instructor's Note

All topics will be shared in here. Please review the content and course materials in here first. If you still have questions, please feel free to reach me by email or from GitHub at @metinsenturk.
