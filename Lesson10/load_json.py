# coding=utf-8
import json


json_file = open('marvel.json').read()
json_data = json.loads(json_file)

print "Esto trae jason_data\n", json_data
print "Esto trae jason_file\n", json_file
