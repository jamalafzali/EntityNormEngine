# Helper classes / functions for addresses clusters
import re
from geopy.geocoders import Nominatim

# Variable for Nominatim
USER_AGENT = "JamalTest"

class Address():
    """ 
    Class to store cleaned Addresses in.
    """
    def __init__(self, address_line):
        self.address_line = address_line
        self.postcode = ''
        self.country = ''
        self.city = ''


def find_address(line):
    """ Helper function that queries an address line using Nominatim. """
    geolocator = Nominatim(user_agent=USER_AGENT)
    address = line.upper()
    geo = geolocator.geocode(address)
    return geo

def getPostcode(address):
    """ Helper function that extracts British postcode from an address line. """
    address = address.upper()
    postcode = ''
    clean_postcode = re.findall(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b', address)
    if clean_postcode:
        postcode = clean_postcode[0].replace(' ', '')
    return postcode

def compare_addr(addr1, addr2):
    """
    Helper function to compare two Address objects.
    Will try to match attributes in this order: postcode, country, city,
    returing True or False.
    """
    # Compare postcodes (if both exist)
    if addr1.postcode and addr2.postcode:
        if addr1.postcode == addr2.postcode:
            return True
        else:
            return False
    
    # Compare countries (if both exist)
    if addr1.country and addr2.country:
        if addr1.country == addr2.country:
            return True
        else:
            return False
    
    # Compare cities (if both exist)
    if addr1.city and addr2.city:
        if addr1.city == addr2.city:
            return True
        else:
            return False
        
    # If none exist, then we say these don't match
    return False