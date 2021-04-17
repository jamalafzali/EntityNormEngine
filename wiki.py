import wikipedia

def get_wiki_summary(query):
    """ 
    Given a query, function returns the first sentence of 
    Wikipedia article.
    """
    queries = wikipedia.search(query, suggestion=False)
    
    summary = ''
    for q in queries:
        try:
            summary = wikipedia.summary(q, sentences=1, auto_suggest=False)
        except wikipedia.DisambiguationError:
            continue
        except wikipedia.PageError:
            continue
        break
    return summary

## Testing
# print(get_wiki_summary("Dining Table"))
# print(get_wiki_summary("Chair"))