import re
from geopy.geocoders import Nominatim
import pandas as pd
from address import Address, find_address, getPostcode, compare_addr


class AddressClusters():
    """
    Class representing address clusters.
    
    ...

    Attributes
    ----------
    clusters : list 
        Contains all clusters.
    clean_clusters : list of Address objects
        Copy of clusters but each entry is replaced with a cleaned Address object.
    countriesSet : set
        Set containing all country names in the world.
    citiesSet : set
        Set containing all city names in the world.
    
    Methods
    -------
    add_entry(new_address)
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
    
    clean_address(line)
        Given an address line, will attempt to query its location.
        Function will then parse this (or original address line if no location found),
        returing an Address object.

    get_clusters()
        Returns clusters.
    
    """
    def __init__(self):
        """
        Parameters
        ----------
        clusters : list 
            Contains all clusters.
        clean_clusters : list of Address objects
            Copy of clusters but each entry is replaced with a cleaned 
            Address object.
        countriesSet : set
            Set containing all country names in the world.
        citiesSet : set
            Set containing all city names in the world.
        """
        self.clusters = []
        self.clean_clusters = []

        countries_df = pd.read_csv('./data/worldcities.csv')['country']
        self.countriesSet = set(countries_df.unique())

        cities_df = pd.read_csv('./data/worldcities.csv')['city']
        self.citiesSet = set(cities_df.unique())

    def add_entry(self, new_addr):
        """
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
        """
        clean_addr = self.clean_address(new_addr)

        for i in range(len(self.clean_clusters)):
            for j in range(len(self.clean_clusters[i])):
                existing_addr = self.clean_clusters[i][j]
                if compare_addr(clean_addr, existing_addr):
                    self.clean_clusters[i].append(clean_addr)
                    self.clusters[i].append(new_addr)
                    return

        # If no matches, then add a new cluster
        self.clean_clusters.append([clean_addr])
        self.clusters.append([new_addr])

    def clean_address(self, line):
        """
        Given an address line, will attempt to query its location.
        Function will then parse this (or original address line if no location found),
        returing an Address object.
        """
        # Create address object
        clean_address = Address(line)
        
        # Query address
        geo = find_address(line)
        if geo:
            add = geo.address
        else: # If query returns None, use original line
            add = line
        
        # Remove all punctuation
        add = re.sub(r'[^\w\s]', '', add)
        
        # Extract postcode
        postcode = getPostcode(add)
        clean_address.postcode = postcode
        
        add_split = add.title().split()
        add_list = []
        for i in range(len(add_split)):
            for j in range(i+1, len(add_split)+1):
                add_list.append(' '.join(add_split[i:j]))
        
        # Extract country
        for i in range(len(add_list)-1, -1, -1):
            if add_list[i] in self.countriesSet:
                clean_address.country = add_list[i]
                break
        
        # Extract city
        for i in range(len(add_list)-1, -1, -1):
            if add_list[i] in self.citiesSet:
                clean_address.city = add_list[i]
                break

        return clean_address
    
    def get_clusters(self):
        return self.clusters

# ## Testing
# aC = AddressClusters()
# addresses = ["Imperial Collge London", "SW7 2AZ", "SLOUGH SE12 2XY", "33 TIMBER YARD, LONDON, L1 8XY", "44 CHINA ROAD, KOWLOON, HONG KONG"]
# for addr in addresses:
#     aC.add_entry(addr)
# print(aC.get_clusters())