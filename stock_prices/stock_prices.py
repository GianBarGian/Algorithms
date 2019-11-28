#!/usr/bin/python

import argparse
import functools
def find_max_profit(prices):
  gain_list = []
  for index in range(len(prices) - 1):
    temp = prices[index + 1:]
    max_price =functools.reduce(lambda acc,curr: acc if acc > curr else curr, temp)
    gain = max_price - prices[index]
    gain_list.append(gain)
  max_gain = functools.reduce(lambda acc,curr: acc if acc > curr else curr, gain_list)
  return max_gain

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))