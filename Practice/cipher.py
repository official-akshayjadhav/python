#
#problem :
#   ref. : hackerrank -> PRactice -> Algorithm -> Bit Manupulation -> Cipher

 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cipher function below.
def cipher(n, k, s):
    m_len = n

    if k <= 1 :
        return s
    #else part
    m = []
    m.append(s[0])
    for i in range(0, k-2) :
        m.append(s[i+1] and 0)

    return m

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = cipher(n, k, s)

    #fptr.write(''+result + '\n')
    result = ''.join(str(x) for x in result)
    print(result)

    #fptr.close()
