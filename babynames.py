#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.
For writing regex, it's nice to include a copy of the target
text for inspiration.
Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
Suggested milestones for incremental development:
 - Extract the year and print it
 - Extract the names and rank numbers and just print them
 - Get the names data into a dict and print it
 - Build the [year, 'name rank', ... ] list and print it
 - Fix main() to use the extract_names list
"""


def extract_names(filename):
    #names = []
    with open(filename, 'r') as file:
        # for line in file:
        #     print(line, end ="")
        match = re.search(r'Popularity\sin\s(\d\d\d\d)', file.read())
    year = [match.group(1)]

    with open(filename, 'r') as file:

        match_all = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file.read())
    year = [match.group(1)]

    """finding and organizing the names by gender boy or girl only"""
    for tup in match_all:
        male = tup[1] + ' ' + tup[0]
        female = tup[2] + ' ' + tup[0]
        year.append(male)
        year.append(female)

    return sorted(year)

    # if not year_match:
    #     return year_match
def main():

    args = sys.args[1:]

    if not args:
        print('usage:[--summaryfile] file [file ...]')
        sys.exit(1)


# if __name__ == '__main__':
#     main(sys.argv[1:])
