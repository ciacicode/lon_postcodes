__author__ = 'ciacicode'
import csv
import json
import pdb
import re

WESTMINSTER_CODE_REGEX = re.compile('^(?P<code>W1)[^[0-9]]')

# The postcode_parser contains a set of functions built with the goal of creating a csv containing
# geometry data for all London postcodes


def select_london_postcodes():
    """
    Uses the ukpostcodes.csv courtesy of https://github.com/Gibbs/UK-Postcodes/blob/master/postcodes.csv
    and outputs a list of postcodes only for the greater london area
    """
    with open('ukpostcodes.csv') as csv_file:
        reader = csv.DictReader(csv_file)
        output_list = []
        london_areas = ['Greater London', 'Westminster', 'City of London']
        for row in reader:
            if row['region'] in london_areas:
                output_list.append(row['postcode'])
    return output_list


def select_london_postcodes_geometry():
    """
    Compares a geojson file content with a list of london postcodes
    It outputs a list with dicts of structure
    [{name: postcode, lons: longituteds, lats: latitudes}]
    """
    final_list = []
    row_dict = {}
    # open json file into a dict
    with open('ukpostcodes.json') as json_file:
        json_data = json.load(json_file)

    uk_geometry = json_data['features']
    london_postcodes = select_london_postcodes()

    # for each feature in the features list access the name property
    # and compare it with the london_postcodes
    for item in range(0, len(uk_geometry)):
        # feature is a postcode dict containing data and name
        feature = uk_geometry[item]
        postcode = feature['properties'].values()
        pdb.set_trace()
        postcode = str(postcode[0])
        # normalise the postcode so to get only the area
        complete_postcode_area = postcode.split()[0]
        postcode_area = complete_postcode_area

        if WESTMINSTER_CODE_REGEX.match(postcode_area):
            postcode_area = WESTMINSTER_CODE_REGEX.sub(
                '\g<code>', postcode_area)

        if postcode_area in london_postcodes:
            row_dict['parent'] = complete_postcode_area
            row_dict['name'] = postcode
            geometry = feature['geometry']
            coordinates = geometry['coordinates'][0][0]
            # unzip the longitude and latitudes
            lons, lats = zip(*coordinates)
            # get rid of tuple parenthesis
            str_lons = ', '.join(map(str, lons))
            str_lats = ','.join(map(str, lats))
            row_dict['lons'] = str_lons
            row_dict['lats'] = str_lats
            final_list.append(row_dict)
            row_dict = {}
    return final_list


def create_lon_postcodes_geometry(geometry):
    """
    Receives a list of geometry data containing dicts of latitude and longitude
    Creates a csv for easy reference and mapping
    """
    with open('london_postcodes.csv', 'w') as csvfile:
        fieldnames = ['parent', 'name', 'lons', 'lats']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for postcode in range(0, len(geometry)):
            writer.writerow(geometry[postcode])

london_geometry_list = select_london_postcodes_geometry()

create_lon_postcodes_geometry(london_geometry_list)
