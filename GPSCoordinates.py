import math

def getCordinatesFromCenter(pixel_length,lat, long, x, y, cx, cy):
    equator_circumference = 6371000
    polar_circumference = 6356800
    m_per_deg_long = 360 / polar_circumference
    rad_lat = (lat * math.pi / 180)
    m_per_deg_lat = 360 / (math.cos(rad_lat) * equator_circumference)
    deg_diff_long = abs(cx - x) * pixel_length * m_per_deg_long  # Number of degrees latitude as you move north/south along the line of longitude
    deg_diff_lat = abs(cy - y) * pixel_length * m_per_deg_lat  # Number of degrees longitude as you move east/west along the line of latitude
    # changing north/south moves along longitude and alters latitudinal coordinates by meters * meters per degree longitude, moving east/west moves along latitude and changes longitudinal coordinates in much the same way.
    if x > cx:
        if y >= cy:
            res_lat = lat + deg_diff_long
            res_long = long + deg_diff_lat
        else:
            res_lat = lat - deg_diff_long
            res_long = long + deg_diff_lat
    else:
        if y >= cy:
            res_lat = lat + deg_diff_long
            res_long = long - deg_diff_lat
        else:
            res_lat = lat - deg_diff_long
            res_long = long - deg_diff_lat

    return res_lat, res_long


def getCordinates(lat, long, x, y, direction):
    equator_circumference = 6371000
    polar_circumference = 6356800
    m_per_deg_long = 360 / polar_circumference
    rad_lat = (lat * math.pi / 180)
    m_per_deg_lat = 360 / (math.cos(rad_lat) * equator_circumference)
    deg_diff_long = x * m_per_deg_long  # Number of degrees latitude as you move north/south along the line of longitude
    deg_diff_lat = y * m_per_deg_lat  # Number of degrees longitude as you move east/west along the line of latitude
    # changing north/south moves along longitude and alters latitudinal coordinates by meters * meters per degree longitude, moving east/west moves along latitude and changes longitudinal coordinates in much the same way.
    if direction == 1:
        res_lat = lat + deg_diff_long
        res_long = long + deg_diff_lat  # Might need to swith the long equations for these two depending on whether  are east or west of the prime meridian
    elif direction == 2:
        res_lat = lat + deg_diff_long
        res_long = long - deg_diff_lat
    elif direction == 3:
        res_lat = lat - deg_diff_long
        res_long = long - deg_diff_lat
    elif direction == 4:
        res_lat = lat - deg_diff_long
        res_long = long + deg_diff_lat  # Might need to swith the long equations for these two depending on whether  are east or west of the prime meridian
    return res_lat, res_long


def measure(lat1, lon1, lat2, lon2):
    R = 6378.137
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat1 * math.pi / 180) * math.cos(
        lat2 * math.pi / 180) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    print(d * 1000)


lat = 36.8490881
long = -76.2544901
meters = 5  # Number of meters to calculate coords for north/south/east/west
#getCordinates(lat, long, meters, 1)
#measure(lat,-76.2544901,36.8490881,-76.2546412)