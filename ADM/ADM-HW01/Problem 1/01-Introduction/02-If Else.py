#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print((n%2==0 and (2<=n<=4 or n>=22))*"Not " + "Weird")
