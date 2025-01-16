from flask import Flask, request
from sentence_transformers import SentenceTransformer
import torch
import numpy as np
import json


with open("articles.json", "r") as file:
    raw_data = file.read()
articles = json.loads(raw_data)

embeddings = np.load("embeddings.npy")

model = SentenceTransformer('all-MiniLM-L6-v2')


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this API is for searching articles using semantic search, try the '/search?query=your-query-here'"


@app.route("/search")
def search_query():
    query = request.args.get("query", "")
    if len(query) == 0:
        return articles[:5]
    query_embedding = model.encode(query)
    similarity_scores = model.similarity(query_embedding, embeddings)[0]
    top_k = 5
    scores, indices = torch.topk(similarity_scores, k=top_k)
    return [articles[i] for i in indices]
