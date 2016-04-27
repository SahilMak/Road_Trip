#!/usr/bin/env python3.5
import sys
import math
import googlemaps

def main():
  # Initialize shortest path variables
  shortest = math.inf
  path = []
  
  # Get file and starting city from command line
  file = open(sys.argv[1])
  start = sys.argv[2]
  
  # Store city names in list
  city = file.readline().split(" ")
  length = len(city)
  city[length - 1] = city[length - 1].rstrip('\n')
  
  # Store 2 ordered cities in list
  order = file.readline.split(" ")
  if len(order) == 1:
    order = [start, start]
  else:
    order[1] = order[1].rstrip('\n')
  
  # Store distances in list
  distance = [line.split() for line in file]
  
  # Close file
  file.close()
  
  # Create list of directions
  direction = [False] * (length - 1)
  
  # Create dictionary from list of cities
  num = {city[0]:0}
  for x in range(1, length):
    num[city[x]] = x
  
  # Add starting city to beginning and end of list
  city.remove(start)
  city.insert(0, start)
  city.append(start)
  
  # Find length of initial path (if valid)
  if city.index(order[0]) <= city.index(order[1]):
    for x in range(length):
      if distance[num[city[x]]][num[city[x + 1]]] == 'Inf':
        shortest = math.inf
      else:
        shortest += int(distance[num[city[x]]][num[city[x + 1]]])
    path = city[:]
  
  # Find shortest path
  short()

main()
