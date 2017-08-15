#!/usr/bin/env python3

locations = [(17.25,-88.80), (-35.28,149.06), (-18.12,178.42), (36.10,-112.11), (40.77,-73.96), (5.96,-62.53)]

locations_map = dict()

#zip function may help here
locations_map['Belmopan'] = locations[0]
locations_map['Canberra'] = locations[1]
locations_map['Fiji'] = locations[2]
locations_map['Grand Canyon'] = locations[3]
locations_map['New York City'] = locations[4]
locations_map['Angel Falls'] = locations[5]

for pair in locations_map.items():
    print(pair)
