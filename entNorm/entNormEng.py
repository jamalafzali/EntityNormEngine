# import sys
# sys.path.append('../')

from serial_number import SerialClusters
from physical_goods import GoodsClusters
from locations import LocationClusters
from company_name import CompanyClusters
from addresses import AddressClusters
# from classification import classify
from bert_embedding import get_embedding
import pickle


class EntNormEng():
    """
    Entity Normalization Engine class.
    
    ...

    Attributes
    ----------
    clustDict : dict
        dictionary containing numerical mapping of input types
    clusters : list
        list containing each input types cluster object

    
    Methods
    -------
    add_entry(sample, sample_type)
        Classifies sample into one of the cluster types, and then attempts to
        cluster it by calling that type's object's add_entry method.
        NOTE: For now, we need to manually enter in the sample_type

    print_clusters()
        Concatenates all cluster types and prints the list
    """

    def __init__(self):
        """
        Parameters
        ----------
        clustDict : dict
            dictionary containing numerical mapping of input types
        clusters : list
            list containing each input types cluster object
        """
        self.clustDict = {'serial': 0, 'good': 1, 'location': 2, 'company': 3, 'address': 4}
        self.clusters = [SerialClusters(), GoodsClusters(), LocationClusters(), CompanyClusters(), AddressClusters()]
        self.val_to_label = {0: 'company', 1: 'address', 2: 'location', 3: 'serial', 4: 'good'}

        # Loading classifier model
        filename = 'entNorm/entity_classifier.pickle'
        self.classifier = pickle.load(open(filename, 'rb'))


    def add_entry(self, sample, sample_type=''):
        """
        Classifies sample into one of the input types, and then attempts to
        cluster it by calling that type's object's add_entry method.
        NOTE: For now, we need to manually enter in the sample_type

        Parameters
        ----------
        sample : str
            The input sample
        sample_type : str
            The input sample's type. Type should match one of the entries in
            clustDict. 
            NOTE: This wil be removed when classifier is built.

        """

        # Need a classifier to auto get the sample_type
        if sample_type == '':
            sample_type = self.classify(sample)

        self.clusters[self.clustDict[sample_type]].add_entry(sample)
    
    def classify(self, sample):
        embed = get_embedding(sample.upper()).numpy()
        pred = self.val_to_label[self.classifier.predict([embed])[0]]
        print("Predicted label for", sample, "is:", pred)
        return pred.lower()


    def print_clusters(self):
        """
        Concatenates all cluster types and prints the list.
        """

        total_clusters = []
        for cluster in self.clusters:
           total_clusters += cluster.get_clusters()
        print(total_clusters)


# ### Testing - with provided labels
# entNorm = EntNormEng()
# entNorm.add_entry("12345", 'serial')
# entNorm.add_entry("plastic bottle", 'good')
# entNorm.add_entry("Marks and Spencers Ltd", 'company')
# entNorm.add_entry("ASIA", 'location')
# entNorm.add_entry("12345////", 'serial')
# entNorm.add_entry("London", 'location')
# entNorm.add_entry("Imperial College London", 'address')
# entNorm.add_entry("NVIDIA Ireland", 'company')
# entNorm.add_entry("plastic Chair", 'good')
# entNorm.add_entry("M&S Limited", 'company')
# entNorm.add_entry("SW7 2AZ", 'address')
# entNorm.add_entry("LDN, GBR", 'location')
# entNorm.add_entry("12345sds////", 'serial')

# entNorm.print_clusters()

### Testing - With automatic labels
entNorm = EntNormEng()
entNorm.add_entry("123-456-789")
entNorm.add_entry("plastic bottle")
entNorm.add_entry("Marks and Spencers Ltd")
entNorm.add_entry("ASIA")
entNorm.add_entry("123/456/789")
entNorm.add_entry("London")
entNorm.add_entry("Imperial College London")
entNorm.add_entry("NVIDIA Ireland")
entNorm.add_entry("Plastic Chair")
entNorm.add_entry("M&S Limited")
entNorm.add_entry("SW7 2AZ")
entNorm.add_entry("LDN, GBR")
entNorm.add_entry("Hardwood Table")
entNorm.add_entry("123/456/777")

entNorm.print_clusters()
    

