# Path to Python

Diving into Python.

* 1: Language Basics
* 2: Multiparadigmatic programming (imperative, OO, functional)
* 3: Working with data (files, web, JSON)
* 4: Tabular data with Pandas (pandas, csv, plotting)

## Schedule

### Day 1

* [ ] How Python views the world
    * [x] [ExecutionModes.md](ExecutionModes.md)
    * [x] [notebooks/python_world_view.ipynb](notebooks/python_world_view.ipynb)
* [ ] Language features
    * [x] [notebooks/intro/01.ipynb](notebooks/intro/01.ipynb)
    * [x] [notebooks/intro/02.ipynb](notebooks/intro/02.ipynb)
    * [x] [notebooks/intro/03.ipynb](notebooks/intro/03.ipynb)
    * [x] [notebooks/intro/04.ipynb](notebooks/intro/04.ipynb)

### Day 2

* [ ] Language Features
    * [ ] [notebooks/intro/05.ipynb](notebooks/intro/05.ipynb)
    * [ ] [notebooks/intro/06.ipynb](notebooks/intro/06.ipynb)
    * [ ] [notebooks/intro/07.ipynb](notebooks/intro/07.ipynb)
* [ ] Python I/O and serializations
    * [ ] [notebooks/IO.ipynb](notebooks/IO.ipynb)
* [ ] Additional Python Topics
    * [ ] [notebooks/Exceptions.ipynb](notebooks/Exceptions.ipynb)
    * [ ] [notebooks/Collections.ipynb](notebooks/Collections.ipynb)
    * [ ] [notebooks/Generators.ipynb](notebooks/Generators.ipynb)
    * [ ] [notebooks/Decorators.ipynb](notebooks/Decorators.ipynb)
    * [ ] [notebooks/FunctionalAspects.ipynb](notebooks/FunctionalAspects.ipynb)
    * [ ] [notebooks/TypeHintsOverview.ipynb](notebooks/TypeHintsOverview.ipynb)
* [ ] Python data munging
    * [ ] [notebooks/HelloNumpy.ipynb](notebooks/HelloNumpy.ipynb)
    * [ ] [notebooks/HelloPandas.ipynb](notebooks/HelloPandas.ipynb)
    * [ ] [notebooks/Pandas/01 Pandas Basic Access.ipynb](notebooks/Pandas/01 Pandas Basic Access.ipynb)
    * [ ] [notebooks/Pandas/02 Pandas Reading Excel.ipynb](notebooks/Pandas/02 Pandas Reading Excel.ipynb)
    * [ ] [notebooks/Pandas/03 Pandas Aggregations.ipynb](notebooks/Pandas/03 Pandas Aggregations.ipynb)
    * [ ] [notebooks/Pandas/04 Pandas Basic Plotting.ipynb](notebooks/Pandas/04 Pandas Basic Plotting.ipynb)

Extra:

* [notebooks/DataModelOverview.ipynb](notebooks/DataModelOverview.ipynb), ...


Examples:

* [notebooks/Pandas/13 Pandas Example - Geolocations.ipynb](notebooks/Pandas/13 Pandas Example - Geolocations.ipynb) (MUKA)
* [notebooks/Pandas/14 Pandas Example - Learning about Weather with DWD.ipynb](notebooks/Pandas/14 Pandas Example - Learning about Weather with DWD.ipynb)
* [notebooks/Pandas/15 Pandas Example - Used Cars.ipynb](notebooks/Pandas/15 Pandas Example - Used Cars.ipynb)

Example (just rendered, data is now 404):

* [https://github.com/miku/sundaypython/blob/master/notebooks/04%20Working%20with%20CSV.ipynb](https://github.com/miku/sundaypython/blob/master/notebooks/04%20Working%20with%20CSV.ipynb)

<!--
    * [ ] Data munging
    * [ ] [notebooks/HelloPandas.ipynb](notebooks/HelloPandas.ipynb)
* [ ] Example AI project with LlamaIndex
    * [ ] [Projects/rag](Projects/rag)
-->
----

## Mode of operation

We will look at different contexts:

* [ ] many data structures and approaches can be tried out in a **REPL**
* [ ] research, experiments in **notebooks**
* [ ] automating tasks with **scripts**

## Python Background

* 1991-02-21 (more than 33 years ago, about 19 years after C)
* open source, dynamically typed, interpreted language with a major implementation ("[cpython](https://github.com/python/cpython/)")
* large code fissure between 2006 ([PEP-3000](https://peps.python.org/pep-3000/)) and 2020 ("[Sunsetting Python 2](https://www.python.org/doc/sunset-python-2/)")
* de-facto language for the convenience layer in scienfitic computing, [on the rise](https://www.tiobe.com/tiobe-index/python/) (tiobe), [Heise: Und der Sieger ist - Python](https://www.heise.de/news/TIOBE-Index-Und-der-Sieger-ist-Python-7216002.html) (2022), blueprint for new developments (like [Mojo](https://en.wikipedia.org/wiki/Mojo_(programming_language)))
* many popular libraries ([top 20](https://pypistats.org/top) packages are downloaded about 210M per days, or 5.8B times per month, or 2250 "installs" per second)

```python
$ python -c 'import pandas as pd;print(pd.read_html("https://pypistats.org/top")[1][2].sum())'
213946761

$ python -c 'import pandas as pd;print(pd.read_html("https://pypistats.org/top")[3][2].sum())'
5833512800
```

* Python is a "glue language" - in many ways
* Python has a few downsides ("deployment" and "packaging", requires more discipline in my experience to write robust code)

### Python Eras

* 1990s: scripting
* 2000s: scientific computing
* 2010s: data science (also "web")
* 2020s: ML/AI (as a guess)

### Snapshot as of 2024-01-16

About 630 KLOC C, plus a standard library of about 900 KLOC Python, plus
documentation, tutorials, etc.

```
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
...
 C                     409       550295       430438        64500        55357
 C Header              537       237280       200351        14728        22201
...
 Python               1893       912977       736017        59248       117712
 ReStructuredText      802       411335       292093            0       119242
...
===============================================================================
 Total                4210      2339000      1771030       246934       321036
===============================================================================
```

## Installation Options

* Linux Distributions come with Python installed (on Ubuntu, there is
  "python-is-python3", cf. [AU1296790](https://askubuntu.com/questions/1296790/python-is-python3-package-in-ubuntu-20-04-what-is-it-and-what-does-it-actually)
* [Installation on Windows](InstallWindows.md)
* On most linux distributions, you will already have Python installed
* On macOS, there is a homebrew version: [https://docs.brew.sh/Homebrew-and-Python](https://docs.brew.sh/Homebrew-and-Python)

