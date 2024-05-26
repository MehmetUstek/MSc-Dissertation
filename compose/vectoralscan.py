from gensim.models import Word2Vec
from compose.parse_compose import parse_yaml_to_ast
from utils.load_json import load_json
from scipy.spatial.distance import cosine
from utils.logs.custom_formatter import logger_with_custom_formatter
from utils.logs.severity_printer import print_severity

model_path = './compose/vectorization/docker_compose_embeddings.model'
node_embeddings = Word2Vec.load(model_path)

def tree_vector(tree, model):
    """ Generate a vector for the tree using the Word2Vec model for embeddings.
        `tree` is a nested dictionary representing the AST.
        `model` is a trained Word2Vec model with embeddings for each node type.
    """
    vector = [0] * model.vector_size  # Initialize with zeros, length of vector_size in the model
    if isinstance(tree, dict):
        for node_type, subtree in tree.items():
            if node_type in model.wv:  # Check if the node type has an embedding in the model
                node_vector = model.wv[node_type]  # Get the embedding vector
                vector = [sum(x) for x in zip(vector, node_vector)]  # Sum up vectors
            if isinstance(subtree, dict):
                subtree_vector = tree_vector(subtree, model)  # Recursively process the subtree
                vector = [sum(x) for x in zip(vector, subtree_vector)]  # Sum up vectors
    elif isinstance(tree, list):
        for item in tree:
            item_vector = tree_vector(item, model)  # Process each item in the list
            vector = [sum(x) for x in zip(vector, item_vector)]  # Sum up vectors
    return vector


def cosine_similarity(vec1, vec2):
    # print("vec1:",vec1)
    # print("vec2:",vec2)
    return 1 - cosine(vec1, vec2)


def traverse_and_compare(ast, antipattern_vector, error, severity, logger, depth=0, min_depth=2,max_depth=3, path=''):
    """
    Recursively traverses an AST up to a specified maximum depth, compares each branch to an antipattern vector,
    and logs a warning if the similarity exceeds 0.85.
    
    :param ast: AST node currently being traversed.
    :param antipattern_vector: The vector representation of the antipattern.
    :param depth: Current depth in the AST.
    :param max_depth: Maximum depth to start comparisons.
    :param path: Path string for logging purposes.
    """
    if depth > max_depth:
        return  # Stop the recursion if the current depth exceeds the maximum depth
    # print("depth",depth)

    if isinstance(ast, dict):
        for key, subtree in ast.items():
            new_path = f"{path}/{key}" if path else key
            if isinstance(subtree, dict) or isinstance(subtree, list):
                traverse_and_compare(subtree, antipattern_vector,  error, severity, logger, depth+1,min_depth, max_depth, new_path)
            elif depth >= min_depth:  # Only compare at or beyond the minimum depth
                # Process and compare at the current depth if it's less than or equal to max_depth
                # print("ast",ast)
                # print("ast_depth",depth)
                branch_vector = tree_vector(ast, node_embeddings)  # Ensure you adjust this call according to your vector generation logic
                similarity = cosine_similarity(branch_vector, antipattern_vector)
                # print("cosine similarity:", similarity)
                if similarity > 0.85:
                    print_severity(logger, severity, f"High similarity found: {similarity} in branch {new_path}, in ast: {ast}")
                    # logging.warning(f"High similarity found: {similarity} in branch {new_path}, in ast {ast}")
    elif isinstance(ast, list):
        for idx, item in enumerate(ast):
            new_path = f"{path}[{idx}]"
            traverse_and_compare(item, antipattern_vector,   error, severity, logger, depth,min_depth, max_depth, new_path)

# Example usage
ast_example = {
    "services": {
        "web": {
            "image": "nginx",
            "ports": ["80:80"],
            "volumes": {"type": "bind"}
        },
        "db": {
            "image": "postgres"
        }
    }
}

# Start the traversal and comparison with a specified maximum depth

# Example usage
ast_example = {
    "services": {
        "web": {
            "image": "nginx",
            "volumes": {"type": "bind"}
        },
        "db": {
            "image": "postgres"
        }
    }
}


tree1 = {
    'services': {
        'service': {
            "volumes": { "type": "bind" }
        }
    }
}

def to_vector_and_fetch_vulnerabilities(ast, antipattern_tree,antipattern_min_depth, antipattern_depth, error, severity, logger):
    antipattern_vector = tree_vector(antipattern_tree, node_embeddings)

    traverse_and_compare(ast, antipattern_vector,min_depth=antipattern_min_depth, max_depth=antipattern_depth, error=error, severity=severity, logger=logger)

# antipattern_depth = 2
# # Example usage
# to_vector_and_fetch_vulnerabilities(ast_example,tree1, antipattern_depth)

def get_vectoral_vulnerability(compose_file_path,antipattern_tree,antipattern_min_depth, antipattern_depth, error, severity, logger):
    compose_ast = parse_yaml_to_ast(compose_file_path)
    to_vector_and_fetch_vulnerabilities(compose_ast, antipattern_tree,antipattern_min_depth, antipattern_depth, error, severity, logger)

def vectoral_scan(compose_file_path):
    antipatterns = load_json('compose/antipattern_trees_for_vectors.json')
    
    # Initiate logger
    logger = logger_with_custom_formatter(file_path=compose_file_path)

    for antipattern in antipatterns:
        antipattern_tree, antipattern_max_depth,antipattern_min_depth, error, severity = antipattern.values()
        # print(antipattern_tree)

        get_vectoral_vulnerability(compose_file_path, antipattern_tree,antipattern_min_depth, antipattern_max_depth, error, severity, logger)
