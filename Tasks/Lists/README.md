# Using a list

## Without loops




## With a loop

Given a two column file, like: 

```
3   4
4   3
2   5
1   3
3   9
3   3
```

> Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

> Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

Tips:

* you can use `open("filename.txt").read()` or the [fileinput](https://docs.python.org/3/library/fileinput.html) module to read from stdin.
* sorting may help, and there is a builtin function for that
* `sorted`
* `list.append`
* `int`
* `abs`  -- abs(a - b)

