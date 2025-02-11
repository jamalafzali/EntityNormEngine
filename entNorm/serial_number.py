import re

class SerialClusters():
    """
    Class representing serial number clusters.
    
    ...

    Attributes
    ----------
    clusters : list
        Contains all clusters.
    clean_clusters : list
        Copy of clusters but each entry is replaced with a cleaned version.
    
    Methods
    -------
    add_entry(new_serial)
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
    
    get_clusters()
        Returns clusters.
    
    """
    def __init__(self):
        self.clusters = []
        self.clean_clusters = []

    def add_entry(self, new_serial):
        clean_serial = re.sub(r'[^\w\s]', '', new_serial).replace(' ', '').upper()
        
        # Using clean serial, go through every other existing 
        # And find a match
        for i in range(len(self.clean_clusters)):
            if clean_serial == self.clean_clusters[i][0]:
                self.clean_clusters[i].append(clean_serial)
                self.clusters[i].append(new_serial)
                return
        # Else, make a new cluster
        self.clusters.append([new_serial])
        self.clean_clusters.append([clean_serial])

    def get_clusters(self):
        return self.clusters


### Testing
# sC = SerialClusters()
# serials = ['XYZ 12345 / ILD', 'ABC/ICL/29189NC', 'XY Z12 345 //// ILD', 'ABC...ICL--291-89N C']
# for serial in serials:
#     sC.add_entry(serial)
# print(sC.get_clusters())