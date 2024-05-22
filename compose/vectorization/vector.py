import os
import yaml
from gensim.models import Word2Vec

def load_compose_files(directory):
    """ Load and parse all Docker Compose files from the specified directory """
    trees = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.endswith('.yml'):
            with open(file_path, 'r') as file:
                compose_dict = yaml.safe_load(file)
                trees.append(compose_dict)
    return trees


def walk_tree(tree, path=None):
    """ Recursively walk through the Docker Compose structure to generate paths of nodes """
    if path is None:
        path = []
    if isinstance(tree, dict):
        for key, value in tree.items():
            new_path = path + [key]
            yield new_path
            yield from walk_tree(value, new_path)
    elif isinstance(tree, list):
        for item in tree:
            yield from walk_tree(item, path)

def prepare_data(trees):
    """ Prepare data by generating node sequences from Docker Compose ASTs """
    sequences = []
    for tree in trees:
        sequences.extend(list(walk_tree(tree)))
    return sequences

# Directory containing your Docker Compose files
compose_directory = '../../../composefiles_datastore' ## TODO

# Load and prepare data
trees = load_compose_files(compose_directory)
print("trees", trees)
sequences = prepare_data(trees)

# Train Word2Vec model
model = Word2Vec(sentences=sequences, vector_size=100, window=5, min_count=1, workers=4)

# Save the model
model.save("docker_compose_embeddings.model")

# Example of using embeddings
vector = model.wv['services']  # Get vector for 'services' node
print("Vector for 'services':", vector)