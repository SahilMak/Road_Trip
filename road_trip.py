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
  for n in range(math.factorial(length)):
    # Find largest mobile element
    largest = 0
    index = 0
    swap = False
    for x in range(1, length):
      if not(direction[x - 1]) and x > 1 and num[city[x]] > num[city[x - 1]] and num[city[x]] > largest:
        largest = num[city[x]]
        index = x
        swap = direction[x - 1]
      elif direction[x - 1] and x < (length - 1) and num[city[x]] > num[city[x + 1]] and num[city[x]] > largest:
        largest = num[city[x]]
        index = x
        swap = direction[x - 1]
    # Swap elements
    if not(swap):
      city[index], city[index - 1] = city[index - 1], city[index]
      direction[index - 1], direction[index - 2] = direction[index - 2], direction[index - 1]
    else:
      city[index], city[index + 1] = city[index + 1], city[index]
      direction[index - 1], direction[index] = direction[index], direction[index - 1]
    # Reverse direction of largest non-mobile element
    for x in range(length):
      if num[city[x]] > largest:
        direction[x - 1] = not(direction[x - 1])
    # Find length of current path
    total = 0
    if city.index(order[0]) <= city.index(order[1]):
      for x in range(length):
        if distance[num[city[x]]][city[x + 1]] == 'Inf':
          total = math.inf
        else:
          total += int(distance[num[city[x]]][num[city[x + 1]]])
      # Determine if current path is shortest
      if total <= shortest:
        shortest = total
        path = city[:]
  # Print shortest path
  if shortest == math.inf:
    print('No possible itinerary')
  else:
    print(path[0] + ' ' + distance[num[path[0]]][num[path[1]]] + ' ' + \
          path[1] + ' ' + distance[num[path[1]]][num[path[2]]] + ' ' + \
          path[2] + ' ' + distance[num[path[2]]][num[path[3]]] + ' ' + \
          path[3] + ' ' + distance[num[path[3]]][num[path[4]]] + ' ' + \
          path[4] + ' ' + distance[num[path[4]]][num[path[5]]] + ' ' + \
          path[5] + ' ' + distance[num[path[5]]][num[path[6]]] + ' ' + \
          path[6] + ' ' + distance[num[path[6]]][num[path[7]]] + ' ' + \
          path[7] + ' ' + distance[num[path[7]]][num[path[8]]] + ' ' + \
          path[8] + ' ' + distance[num[path[8]]][num[path[9]]] + ' ' + \
          path[9] + ' ' + distance[num[path[9]]][num[path[10]]] + ' ' + path[10])
    print(shortest)

def gmaps(city):
  maps = googlemaps.Client(key='API key')
  for x in range(len(city) - 1):
    distance = maps.distance_matrix(city[x], city[x + 1])
    print(distance['rows'][0]['elements'][0]['distance']['value'])

main()
