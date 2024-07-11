
def bfs_search(tree, key):
    """ Perform BFS in the AST to find the first occurrence of the specified key """
    queue = [tree]
    while queue:
        current = queue.pop(0)
        if key in current:
            return current[key]  # Return the subtree when the key is found
        for subkey, subval in current.items():
            if isinstance(subval, dict):
                queue.append(subval)
            elif isinstance(subval, list):
                queue.extend(subval)
    return None

def dfs_match(node1, node2):
    """ Recursively match two ASTs """
    if type(node1) != type(node2):
        return False
    if isinstance(node1, dict):
        if node1.keys() != node2.keys():
            return False
        return all(dfs_match(node1[k], node2[k]) for k in node1)
    elif isinstance(node1, list):
        if len(node1) != len(node2):
            return False
        return all(dfs_match(n1, n2) for n1, n2 in zip(node1, node2))
    else:
        return node1 == node2




