from transformers import BertTokenizer, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased',
                            output_hidden_states = True, # Whether the model returns all hidden-states.
                            )

def get_embedding(new_entry):
        """
        Given a new entry, return an embedding of this.
        """
        ##############################
        # Get summary and preprocess #
        ##############################

        summary = '[CLS] ' + new_entry + '[SEP]'

        # Tokenize the phrase
        tokenized = tokenizer.tokenize(summary)[:512]

        # Map tokens to vocab indicies
        indexed = tokenizer.convert_tokens_to_ids(tokenized)

        # Get segments of same size
        segments = [1] * len(tokenized)

        # Convert inputs to PyTorch tensors
        tokens_tensor = torch.tensor([indexed])
        segments_tensors = torch.tensor([segments])

        #################
        # Get Embedding #
        #################
        model.eval()

        with torch.no_grad():
            outputs = model(tokens_tensor, segments_tensors)
            hidden_states = outputs[2]

        token_embeddings1 = torch.stack(hidden_states, dim=0)
        token_embeddings1 = torch.squeeze(token_embeddings1, dim=1)
        
        token_vecs = hidden_states[-2][0]
        
        sentence_embedding = torch.mean(token_vecs, dim=0)

        return sentence_embedding