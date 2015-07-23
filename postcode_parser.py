__author__ = 'ciacicode'
import json
import csv
import pdb

# The postcode_parser contains a set of functions built with the goal of creating a csv containing
# geometry data for all London postcodes

def select_london_postcodes():
    """
    Uses the ukpostcodes.csv courtesy of https://github.com/Gibbs/UK-Postcodes/blob/master/postcodes.csv
    and outputs a list of postcodes only for the greater london area
    """
    with open ('ukpostcodes.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        output_list = []
        for row in reader:
            if row['region'] == 'Greater London':
                output_list.append(row['postcode'])
    return output_list

def select_london_postcodes_geometry():
    """
    Compares a geojson file content with a list of london postcodes
    It outputs a dict of structure
    {name: postcode, geometry: [lon,lat]}
    """
    row_dict = {}
    # open json file into a dict
    with open('ukpostcodes.json') as json_file:
        json_data = json.load(json_file)

    uk_geometry = json_data['features']
    london_postcodes = select_london_postcodes()

    # for each feature in the features list access the name property
    # and compare it with the london_postcodes
    for item in range(0,len(uk_geometry)):
        # feature is a postcode dict containing data and name
        feature = uk_geometry[item]
        postcode = feature['properties'].values()
        postcode = str(postcode[0])

        #normalise the postcode so to get only the area
        postcode = postcode[:-2]
        if postcode in london_postcodes:
            row_dict['name'] = postcode
            geometry = feature['geometry']
            pdb.set_trace()
            coordinates = geometry['coordinates'][0][0]




