# Using world cities database from 
# https://simplemaps.com/data/world-cities

from clusteringED import clustering_with_edit_dist
import pandas as pd
import re

class LocationClusters():
    def __init__(self):
        self.clusters = []
        self.clean_clusters = []

        # Dict to convert abbreviations
        cities_df = pd.read_csv('./worldcities.csv')
        self.codeToCountry = pd.Series(cities_df.country.values, index=cities_df.iso3).to_dict()

    def clean_location(self, location):  
        # Remove punctuation
        location = re.sub(r'[^\w\s]', '', location)
        
        # Convert abbreviations
        location_split = location.upper().split()
        for i in range(len(location_split)):
            if location_split[i] in self.codeToCountry:
                location_split[i] = self.codeToCountry[location_split[i]].upper()

        return " ".join(location_split)

    def add_entry(self, new_loc):
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




# def clean_location(location):
#     # Convert abbreviations to full names
#     cities_df = pd.read_csv('./worldcities.csv')
#     codeToCountry = pd.Series(cities_df.country.values, index=cities_df.iso3).to_dict()
    
#     location_split = location.upper().split()
#     for i in range(len(location_split)):
#         if location_split[i] in codeToCountry:
#             location_split[i] = codeToCountry[location_split[i]].upper()
#     return " ".join(location_split)

# def location_clusters(locations):
#     # Clean each location
#     cleaned_locations = list(map(clean_location, locations))
#     clusters = clustering_with_edit_dist(locations, cleaned_locations)
#     return clusters

# ### Testing
# x = ["London", "LDN", "ASIA", "US", "United Kingdom", "United States", "GBR"]
# print(location_clusters(x))