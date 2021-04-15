from clusteringED import clustering_with_edit_dist

class GoodsClusters():
    """
    Class representing physical goods clusters.
    
    ...

    Attributes
    ----------
    clusters : list
        Contains all clusters.
    clean_clusters : list
        Copy of clusters but each entry is replaced with a cleaned version.
    
    Methods
    -------
    add_entry(new_loc)
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
    
    get_clusters()
        Returns clusters.
    
    """
    def __init__(self):
        self.clusters = []
        self.clean_clusters = []

    def add_entry(self, new_good):
        """
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
        """

        # Long term goal to try incorporate BERT 
        i = clustering_with_edit_dist(new_good, self.clean_clusters)
        
        if i != -1:
            self.clusters[i].append(new_good)
            self.clean_clusters[i].append(new_good)
            return
        # Else, make a new cluster
        self.clusters.append([new_good])
        self.clean_clusters.append([new_good])

    def get_clusters(self):
        return self.clusters


# ## Testing
# gC = GoodsClusters()
# goods = ["hardwoord table", "plastic bottle", "Coffee Table", "Coke Bottle", "Wooden Spoons"]
# for good in goods:
#     gC.add_entry(good)
# print(gC.get_clusters())