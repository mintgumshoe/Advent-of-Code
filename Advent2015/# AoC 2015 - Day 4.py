# AoC 2015 - Day 4
input = 'iwrupvqb' 

import hashlib

def solution(input): 
    n = 1
    while n < len(input): 
        str = f'{input}{n}'
        str = hashlib.md5(input.encode()).hexdigest()
        if str.startswith('00000'):
            return n
        if n % 10 == 0: 
            print(str)
        n = n + 1


print(f"Test1 - Expected: 609043 - Actual: {solution('abcdef')}")
#print(f"Test1 - Expected: 1048970 - Actual: {solution('pqrstuv')}")
#print(f"Real Hash - Input: {input} - Output: {solution(input)}")