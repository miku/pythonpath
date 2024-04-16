# Tasks and Mini-Projects

A few tasks and mini-projects to get more familiar with Python language features.

## Represent your domain

> Use strings, ints, lists, dicts, sets to represent a typical data structure
> of your domain.

Example solution: [notebooks/represent.ipynb](notebooks/represent.ipynb)

## Number guessing game

Write a short program that implements a number guessing game. The program
chooses a number at random, then asks the user repeatedly for input. If the
user input matches the random number, the program exits, otherwise the program
gives feedback to the user, whether the guess is too high or too low.

Example solution: [notebooks/guess.ipynb](notebooks/guess.ipynb)

## First-last

Write a function that when given a sequence like a list, tuple or string,
returns the first and the last element.

```python
def firstlast(seq):
    # TODO: return first and last element (assume seq is not empty)
```

Example solution: [notebooks/firstlast.ipynb](notebooks/firstlast.ipynb)


## Trigram

Write a language guessing algorithm based on trigrams. 


## Bitcoin Price Tracking

* go to https://api.blockchain.com/v3/exchange/tickers
* request the data
* write data out as TSV
* write a separate file that creates a file "trade_volume.tsv" if it does not 