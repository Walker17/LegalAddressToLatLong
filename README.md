# Legal Address to Latitude & Longitude

## Township System

The purpose of the township system was to provide an easily understood method for describing
and locating parcels of land recently purchased or homesteaded by the large influx of settlers.
The method of legal description used for unsubdivided lands is based on the township or grid
system of survey.

(Source: http://www.realestatemanitoba.com/module1/unit2/unit2_sess1_township.htm)

## Convert Legal Descriptions to Latitude & Longitude

By converting the legal descriptions to latitude and logitude, people can easily find the location
of the specific parcel via Google Map. It might ease the steps in doing data collection and furthur
analysis.

The script provided in this repo is the prototype version that I implement the ideas from the following
resources. However, the accuracy of the result is not as good as desired. It might be caused the incorrectly
implementing.

Sources:
1. Formula: https://www.movable-type.co.uk/scripts/latlong.html
2. Calculate Lat/Long with given distance, bearing, and an original coordinate: https://stackoverflow.com/questions/7222382/get-lat-long-given-current-point-distance-and-bearing
3. Township and Grid System: http://www.realestatemanitoba.com/module1/unit2/unit2_sess1_township.htm

## Improvment can be done
1. Improve the accuracy so that each section even quater in each township can be located
2. Expand the region that the coordinates can bu calculated (not just calculated from the first meridian, maybe second, third, etc.)
3. Batch conversion
4. Allow more formats

## Asking for suggestions
If you're also interested in it, you're very welcome to contribute to the repository, or post questions in the issues. Thank you so much.
