import shlex

def extract_user_group(run_command):
    # Split the command into segments for easier analysis
    parts = shlex.split(run_command)
    
    username = None
    groupname = None
    
    # Iterate over the parts to find `useradd` and `groupadd`
    try:
        if 'groupadd' in parts:
            # Get the index of 'groupadd' and calculate position of groupname
            groupadd_index = parts.index('groupadd')
            for i in range(groupadd_index + 1, len(parts)):
                if parts[i].startswith('-'):
                    continue  # Skip flags and their possible values
                else:
                    groupname = parts[i]
                    break

        if 'useradd' in parts:
            # Get the index of 'useradd' and calculate position of username
            useradd_index = parts.index('useradd')
            # Typically, the username follows the `useradd` command, but check for flags
            for i in range(useradd_index + 1, len(parts)):
                if parts[i].startswith('-'):
                    continue  # Skip flags and their possible values
                elif len(parts) - i > 1 and groupname is None:
                    groupname = parts[i]
                    #TODO: Also check if the group is specified beforehand.
                else:
                    username = parts[i]
                    break

    except ValueError:
        # 'useradd' or 'groupadd' not found in the parts
        pass
    
    return username, groupname