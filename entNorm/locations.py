# Using world cities database from 
# https://simplemaps.com/data/world-cities

from clusteringED import clustering_with_edit_dist
import pandas as pd
import re

class LocationClusters():
    """
    Class representing location clusters.
    
    ...

    Attributes
    ----------
    clusters : list
        Contains all clusters.
    clean_clusters : list
        Copy of clusters but each entry is replaced with a cleaned version.
    codeToCountry : dict
        Mapping of country code to country e.g. "USA" : "United States"

    Methods
    -------
    add_entry(new_loc)
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
    
    get_clusters()
        Returns clusters.
    
    clean_location(company)
        Converts company names to upper case and removes any punctuation.
        Replaces any country codes to their full names.

    """

    def __init__(self):
        """
        Attributes
        ----------
        clusters : list
            Contains all clusters.
        clean_clusters : list
            Copy of clusters but each entry is replaced with a cleaned version.
        codeToCountry : dict
            Mapping of country code to country e.g. "USA" : "United States"
        """
        self.clusters = []
        self.clean_clusters = []

        # Dict to convert abbreviations
        cities_df = pd.read_csv('./data/worldcities.csv')
        self.codeToCountry = pd.Series(cities_df.country.values, index=cities_df.iso3).to_dict()

    def clean_location(self, location):
        """
        Converts company names to upper case and removes any punctuation.
        Replaces any country codes to their full names.
        Returns the cleaned location.
        """  
        # Remove punctuation
        location = re.sub(r'[^\w\s]', '', location)
        
        # Convert abbreviations
        location_split = location.upper().split()
        for i in range(len(location_split)):
            if location_split[i] in self.codeToCountry:
                location_split[i] = self.codeToCountry[location_split[i]].upper()

        return " ".join(location_split)

    def add_entry(self, new_loc):
        """
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
        """
        clean_loc = self.clean_location(new_loc)

        i = clustering_with_edit_dist(clean_loc, self.clean_clusters)

        if i != -1:
            self.clusters[i].append(new_loc)
            self.clean_clusters[i].append(clean_loc)
            return
        # Else, make a new cluster
        self.clusters.append([new_loc])
        self.clean_clusters.append([clean_loc])

    def get_clusters(self):
        return self.clusters 


# ## Testing
# lC = LocationClusters()
# locs = ["London", "LDN", "ASIA", "USA", "United States", "CHINA"]
# for loc in locs:
#     lC.add_entry(loc)
# print(lC.get_clusters())
# print(lC.clean_clusters)
