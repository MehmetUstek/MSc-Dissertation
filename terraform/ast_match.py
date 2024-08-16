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
                return found_subtree
            else:
                continue
        else:
            continue # Do something if needed.
    return None

def missing_configuration_ast_match(small_ast, large_ast):
    for key, value in small_ast.items():
        # Perform BFS to find the top-level small_ast in the large AST
        # if key == "resource" and isinstance(value, list): # Special case for vulnerabilities that use resource at the top level like 102.
        #     # I defined everything to start below resource the level.
        #     # key = value[0] # This configuration is an example of vulnerability 102.
        #     for lst_item in value:
        #         for lst_key, lst_value in lst_item.items():
        #             print(lst_key, lst_value)
        #             if lst_key == "policy":
        #                 print("asd")
        #             found_subtree = bfs_search(large_ast, key)
        #             if found_subtree:
        #                 break
        #         if found_subtree:
        #             break
                    
        # else: # General case
        #     found_subtree = bfs_search(large_ast, key)

        found_subtree = bfs_search(large_ast, key)

        # If found, use DFS to check for missing conf.
        if found_subtree: # So the resource exists in the tree. Let's check if the configuration is missing.
            match_result = dfs_match(found_subtree, value)
            if not match_result:
                return found_subtree
            else:
                continue
        else:
            continue # Do something if needed.
    return None

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