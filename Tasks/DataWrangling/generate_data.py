#!/bin/bash

import random
# import pandas as pd

flags = ["A", "B", "C"]

# for date in pd.date_range("2024-01-01", "2024-02-01", freq="D"):
for i in range(1, 31):
    date = "2024-01-{:02d}".format(i)
    # filename = "{}.tsv".format(date.strftime("%Y-%m-%d"))
    filename = "{}.tsv".format(date)
    with open(filename, "w") as f:
        for i in range(86400):
            flag_1 = random.choice(flags)
            if flag_1 == "A":
                flag_2 = "ignore" if random.random() > 0.9 else "ok"
            elif flag_1 == "B":
                flag_2 = "ignore" if random.random() > 0.5 else "ok"
            else:
                flag_2 = "ignore" if random.random() > 0.1 else "ok"
            print("{}\t{}\t{}".format(flag_1, random.randint(1000, 9999), flag_2), file=f)

