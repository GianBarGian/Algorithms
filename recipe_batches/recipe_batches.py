#!/usr/bin/python

import math
import functools
def recipe_batches(recipe, ingredients):
  result_list = []
  for key in recipe:
    if key in ingredients:
      result = int(ingredients[key] / recipe[key])
      result_list.append(result)
    else: 
      result_list.append(0)
  bulks = functools.reduce(lambda acc,curr: acc if acc < curr else curr, result_list)
  return bulks



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 52, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))