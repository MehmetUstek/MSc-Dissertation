def is_subset(dict1, dict2):
    """
    Check if all key-value pairs in dict1 are present in dict2.
    
    Args:
    dict1 (dict): The smaller dictionary to check.
    dict2 (dict): The larger dictionary to compare against.
    
    Returns:
    bool: True if dict1 is a subset of dict2, False otherwise.
    """
    return all(dict1.get(key) == dict2.get(key) for key in dict1)

