from clusteringED import clustering_with_edit_dist

def goods_clusters(goods):
    clusters = clustering_with_edit_dist(goods)
    return clusters

### Testing
# x = ["hardwoord table", "plastic bottle", "Coffee Table", "Coke Bottle", "Wooden Spoons"]
# print(goods_clusters(x))