# Encoding
# -*- coding: utf-8 -*-

import requests


class GoogleJson(object):
    def __init__(self):
        latitude = -33.86705
        longitude = 151.19573

        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(
            longitude) + "&radius=500&type=restaurant&keyword=cruise&key=AIzaSyBSa0SUjt7GVytZzWuzp32_nbby0RNBoNE"
        response = requests.get(url)
        data = response.json()
        Results(data["results"])


class Results(object):
    list_results = []

    def __init__(self, results):
        self.results = results
        for x in range(len(self.results)):
            self.list_results.append(self.results[x])
        Geometry(self.list_results)


class Geometry(object):
    list_geometry = []
    list_name = []

    def __init__(self, geometry):
        self.geometry = geometry
        for y in range(len(self.geometry)):
            self.list_geometry.append(self.geometry[y]['geometry'])
            self.list_name.append(geometry[y]['name'])
        LatitudeLongitude(self.list_geometry, self.list_name)


class LatitudeLongitude(object):
    def __init__(self, coords, names):
        self.coords = coords
        self.names = names
        for z in range(len(coords)):
            print "The place:", names[z], "is located in the latitude", coords[z]['location']['lat'], "with " \
                "longitude is", coords[z]['location']['lng']


GoogleJson()

