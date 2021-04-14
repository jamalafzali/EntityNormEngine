from clusteringED import clustering_with_edit_dist
# from minEditDist import edit_distance, min_edit_distance


class GoodsClusters():
    def __init__(self):
        self.clusters = []
        self.clean_clusters = []

    def add_entry(self, new_good):
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