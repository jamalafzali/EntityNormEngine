from serial_number import SerialClusters
from physical_goods import GoodsClusters
from locations import LocationClusters
from company_name import CompanyClusters

class EntNormEng():
    def __init__(self):
        self.clustDict = {'serial': 0, 'good': 1, 'location': 2, 'company': 3}
        self.clusters = [SerialClusters(), GoodsClusters(), LocationClusters(), CompanyClusters()]


    def add_entry(self, x, sample_type):
        # Need a classifier to auto get the sample_type
        # sample_type = classify(x)

        self.clusters[self.clustDict[sample_type]].add_entry(x)
        
    def print_clusters(self):
        total_clusters = []
        for cluster in self.clusters:
           total_clusters +=  cluster.get_clusters()
        print(total_clusters)


# ### Testing
# entNorm = EntNormEng()
# entNorm.add_entry("12345", 'serial')
# entNorm.add_entry("plastic bottle", 'good')
# entNorm.add_entry("Marks and Spencers Ltd", 'company')
# entNorm.add_entry("ASIA", 'location')
# entNorm.add_entry("12345////", 'serial')
# entNorm.add_entry("London", 'location')
# entNorm.add_entry("NVIDIA Ireland", 'company')
# entNorm.add_entry("plastic Chair", 'good')
# entNorm.add_entry("M&S Limited", 'company')
# entNorm.add_entry("LDN, GBR", 'location')
# entNorm.add_entry("12345sds////", 'serial')

# entNorm.print_clusters()


    

