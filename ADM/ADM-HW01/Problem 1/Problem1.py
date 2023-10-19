"""
    Sapienza University of Rome
    Algorithmic Methods of Data Mining - Fall 23
    HW01
    AmirAli Zabihi - 2113074
"""

# Introduction

## 01-Hello, World!

if __name__ == '__main__':
    print("Hello, World!")
    
## 02-If Else

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print((n%2==0 and (2<=n<=4 or n>=22))*"Not " + "Weird")

## 03-Arithmetic Operations

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b, a-b, a*b, sep="\n", end="")

## 04-Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b, a/b, sep="\n", end="")

## 05-Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

## 06-Write a Function

def is_leap(n):
    return n%4==0 and not(n%100==0 and not(n%400==0))

year = int(input())
print(is_leap(year))

## 07-Print Function

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end="")

# Data Types

## 01-List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

    print(result)

## 02-Find the Runner-Up

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = max(arr)
    while max_val in arr:
        arr.remove(max_val)
    print(max(arr))

## 03-Nested Lists

if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    
    unique_scores = sorted(set([score for name, score in records]))
    second_lowest_score = unique_scores[1]
    students_with_second_lowest = [name for name, score in records if score == second_lowest_score]
    for student in sorted(students_with_second_lowest):
        print(student)

## 04-Finding the Percentages

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

   
    query_scores = student_marks[query_name]
    average = sum(query_scores) / len(query_scores)

    print("{:.2f}".format(average))

# Strings

## 01-Swap Case

def swap_case(s):
     
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
## 02-Split & Join

def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
## 03-

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
## 04-

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return "".join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
## 05-

def count_substring(s, sub):
    n = 0
    for i in range(len(s)-len(sub)+1):
        for j in range(len(sub)):
            st = 1
            if s[i+j] != sub[j]:
                st = 0
                break
        if st == 1:
            n += 1
            st = 0
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
## 06-

