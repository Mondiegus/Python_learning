import numpy as np
import pandas as pd

class Astronaut:
    def __init__(self, name, surname, age_of_birth):
        self.name = name
        self.surname = surname
        self.age_of_birth = age_of_birth


class Location:
    def __init__(self, name, place, state):
        self.name = name
        self.place = place
        self.state = state

class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.species = species
        self.petal_width = petal_width
        self.petal_length = petal_length
        self.sepal_width = sepal_width
        self.sepal_length = sepal_length

    @property
    def total(self):
        return(self.petal_width + self.petal_length + self.sepal_width + self.sepal_length)

    def mean(self, number_of_elements=4):
        return(self.total / number_of_elements)


twardowski = Astronaut('Jan', 'Twardowski', '1961-04-12')
watney = Astronaut('Mark', 'Watney', '1969-07-21')
jsc = Location('Kennedy Space Center', 'Merritt Island', 'FL')
ksc = Location('Johnson Space Center', 'Houston', 'TX')
jpl = Location('Jet Propulsion Laboratory', 'Pasadena', 'TX')

cos1 = Iris(5.8,2.7,5.1,1.9,'virginica')
cos2 = Iris(5.1,3.5,1.4,0.2,'setosa')

print(f"Dla {cos1.species}:\r\n suma: {cos1.total} \r\n średnia: {cos1.mean()}")
print(f"Dla {cos2.species}:\r\n suma: {cos2.total} \r\n średnia: {cos2.mean()}")

