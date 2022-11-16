#!/usr/bin/env python

# og_string is a string from the original csv you want. 
# For example, I copied a column that was 'Active Users' from a CSV and entered it in between 3 quote marks on either end 
og_string = """a
b
c
d
1
2
3
4
e
f
g
h
i
5
6
7"""


# og_string_2 is a string from the original csv you want. 
# For example, I copied a column that was 'Former Employees' from a CSV and entered it in between 3 quote marks on either end 

og_string_2 = """c
d
4
h
5
i
9"""

##################################################################################################################################
##################################################################################################################################


# Removes new line characters
def func(to_rm_nl):
    return ' '.join(to_rm_nl.splitlines())

# creates a new variable w/o new line chars from og_string i.e. just a string separated by spaces
a_data_nl_rm = func(og_string)

# creates a new variable w/o new line chars from og_string_2 i.e. just a string separated by spaces
b_data_nl_rm = func(og_string_2)


# takes above function and then turns it into a list separating each value by the spaces
def convert(to_make_list):
    listify = list(to_make_list.split(" "))
    return listify


# turns a_data_nl_rm into list (to be used below)
clean_og_list = convert(a_data_nl_rm)

# turns b_data_nl_rm into list (to be used below)
clean_og_list_2 = convert(b_data_nl_rm)

##################################################################################################################################
##################################################################################################################################


# This function does the heavy lifting
# It compares the data from above

def checking_lists(list1, list2):
# This variable is a bucket for duplicated items. 

    duplicates = []

    for list1_items in list1:
        for check_items in list2:
            if check_items == list1_items:
                duplicates.append(list1_items)

    print(duplicates)   
    return duplicates             


checking_lists(clean_og_list, clean_og_list_2)
