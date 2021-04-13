import re

def create_clusters(x, cleaned_x):
    # Get the indexes of the cleaned versions that match and 
    # then form groups
    cleaned_x = list(enumerate(cleaned_x))

    clusters = []
    while(len(cleaned_x) != 0):
        # Take the first value 
        curr_val = cleaned_x[0][1]
        curr_index = cleaned_x[0][0]
        cleaned_x = cleaned_x[1:]

        # Add to unique cluster group
        clusters.append([])
        clusters[-1].append(x[curr_index])

        # Find matching entries to add to this cluster
        for entry in cleaned_x:
            index = entry[0]
            val = entry[1]
            if curr_val == val:
                clusters[-1].append(x[index])

        # Remove values already checked
        cleaned_x = [entry for entry in cleaned_x if entry[1] != curr_val]
    return clusters

def serial_cluster(serials):
    # Clean data
    clean_serials = []
    for serial in serials:
        # Removes punctuation & spaces, and converts all to uppercase
        clean_serial = re.sub(r'[^\w\s]', '', serial).replace(' ', '').upper()
        clean_serials.append(clean_serial)
    
    clusters = create_clusters(serials, clean_serials)
    return clusters

### Testing
serials = ['XYZ 12345 / ILD', 'ABC/ICL/29189NC', 'XY Z12 345 //// ILD', 'ABC...ICL--291-89N C']
print(serial_cluster(serials))