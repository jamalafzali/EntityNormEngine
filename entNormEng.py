from serial_number import SerialClusters
from physical_goods import GoodsClusters
from locations import LocationClusters

class EntNormEng():
    def __init__(self):
        # Clusters will be or
        self.clustDict = {'serial': 0, 'good': 1, 'location': 2}
        self.clusters = [SerialClusters(), GoodsClusters(), LocationClusters()]


    def add_entry(self, x, sample_type):
        # Classify x
        # sample_type = 'serial'

        self.clusters[self.clustDict[sample_type]].add_entry(x)
        
    def print_clusters(self):
        total_clusters = []
        for cluster in self.clusters:
           total_clusters +=  cluster.get_clusters()
        print(total_clusters)


### Testing
entNorm = EntNormEng()
entNorm.add_entry("12345", 'serial')
entNorm.add_entry("plastic bottle", 'good')
entNorm.add_entry("12345////", 'serial')
entNorm.add_entry("London", 'location')
entNorm.add_entry("plastic Chair", 'good')
entNorm.add_entry("LDN, GBR", 'location')
entNorm.add_entry("12345sds////", 'serial')

entNorm.print_clusters()


    

