
def check_shared_volume_antipattern(node,compose_error_descriptions):
    matches = []
    if isinstance(node, dict) and 'services' in node:
        volumes = {}
        for service, config in node['services'].items():
            if 'volumes' in config:
                for volume in config['volumes']:
                    if isinstance(volume, str):
                        volume_location = volume
                    elif isinstance(volume, dict):
                        volume_location = volume.get("source")
                        if volume_location in volumes:
                            matches.append({"errorNo":"4","severity":10, "customErrorMessage":f"Antipattern found in services: {volumes[volume_location]} and {service}."})

                            # matches.append([f"Antipattern found in services: {volumes[volume]} and {service}. {compose_error_descriptions['4']}",10])
                        volumes[volume_location] = service

    return matches