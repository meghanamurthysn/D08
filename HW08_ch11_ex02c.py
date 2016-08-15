#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_new(d, v):
    list_keys = []
    for k in d:
	    if d[k] == v:
		    list_keys.append(k)
    return list_keys
    raise ValueError

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
    pledge_histogram = d    
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

pledge_histogram = histogram_new(get_pledge_list())

###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
    print(reverse_lookup_new(pledge_histogram, 1))
    print(reverse_lookup_new(pledge_histogram, 9))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
