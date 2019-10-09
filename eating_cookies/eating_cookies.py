#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
  
def eating_cookies(n, cache=None):
  result = 0
  
  if n == 0:
    return 1
  if n > 0:
    result += eating_cookies(n - 1)
  if n > 1:
    result += eating_cookies(n - 2)
  if n > 2:
    result += eating_cookies(n - 3)
  return result

print(eating_cookies(3, 0))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')