'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

import json

infile = open('eq_data.json', 'r')
eq_data = json.load(infile)

# 1) print out the number of earthquakes

print('Number of Earthquakes:', len(eq_data['features']))
print()

# 2) iterate through the dictionary and extract the location, magnitude,
#   longitude and latitude of the location and put it in a new
#   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
#   magnitude > 6. Print out the new dictionary.

# initalise dictonary for new earthquakes, use temp_dict as temporary dictionary to append into eq_dict's list under earthquake key

eq_dict = {'earthquakes': []}
temp_dict = {}

for row in range(len(eq_data['features'])):

    if eq_data['features'][row]['properties']['mag'] > 6:

        temp_dict['location'] = eq_data['features'][row]['properties']['place']
        temp_dict['magnitude'] = eq_data['features'][row]['properties']['mag']
        temp_dict['longitude'] = eq_data['features'][row]['geometry']['coordinates'][0]
        temp_dict['latitude'] = eq_data['features'][row]['geometry']['coordinates'][1]

        eq_dict['earthquakes'].append(temp_dict)
        temp_dict = {}

print(eq_dict['earthquakes'])

# 3) using the eq_dict dictionary, print out the information as shown below (first three shown):

print()
for row in range(len(eq_dict['earthquakes'])):

    print('Location:', eq_dict['earthquakes'][row]['location'])
    print('Magnitude:', eq_dict['earthquakes'][row]['magnitude'])
    print('Longitude:', eq_dict['earthquakes'][row]['longitude'])
    print('Latitude:', eq_dict['earthquakes'][row]['latitude'])
    print()
