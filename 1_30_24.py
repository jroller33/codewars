'''
1/30/24
Narcissistic Number -
- Positive Number
- sum of its own digits
- each digit is raised to the power of # of digits in the base
- Ex: 153 = 1^3 + 5^3 + 3^3
'''

def narcissistic(num):
    length = len(str(num))

    split_num = [int(i) for i in str(num)]

    result = 0
    for i in split_num:
        pow = i ** length
        result += pow

    if result == num:
        print(True)
    elif result != num:
        print(False)
    else:
        raise Exception

# narcissistic(1652)
# works!
    
'''
1/31/24
divisors(n) takes an int n>1 and returns an array of all n's divisors, except n and 1.
list from smallest to largest
if it's a prime #, return f"{n} is prime"
ex: divisors(12) -> [2,3,4,6]
(25) -> [5]
(13) -> "13 is prime"
'''

def divisors(n):
    div_list = []    
    for i in (range(2, n)):
        if n % i == 0:
            div_list.append(i)
    
    if not div_list:
        print(f"{n} is prime")
    if div_list:
        print(div_list)
        
# divisors(12)
# divisors(25)
# divisors(13)
        
'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

test.assert_equals(make_readable(0), "00:00:00")
test.assert_equals(make_readable(59), "00:00:59")
test.assert_equals(make_readable(60), "00:01:00")
test.assert_equals(make_readable(3599), "00:59:59")
test.assert_equals(make_readable(3600), "01:00:00")
test.assert_equals(make_readable(86399), "23:59:59")
test.assert_equals(make_readable(86400), "24:00:00")
test.assert_equals(make_readable(359999), "99:59:59")
'''
import datetime
def make_readable(s):
    print(str(datetime.timedelta(s)))

# make_readable(0)
# make_readable(59)
# make_readable(60)
# make_readable(3599)
# make_readable(3600)
# make_readable(86399)
# make_readable(86400)
# make_readable(359999)
    
'''
"Find the odd int"
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''

from collections import Counter
def find_it(seq):
    print(Counter(seq))


find_it([1,7,7,7,3,9,9,9,7,9,10,0])

