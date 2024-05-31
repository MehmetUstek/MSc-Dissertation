from gensim.models import Word2Vec
# Load your KeyedVectors model (replace with your actual model path)
model_path = './docker_compose_embeddings.model'  # Replace this with the actual path to your model
word2vec_model = Word2Vec.load(model_path)

# Access the KeyedVectors instance
word_vectors = word2vec_model.wv

# Iterate over the KeyedVectors object
# for word in word_vectors.index_to_key:
#     vector = word_vectors[word]
#     print(f"Word: {word}")

# Open a file to write
with open('word_vectors.txt', 'w') as file:
    for word in word_vectors.index_to_key:
        file.write(f"{word}\n")  # Convert numpy array to list for better readability

print("Word vectors have been saved to 'word_vectors.txt'.")