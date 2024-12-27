import numpy as np
from embed_function import embedder

def search(query, data_source, k=5):
    """
    Search function to find top k similar chunks to the query
    """

    # compute embedding for the query
    query_embedding = embedder(query)

    # normalize the query embedding
    query_norm = np.linalg.norm(query_embedding)

    # compute cosine similarities between query embedding and data source embeddings
    similarities = []
    for embedding, chunk in data_source:
        # normalize the data source embedding
        embedding_norm = np.linalg.norm(embedding)

        # compute cosine similarity
        similarity = np.dot(query_embedding, embedding) / (query_norm * embedding_norm)
        similarities.append((similarity, chunk))

    # sort the similarities in decending order
    similarities.sort(reverse=True, key=lambda x: x[0])

    top_k = similarities[:k]

    return top_k