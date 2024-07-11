from terraform.iteration import bfs_search, dfs_match


def ast_match(small_ast, large_ast):
    for key, value in small_ast.items():
        # Perform BFS to find the top-level small_ast in the large AST
        found_subtree = bfs_search(large_ast, key)

        # If found, use DFS to check for match
        if found_subtree:
            match_result = dfs_match(found_subtree, value)
            print("Match found:" if match_result else "No match found.")
        else:
            continue # Do something if needed.


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