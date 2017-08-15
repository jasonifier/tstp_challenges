#!/usr/bin/env python3

artists = ['Diddy','Linkin Park','Jay-Z','Eminem','Imagine Dragons']

songs = [['Coming Home'], ['Numb','In The End','Heavy'], ['Run This Town'], ['Not Afraid','Lose Yourself'], ['Believer','Radioactive']]

songs_by_artist = dict(zip(artists,songs))

#print(songs_by_artist)

# exploring sets in Python

all_artists = list()
for key in songs_by_artist:
    for val in songs_by_artist[key]:
        all_artists.append(key)

print(str(len(all_artists)) + ' artists in the album')

uniq_artists = set(all_artists)

print(str(len(uniq_artists)) + ' unique artists')

print(len(uniq_artists) == len(artists))
