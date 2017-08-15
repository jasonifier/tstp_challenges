#!/usr/bin/env python3

about_me = {'height': 70, 'favorite_color': 'red', 'favorite_athlete': 'Stephen Curry', 'favorite_show': 'The Big Bang Theory'}

inquiry = input("Select what you want to learn about me by typing one of four letters for the attribute: (a) - 'height', (b) - 'favorite_color', (c) - 'favorite_athlete', (d) - 'favorite_show' ")

if inquiry == 'a':
    print('My height is ' + str(about_me['height']))
elif inquiry == 'b':   
    print('My favorite color is ' + about_me['favorite_color'])
elif inquiry == 'c':
    print('My favorite athlete is ' + about_me['favorite_athlete'])
elif inquiry == 'd':
    print('My favorite TV show is ' + about_me['favorite_show'])
else:
    print('You did not select a valid choice.')
