"""
    This is a module for reading, writing and removing notes about film from .csv file
"""
import csv
import pandas as pd


def readNotes():
    data = pd.read_csv('uaFilms.csv', delimiter=';', index_col='FilmName', names=['FilmName', 'Note', 'Rating'])
    print(data)


def addNote(film_name: str, note: str, rating: int):
    if rating in range(1, 6):
        fieldnames = ['film_name', 'note', 'rating']
        with open('uaFilms.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
            writer.writerow(
                {'film_name': film_name, 'note': note, 'rating': rating}
            )
    else:
        print('Rating should be in range 1-5, you have {} instead'.format(rating))


def removeNote(index: int):
    data = pd.read_csv('uaFilms.csv', delimiter=';', index_col='FilmName', names=['FilmName', 'Note', 'Rating'])
    data = data.drop(data.index[index])
    print(data)


