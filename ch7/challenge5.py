#!/usr/bin/env python3

numbers_one = [8, 19, 148, 4]
numbers_two = [9, 1, 33, 83]
products = []

for i in numbers_one:
    for j in numbers_two:
        product = i * j
        products.append(product)

print(products) 
