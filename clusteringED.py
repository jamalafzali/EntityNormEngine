from minEditDist import edit_distance, min_edit_distance

def clustering_with_edit_dist(entry):
    MIN_EDIT_DIST = 3

    clusters = []
    curr_min_dist = float('inf')
    min_index = -1

    # Go through each new entry
    for new_entry in entry:
        clusterFound = False

        # Go through all existing clusters
        for i in range(len(clusters)):
            cluster = clusters[i]

            # Go through each existing entry in existing cluster
            for existing_entry in cluster:
                curr_dist = min_edit_distance(new_entry, existing_entry)
                if curr_dist < MIN_EDIT_DIST:
                    curr_min_dist = min(curr_min_dist, curr_dist)
                    min_index = i
                    clusterFound = True
        
        if clusterFound == True:
            clusters[min_index].append(new_entry)
        # If no matching cluster exists, make new cluster
        else:
            clusters.append([new_entry])
    return clusters

### Testing
# x = ["hardwoord table", "plastic bottle", "Coffee Table", "Coke Bottle", "Wooden Spoons"]
# print(clustering_with_edit_dist(x))
# x = ["LONDON", "LONDON ENG", "KOWLOON", "HONG KONG", "ASIA", "HNG KNG"]
# print(clustering_with_edit_dist(x))