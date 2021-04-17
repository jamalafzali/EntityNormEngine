from transformers import BertTokenizer, BertModel
import torch
from scipy.spatial.distance import cosine
from wiki import get_wiki_summary

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

        # To avoid reloading this each time
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased',
                                  output_hidden_states = True, # Whether the model returns all hidden-states.
                                  )

    def add_entry(self, new_entry):
        """
        Given a new entry, cleans the entry and tries to find a match
        with the existing clean clusters. If found, adds original and clean
        names to their respective clusters, otherwise makes a new cluster.
        """

        # Get embedding of new_entry
        clean_entry = self.get_embedding(new_entry)
        
        i = self.clustering_with_cosine(clean_entry)
        
        if i != -1:
            self.clusters[i].append(new_entry)
            self.clean_clusters[i].append(clean_entry)
            return
        # Else, make a new cluster
        self.clusters.append([new_entry])
        self.clean_clusters.append([clean_entry])

    def clustering_with_cosine(self, new_entry):
        # traverse existing clusters
        # calc diff
        # return cluster index with largest sim
        MIN_SIM = 0.75

        curr_max_sim = 0
        max_index = -1

        # Go through all existing clusters
        for i in range(len(self.clean_clusters)):
            clean_cluster = self.clean_clusters[i]

            # Go through each existing entry in existing cluster
            for existing_entry in clean_cluster:
                curr_sim = 1 - cosine(new_entry, existing_entry)
                if curr_sim >= MIN_SIM:
                    if curr_sim > curr_max_sim:
                        curr_max_sim = curr_sim
                        max_index = i
 
        return max_index

    def get_embedding(self, new_entry):
        """
        Given a new entry, return an embedding of this.
        """
        ##############################
        # Get summary and preprocess #
        ##############################

        summary = get_wiki_summary(new_entry)
        summary = '[CLS] ' + summary + '[SEP]'

        # Tokenize the phrase
        tokenized = self.tokenizer.tokenize(summary)[:512]

        # Map tokens to vocab indicies
        indexed = self.tokenizer.convert_tokens_to_ids(tokenized)

        # Get segments of same size
        segments = [1] * len(tokenized)

        # Convert inputs to PyTorch tensors
        tokens_tensor = torch.tensor([indexed])
        segments_tensors = torch.tensor([segments])

        #################
        # Get Embedding #
        #################
        self.model.eval()

        with torch.no_grad():
            outputs = self.model(tokens_tensor, segments_tensors)
            hidden_states = outputs[2]

        token_embeddings1 = torch.stack(hidden_states, dim=0)
        token_embeddings1 = torch.squeeze(token_embeddings1, dim=1)
        
        token_vecs = hidden_states[-2][0]
        
        sentence_embedding = torch.mean(token_vecs, dim=0)

        return sentence_embedding
  
    def get_clusters(self):
        return self.clusters

        
## Will need to download some required files when running for the first time
# ## Testing
# gC = GoodsClusters()
# goods = ["hardwoord table", "Jon Snow", "Sword", "plastic bottle", "Daenerys Targaryen", "Dining Table", "chair", "Iron helmet","Coke Bottle", "Wooden Spoons"]
# for good in goods:
#     gC.add_entry(good)
# print(gC.get_clusters())