#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
	for c in h:
		print(c, h[c])


def print_hist_new(h):
    for c in sorted(h.keys()):
        print(c, h[c])

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
pledge_histogram = {}


def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def histogram_new(s):
    d = dict()
    for word in s:
        d[word] = d.get(word, 0) + 1
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    # Your code here.
    with open("pledge.txt", "r") as pledge:
        pledge_list = []
        pledge_list = [word for word in pledge.read().split()]
        #Alternative method of nested list comprehension
        #pledge_list = [word for line in pledge.readlines() for word in line.split()]
        #below are the for loops for the nested list comprehension
        #for line in pledge.readlines():
        #    for word in line.split():
        #        pledge_list.append(word)"""
    return pledge_list

###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    hist = histogram_new(get_pledge_list())
    print_hist_new(hist)

if __name__ == '__main__':
    main()
