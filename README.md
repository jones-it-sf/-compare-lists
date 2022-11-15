# compare-lists
Helps you compare two "columns" of data -- Compare Active Employees in one application to Former Employees in another application to make sure there is no overlap. 

Starts with two variables: og_string and og_string_2

I have only used it by copying a column from a .csv and pasting it into the variables.

**Example Data in Variables:**
###########
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

og_string_2 = """c
d
4
h
5
i
9"""
###########

**Once you have entered in the data to the variables:**
1) Save
2) Make sure file is executable via chmod +x filename
3) If you want to run from anywhere, add file to path. Otherwise from terminal, make sure you are in the same directory as the file.
   Ex: michael@JIT-Michael-Woods-MacBook-Pro ~ % cd Desktop
       michael@JIT-Michael-Woods-MacBook-Pro Desktop % python3 check_for_same.py
4) **Samle Output based on above data:**
   ['c', 'd', '4', 'h', 'i', '5']
      
**So:**
If you consider og_string and og_string_2 to be "Active Users" and "Former Employees" respectively, you could make the assumption that either there are former employees listed as active (really bad) or you have active employees listed as former employees (annoying and needs to be changed). 














