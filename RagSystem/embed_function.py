import torch
from transformers import AutoTokenizer, AutoModel

model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def embedder(chunk):
    tokens = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        model_output = model(**tokens)

    embeddings = model_output.last_hidden_state[:, 0, :]
    embed = embeddings[0].numpy()
    return embed