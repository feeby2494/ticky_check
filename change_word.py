#!/usr/bin/env python3

import os
import sys

file_to_mod = sys.argv[1]
old_word = sys.argv[2]
new_word = sys.argv[3]



with open(file_to_mod, "r+") as f:
    new_file = f.readlines()
    f.seek(0)
    for line in new_file:
        if old_word in line:
            f.write(line.replace(old_word, new_word))
        else:
            f.write(line)
    f.truncate()
f.close()
