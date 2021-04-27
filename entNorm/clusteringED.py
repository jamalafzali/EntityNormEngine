from minEditDist import edit_distance, min_edit_distance
from fuzzywuzzy import fuzz

def clustering_with_edit_dist(new_entry, clean_clusters):
    MIN_EDIT_DIST = 3

    curr_min_dist = float('inf')
    min_index = -1

    # Go through all existing clusters
    for i in range(len(clean_clusters)):
        clean_cluster = clean_clusters[i]

        # Go through each existing entry in existing cluster
        for existing_entry in clean_cluster:
            curr_dist = min_edit_distance(new_entry, existing_entry)
            if curr_dist <= MIN_EDIT_DIST:
                if curr_dist <= curr_min_dist:
                    curr_min_dist = min(curr_min_dist, curr_dist)
                    min_index = i
 
    return min_index

def clustering_with_lev(new_entry, clean_clusters):
    MIN_EDIT_SCORE = 65

    curr_best_score = 0
    min_index = -1

    # Go through all existing clusters
    for i in range(len(clean_clusters)):
        clean_cluster = clean_clusters[i]

        # Go through each existing entry in existing cluster
        for existing_entry in clean_cluster:
            curr_score = fuzz.partial_ratio(new_entry, existing_entry)
            if curr_score >= MIN_EDIT_SCORE:
                if curr_score > curr_best_score:
                    curr_best_score = max(curr_best_score, curr_score)
                    min_index = i
 
    return min_index