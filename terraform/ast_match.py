from terraform.iteration import bfs_search, dfs_match


def ast_match(small_ast, large_ast):
    for key, value in small_ast.items():
        # Perform BFS to find the top-level small_ast in the large AST
        found_subtree = bfs_search(large_ast, key)

        # If found, use DFS to check for match
        if found_subtree:
            match_result = dfs_match(found_subtree, value)
            if match_result:
            # print("Match found:" if match_result else "No match found.")
                return True
            else:
                continue
        else:
            continue # Do something if needed.
    return False

def missing_configuration_ast_match(small_ast, large_ast):
    for key, value in small_ast.items():
        # Perform BFS to find the top-level small_ast in the large AST
        found_subtree = bfs_search(large_ast, key)

        # If found, use DFS to check for missing conf.
        if found_subtree: # So the resource exists in the tree. Let's check if the configuration is missing.
            match_result = dfs_match(found_subtree, value)
            if not match_result:
                return True
            else:
                continue
        else:
            continue # Do something if needed.
    return False

# Load the full AST from the main Terraform configuration
# full_ast = parse_terraform('example.tf')

# # Define the antipattern AST
# antipattern_ast = {
#     "provider": [
#         {
#             "aws": {
#                 "region": "us-west-2"
#             }
#         }
#     ]
# }

# find_a_match(antipattern_ast, full_ast)