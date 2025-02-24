from flask import Flask, request, jsonify
from fastembed import TextEmbedding

app = Flask(__name__)

# Initialize the embedding model
embedding_model = TextEmbedding()

@app.route('/embed', methods=['POST'])
def embed_text():
    data = request.json
    documents = data.get('documents', [])
    embeddings = list(embedding_model.embed(documents))
    # Convert each embedding to a list
    embeddings_list = [embedding.tolist() for embedding in embeddings]
    return jsonify(embeddings_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000) 