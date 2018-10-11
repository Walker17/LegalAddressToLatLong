import math
import numpy


# calculate_latlong: given a distance, bearing, and origin (the start coordinate), the function will calculate
# the new (lat, long)
# calculate_latlong: Num Num (listof Num) -> (listof Num)
# the format of origin is [lat, long]
# return: new [lat, long]
    
def calculate_latlong(d, brng, origin):
    # Radius of the Earth
    R = 6378.1
    
    # get the latitude and longitude
    lat = math.radians(origin[0])
    lon = math.radians(origin[1])
    
    # calculating new latitude and longitude
    newlat = math.asin(math.sin(lat)*math.cos(d/R) + \
             math.cos(lat)*math.sin(d/R)*math.cos(brng))

    newlon = lon + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat),
                              math.cos(d/R)-math.sin(lat)*math.sin(lat))
    
    # convert them back to decimal format
    newlat = math.degrees(newlat)
    newlon = math.degrees(newlon)
    
    return [newlat, newlon]


# extract_info: the function extracts information from legal descriptions/addresses, and conducts different
# calculation based on the description
# extract_info: Str -> (listof Num)
# return: new [lat, long]
# requires: the script currently can only deal with the format: X#-X#-#X
    # examples: SW23-19-13W -> south-west quater of the section 23, township 19, range 13, at the west of the first meridian
    #           NE2-25-23W -> north-east quater of the section 2, township 25, range 23, at the west of the first meridian
# Currently can only query from the first meridian

def extract_info(legal_description):
    '''
    For batch conversion, you can add a 'try...except...' so that it can automatically
    avoid the format of the legal address that does not match the format that the script
    can deal with.
    You don't need to modify the code, just use 'try' cover all the code in this function,
    at the end of the code, after 'return new_coord', add the except: return None
    
    You can remove all the print to avoid mass of message to be printed out
    '''
    # lat - the boundary of Canada and United States, long - the prime meridian
    origin = [49.000649, -97.457889]
    
    # location matrix - used to locate the section in a township
    loc_matrix = np.array([[31,32,33,34,35,36],
                           [30,29,28,27,26,25],
                           [19,20,21,22,23,24],
                           [18,17,16,15,14,13],
                           [7,8,9,10,11,12],
                           [6,5,4,3,2,1]], dtype=np.int8)
    '''
    list: info_part
        [0] quarter and section
        [1] township
        [2] range and direction away from the meridian
    '''
    info_part = legal_description.split('-')
    
    quarter = info_part[0][:2]
    section = int(info_part[0][2:])
    township = int(info_part[1])
    ran = int(info_part[2][0])
    direction = info_part[2][1]
    print(quarter, section, township, ran, direction)
    
    # calculate the distance away from the prime meridian/first meridian, also the distance away from the boundary of Canada
    # and United States
    dtownship_mile = township * 6
    dran_mile = ran * 6
    print(dtownship_mile, dran_mile)
    
    # find section
    print(loc_matrix)
    loc = np.where(loc_matrix == section)
    print(loc)
    
    # calculate the distance away from the right-bottom corner of the section 1 in the township
    to_township = (6 - loc[1].item()) - 1
    to_range = (6 - loc[0].item()) - 1
    
    # convert rate for converting miles to kilometers
    conv_fac = 1.609344
    
    # calculate the distance to get to each quater
    if quarter == "NW":
        dran_mile += 0.5
        dtownship_mile -= 0.5
    elif quarter == "NE":
        dran_mile += 0.5
    elif quarter == "SW":
        dtownship_mile -= 0.5
    elif quarter == "SE":
        pass
    else:
        print("quater is wrong")
        return None
    
    # identify the direction to start from the first meridian, and do the calculation
    if direction == "W":
        # add difference in section to range
        dran_mile += to_range
        dtownship_mile -= to_township
        
        brng = math.atan2(-dran_mile, dtownship_mile)
        print(math.degrees(brng))
        to_coord_distance = math.sqrt((dran_mile**2) + (dtownship_mile**2))
        to_coord_distance = to_coord_distance * conv_fac
        
    elif direction == "E":
        dran_mile += to_range
        dtownship_mile += to_township
        
        brng = math.atan2(dran_mile, dtownship_mile)
        print(math.degrees(brng))
        to_coord_distance = math.sqrt((dran_mile**2) + (dtownship_mile**2))
        to_coord_distance = to_coord_distance * conv_fac
        
    else:
        print('direction is wrong')
        return None
    
    print(dtownship_mile, dran_mile)
    
    new_coord = calculate_latlong(to_coord_distance, brng, origin)
    return new_coord
