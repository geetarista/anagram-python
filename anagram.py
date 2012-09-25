#! /usr/env/bin python

import sys

if len(sys.argv) < 2:
    print "Please pass in a file. Examples:"
    print ""
    print "  /usr/share/dict/words"
    print "  words.txt"
    sys.exit()

word_groups = {}

filename = sys.argv[1]

try:
    file = open(filename)
except IOError:
    print "%s is not a valid file." % filename
    sys.exit()

text = file.readlines()
 
for word in text:
    word = word.rstrip("\n")
    group = "".join(sorted(list(word)))
    if group in word_groups:
        word_groups[group].append(word)
    else:
        word_groups[group] = [word]

word_groups = dict(filter(lambda (k, v): len(v) > 1, word_groups.items()))

for group in word_groups.values():
    print ", ".join(group)

file.close()
