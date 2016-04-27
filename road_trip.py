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

main()
