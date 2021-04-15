import re
from clusteringED import clustering_with_lev

class CompanyClusters():
    """
    Class representing company clusters.
    
    ...

    Attributes
    ----------
    clusters : list
        Contains all clusters.
    clean_clusters : list
        Copy of clusters but each entry is replaced with a cleaned version.
    companyTypes : set
        Set containing irrelevant words in company names e.g. LTD.

    Methods
    -------
    add_entry(new_company)
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
    
    get_clusters()
        Returns clusters.
    
    clean_company(company)
        Converts company names to upper case and removes any punctuation.
        Removes any irrelevant words that exist in companyTypes set.
        An acronym is created and appended to the end of the company name.

    """
    def __init__(self):
        """
        Attributes
        ----------
        clusters : list
            Contains all clusters.
        clean_clusters : list
            Copy of clusters but each entry is replaced with a cleaned version.
        companyTypes : set
            Set containing irrelevant words in company names e.g. LTD.
        """
        self.clusters = []
        self.clean_clusters = []

        # Unimportant words that may appear in company name e.g. LTD
        self.companyTypes = set({'CIC', 'CIO', 'LTD', 'LLP', 'SLP', 'LP', 'LIMITED', \
        'CYF', 'PLC', 'CCC', 'UNLIMITED', 'UNLTD', 'ULTD', 'INC', 'INCORPORATED', 'AND'})
    

    def add_entry(self, new_company):
        """
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
        """

        clean_company = self.clean_company(new_company)
        
        i = clustering_with_lev(clean_company, self.clean_clusters)
        
        if i != -1:
            self.clusters[i].append(new_company)
            self.clean_clusters[i].append(clean_company)
            return
        # Else, make a new cluster
        self.clusters.append([new_company])
        self.clean_clusters.append([clean_company])

    def get_clusters(self):
        return self.clusters

    def clean_company(self, company):
        """
        Converts company names to upper case and removes any punctuation.
        Removes any irrelevant words that exist in companyTypes set.
        An acronym is created and appended to the end of the company name.
        Returns the cleaned company name.
        """
        clean = re.sub(r'[^\w\s]', '', company)
        word_list = clean.upper().split()
        i = 0
        while i < len(word_list):
            if word_list[i] in self.companyTypes:
                del word_list[i]
                continue
            i += 1
        
        # Get Acronym and append
        acronym = ''
        for word in word_list:
            acronym += word[0]
        
        word_list += [acronym]
        
        clean = ' '.join(word_list)
        return clean

# ## Testing
# cC = CompanyClusters()
# companies = ["Marks and Spencers LTD", "NVIDIA Ireland", "Microsoft", "Waitrose", "Microsoft Windows", "M&S Limited"]
# for company in companies:
#     cC.add_entry(company)
# print(cC.get_clusters())
# print(cC.clean_clusters)