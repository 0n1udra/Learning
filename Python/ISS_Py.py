#!/usr/bin/env python
#https://codeclubprojects.org/en-GB/python/iss/
import json
import turtle
import urllib.request
import turtle

from datetime import datetime


iss_people_url = "http://api.open-notify.org/astros.json"
iss_loc_url = "http://api.open-notify.org/iss-now.json"

people_response = urllib.request.urlopen(iss_people_url)
loc_response = urllib.request.urlopen(iss_loc_url)

people_result = json.loads(people_response.read())
loc_result = json.loads(loc_response.read())

def read_Data(data):
    for k, v in data.items():
        if type(v) == dict:
            print(f"\t{k}:")
            for k, v in v.items():
                print(f"\t\t{k}: {v}")
        elif type(v) in (list, tuple, set):
            print(f"\t{k}:")
            for i in v:
                print(f"\t\t{i}")
        else:
            print(f"\t{k}: {v}")


print("ISS People Data:")
read_Data(people_result)

print("ISS Location Data:")
read_Data(loc_result)


print(datetime.fromtimestamp(loc_result["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'))