# Project
This project aims to create a reliable geometry data set to use to map London Postcodes. 
The json data contains all main uk postcode areas and their geometry, the lon_postcodes_geometry.csv document instead
only contains postcode geometry in the structure

parent        | name   | lons                | lats                |
--------------| ------ |---------------------|---------------------|
postcode area |postcode|string of longitudes | string of latitudes |

It is important to notice that the latitude and longitude values are strings in the csv. To be used by a mapping library
they will have to be converted to floats prior to use.

## Licensing and Data sources

Geometry data was obtained thanks to http://www.opendoorlogistics.com/data/

* Contains Royal Mail data © Royal Mail copyright and database right 2015
* Contains National Statistics data © Crown copyright and database right 2015.

Any redistribution of this reconstructed dataset must contain these original attribution statements, together with a requirement that any further sub-licences do the same. See http://www.ordnancesurvey.co.uk/docs/licences/os-opendata-licence.pdf for more details. Ordnance Survey does not in any way endorse this reconstructed dataset.

This reconstructed dataset is also derived from:

* GSHHG – A Global Self-consistent, Hierarchical, High-resolution Geography Database http://www.ngdc.noaa.gov/mgg/shorelines/gshhs.html according to an LGPL version 3 licence https://www.gnu.org/licenses/lgpl.html.
* The Humanitarian Information Unit (HIU) World Country Polygon Datasets (https://hiu.state.gov/data/).

Postcode data was obtained thanks to https://github.com/Gibbs/UK-Postcodes/