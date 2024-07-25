
def bfs_search(tree, key):
    """ Perform BFS in the AST to find the first occurrence of the specified key """
    queue = [tree]
    while queue:
        current = queue.pop(0)
        # if key in current and isinstance(current, dict):
        #     return current[key]  # Return the subtree when the key is found
        if isinstance(current, dict):
            if key in current:
                return current[key]
            for subkey, subval in current.items():
                if isinstance(subval, dict):
                    queue.append(subval)
                elif isinstance(subval, list):
                    queue.extend(subval)
        elif isinstance(current, list):
            if key in current:
                return current[key]
            print("aa")
        else:
            # We do not specify antipatterns as a single string.
            continue

    return None

def dfs_match(node1, node2):
    """ Recursively match two ASTs """
    # node2 = small, node1= large ast
    if node2 == "policy_more_than_one":
        return node1 > 1
    if type(node1) != type(node2):
        return False
    if isinstance(node1, dict):
        # Check if all keys in the smaller AST (node2) exist in the larger AST (node1)
        # and if corresponding subtrees or values match
        return all(k in node1 and dfs_match(node1[k], node2[k]) for k in node2)
    elif isinstance(node1, list):
        # if len(node1) != len(node2):
        #     return False
        # return all(dfs_match(n1, n2) for n1, n2 in zip(node1, node2))
        # Instead of comparing each element in the lists to each other,
        # check if any element in the larger list matches the antipattern tree
        return any(dfs_match(subnode, node2[0]) for subnode in node1 if isinstance(node2, list) and len(node2) == 1) or \
               all(dfs_match(n1, n2) for n1, n2 in zip(node1, node2))
    elif isinstance(node1, str):
        if node2 == "bad_example" or node2== "placeholder":
            return True
        elif node2 == "not empty":
            return len(node1) > 0
        elif node2 == "not zero":
            return node1 > 0
        elif node2 == "policy_more_than_one":
            return node1 > 1
        elif "not" in node2:
            cleaned_string = node2.replace('not ', '')
            if node1 != cleaned_string:
                return True
        return node1 == node2
    else:
        return node1 == node2




