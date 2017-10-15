# coding=utf-8
import json


class TheData(object):
    def __init__(self, data_object):
        self.data = data_object
        self.limit = data_object['limit']
        self.total = data_object['total']
        self.count = data_object['count']
        self.results = data_object['results']

    def get_results(self):
        return Results(self.results)


class Results(object):
    def __init__(self, results):
        self.results = results

    def get_personaje(self, pos):
        return Personaje(self.results[pos])


class Personaje(object):
    def __init__(self, personaje):
        self.__personaje = personaje
        self.__id = personaje['id']
        self.__name = personaje['name']

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_thumbnail(self):
        return Thumbnail(self.__personaje['thumbnail'])


class Thumbnail(object):
    def __init__(self, thumb):
        self.extension = thumb['extension']
        self.path = thumb['path']


class Comic(object):
    def __init__(self, comic):
        self.__comic = comic


json_file = open('marvel.json').read()
json_data = json.loads(json_file)
data = TheData(json_data['data'])

the_results = data.get_results()
personaje = None
for i in range(len(the_results.results)):
    personaje = the_results.get_personaje(i)

print personaje.get_thumbnail().path